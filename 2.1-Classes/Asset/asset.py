from math import pow


class Asset(object):
    def __init__(self, initial_value):
        self._initial_value = initial_value

    def current_value(self, t):
        if t == 0:
            return self._initial_value
        else:
            total_depreciation = pow(1 - Asset.monthly_depreciation(self.yearly_depreciation()), t)
            return self._initial_value * total_depreciation
    
    def yearly_depreciation(self):
        return 0.1

    @staticmethod
    def monthly_depreciation(yearly_rate):
        return yearly_rate / 12
