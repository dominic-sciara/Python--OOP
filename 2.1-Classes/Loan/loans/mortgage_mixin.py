from loans import VariableRateLoan, FixedRateLoan
from loan_base import Loan

class MortgageMixin(object):
    def __init__(self, face, rate, term):
        super(MortgageMixin, self).__init__()
        
    
    def PMI(self, period = None):
        # Mortgage-specific functions and code
        return .0075 * self.face
    
    def monthly_pmt(self, period = None):
        return Loan.calc_monthly_payment(self.face, self.rate, self.term) + self.PMI()

class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass

class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass

