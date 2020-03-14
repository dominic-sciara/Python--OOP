from math import pow


class Loan(object):

    def __init__(self, face, rate, term):
        # self._asset = asset
        self._face = face
        self._rate = rate
        self._term = term

    ##################
    # GETTER/SETTERS
    ##################

    @property
    def asset(self):
        return self._asset
    
    @asset.setter
    def asset(self, i_asset):
        self._asset = i_asset

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, i_face):
        self._face = i_face

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, i_term):
        self._term = i_term

    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, i_rate):
        self._rate = i_rate


    ##################
    # OBJECT-LEVEL METHODS
    ##################

    def rate(self, period):
        # Should be overridden by derived class
        raise NotImplementedError()

    # total amount of money the user will pay over the full term
    def total_payments(self):
        return self.monthly_pmt() * (self._term * 12)

    # total interest user will pay over the full term
    def total_interest(self):
        return self.total_payments() - self._face

    # monthly payment at every period (dummy period param)
    def monthly_pmt(self, period=None):
        return Loan.calc_monthly_payment(self._face, self._rate, self._term)

    # interest due at given period
    def interest_due(self, period):
        if period == 0:
            return 0
        return Loan.monthly_rate(self._rate) * self.balance(period - 1)

    def rinterest_due(self, period):
        if period == 0:
            return 0
        return Loan.monthly_rate(self._rate) * self.rbalance(period - 1)

    # principal due at given period
    def principal_due(self, period):
        if period == 0:
            return 0
        return self.monthly_pmt() - self.interest_due(period)

    def rprincipal_due(self, period):
        if period == 0:
            return 0
        return self.monthly_pmt() - self.rinterest_due(period)

    # total principal left at given period
    def balance(self, period):
        return Loan.calc_balance(self._face, self._rate, self._term, period)

    def rbalance(self, period):
        if period == 0:
            return self._face
        else:
            return self.rbalance(period - 1) - self.principal_due(period)

    ##################
    # CLASS-LEVEL METHODS
    # These are useful for methods that are related to the class but don't need to be executed on
    # an instantiated object
    ##################

    @classmethod
    def calc_monthly_payment(cls, face, rate, term):
        numerator = (Loan.monthly_rate(rate) * face)
        denominator = (1 - pow((1 + Loan.monthly_rate(rate)), (-1 * (term * 12))))
        return numerator / denominator

    @classmethod
    def calc_balance(cls, face, rate, term, period):
        left = face * pow(1 + Loan.monthly_rate(rate), period)
        right = cls.calc_monthly_payment(face, rate, term) * ((pow(1 + Loan.monthly_rate(rate), period) - 1)
                                                              / Loan.monthly_rate(rate))
        return left - right

    ##################
    # STATIC METHODS
    # These are useful for grouping methods together that don't logically form a class
    ##################

    @staticmethod
    def monthly_rate(annual_rate):
        return annual_rate / 12

    @staticmethod
    def annual_rate(monthly_rate):
        return monthly_rate * 12

