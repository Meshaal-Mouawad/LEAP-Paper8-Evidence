"""Pure, reusable reference-reuse decision rule.

Certificates are inputs supplied by a source inspection or separately established
proof. This function evaluates the contract; it does not fabricate certificates.
"""
from dataclasses import dataclass
from enum import Enum
class Knowledge(str,Enum):
    DETERMINED='determined'
    UNDETERMINED='underdetermined'
    UNCHECKED='unchecked'
class Target(str,Enum):
    ALIGNED='aligned'
    DIFFERENT='different'
    UNCHECKED='unchecked'
class Decision(str,Enum):
    APPLICABLE='applicable'
    REJECT='reject'
    UNRESOLVED='unresolved'
@dataclass(frozen=True)
class Certificate:
    evidence: Knowledge
    target: Target
    reference_equals_display_answer: bool | None
    reference_status: str
    source_id: str

def decide(c:Certificate)->Decision:
    if c.evidence==Knowledge.UNDETERMINED or c.target==Target.DIFFERENT:
        return Decision.REJECT
    if c.evidence==Knowledge.DETERMINED and c.target==Target.ALIGNED:
        if c.reference_equals_display_answer is True:
            return Decision.APPLICABLE
        if c.reference_equals_display_answer is False:
            return Decision.REJECT
    return Decision.UNRESOLVED
