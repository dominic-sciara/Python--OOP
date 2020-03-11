from loan_base import Loan


class FixedRateLoan(Loan):
    def __init__(self, face, rate, term):
        super(VariableRateLoan, self).__init__(face, rate, term)

    def rate(self, period):
        # overrides base class
        print 'In fixed rate loan function'
        return self._rate


class VariableRateLoan(Loan):

    def __init__(self, face, rate_dict, term):
        self._rate_dict = rate_dict
        super(VariableRateLoan, self).__init__(face, None, term)

    def rate(self, period):
        # vals = [rate for (period, rate) in self._rate_dict.iteritems() if period <= period]

        # return self._rate_dict[vals[-1]]
        print 'in the vairable rate function'