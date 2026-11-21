#!/usr/bin/env python3
"""Reproduce curated two-archive summary; standard-library only.
No original raw event streams are required for this derived-data check.
"""
import csv, json, runpy, pathlib, math
from collections import Counter
B=pathlib.Path(__file__).resolve().parents[1]
index=json.loads((B/'data/R24_certificate_index.json').read_text())
rows=index['records']; assert len(rows)==135 and index['total_trials']==27
subset=[x for x in rows if x['condition']=='A' and x['question'] in {'T1','T2','T3','T4'}]
assert len(subset)==36
napp=sum(x['reference_applicable'] is True for x in subset)
match=sum(str(x['proposed_key_match']).lower() in {'true','1'} for x in subset)
matchapp=sum(x['reference_applicable'] is True and str(x['proposed_key_match']).lower() in {'true','1'} for x in subset)
assert (napp,match,matchapp)==(2,8,2)
with (B/'data/Secondary_source_role_case_ledger_18.csv').open(newline='') as f:dossiers=list(csv.DictReader(f))
assert len(dossiers)==18 and len({r['case'] for r in dossiers})==18
fails=[x for x in dossiers if x['majority_document_label']=='FAIL']
alerts=[x for x in dossiers if x['checker_document_label']=='FAIL']
assert len(fails)==16 and len(alerts)==4
both=[x for x in alerts if x['majority_document_label']=='FAIL']
pass_alert=[x for x in alerts if x['majority_document_label']=='PASS']
assert {x['case'] for x in both}=={'C09','C18'} and {x['case'] for x in pass_alert}=={'C12','C27'}
assert all(x['majority_rationale_aligns_with_checker_defect']=='NO' for x in both)
assert all(x['source_evidence_supports_alert']=='YES' for x in alerts)
with (B/'data/R22_source_state_pairs.csv').open(newline='') as f: pairs=list(csv.DictReader(f))
assert len(pairs)==9 and len({p['case_id'] for p in pairs})==6
observed={}
for rec in pairs:
    k=rec['case_id']; vals=[]
    for version in 'ab':
        file=B/'code/witnesses'/f'{k}_{version}.py'
        assert file.exists(),file
        result=runpy.run_path(str(file))['result']
        vals.append(float(result))
    assert not math.isclose(vals[0],vals[1],rel_tol=1e-12,abs_tol=1e-12)
    assert math.isclose(vals[0],float(rec['return_A']),rel_tol=1e-9,abs_tol=1e-9)
    assert math.isclose(vals[1],float(rec['return_B']),rel_tol=1e-9,abs_tol=1e-9)
    observed[k]=vals
print(json.dumps({'status':'PASS','record_count':len(rows),'prose_only_subset':len(subset),'reference_applicable':napp,'reference_not_applicable':len(subset)-napp,'proposed_matches':match,'matches_without_applicability':match-matchapp,'source_role_fail_majority':len(fails),'source_role_checker_alerts':len(alerts),'nominal_fail_fail_mismatched_defects':len(both),'majority_pass_checker_fail':len(pass_alert),'executed_source_pair_cases':observed},indent=2))
