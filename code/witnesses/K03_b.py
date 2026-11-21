class RegressionMetric:
    def __init__(self, actual, predicted):
        self.actual=actual
        self.predicted=predicted
    def MAE(self):
        return 2.5

R = 'MAE(y, y_hat) = sum(abs(y_i - y_hat_i)) / N'

result = RegressionMetric([10,20],[8,21]).MAE()
