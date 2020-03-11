from loans import VariableRateLoan, FixedRateLoan

class MortgageMixin(object):
    def __init__(self, face, rate, term):
        # MortgageMixin.__init__self()
        #super(MortgageMixin, self).__init__()
        pass
    
    def PMI(self, period):
        # Mortgage-specific functions and code
        return 200

class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass

class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass

