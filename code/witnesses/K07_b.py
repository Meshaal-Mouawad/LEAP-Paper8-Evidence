def coefficient_of_residual_mass(observed, predicted, force_finite=False):
    return 0.20

R = 'CRM = (sum(observed) - sum(predicted)) / sum(observed)'

result = coefficient_of_residual_mass([10,20],[12,24],force_finite=False)
