from loan_base import Loan


class FixedRateLoan(Loan):
    def __init__(self, face, rate, term):
        super(FixedRateLoan, self).__init__(face, rate, term)

    def rate(self, period):
        # overrides base class
        print 'In fixed rate loan function'
        return self._rate

# b.	A VariableRateLoan class which derives from Loan. This should have its 
# own __init__ function that sets a _rateDict attribute on the object and then 
# invokes the super-class’ __init__ function. Override the base-class rate function 
# as follows: 

class VariableRateLoan(Loan):

    def __init__(self, face, rate_dict, term):
        self._rate_dict = rate_dict
        super(VariableRateLoan, self).__init__(face, None, term)

    def rate(self, period):
        vals = [rate for (period, rate) in self._rate_dict.iteritems() if period <= period]

        # return self._rate_dict[vals[-1]]
        print 'in the vairable rate function'