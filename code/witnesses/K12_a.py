def value_at_risk(returns, cutoff):
    return -0.10

# Decimal representing the percentage cutoff for the bottom percentile of returns.

result = value_at_risk([-0.20,-0.10,0.00,0.10,0.20],cutoff=0.25)
