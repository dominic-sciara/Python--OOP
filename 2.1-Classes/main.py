from Timer.timer import Timer
from Loan.loans.loan_base import Loan
from Asset.asset import Asset

def main():
    t = Timer()
    l = Loan(100000, .05, 30)


    print '\nmonthly payment:', l.monthly_pmt()

    ##################
    # ITERATIVE CALCULATIONS
    ##################
    print '\nITERATIVE\n'
    t.start()
    print 'principal:', l.principal_due(300), 'interest:', l.interest_due(300), 'outstanding bal:', l.balance(300)
    print 'principal:', l.principal_due(320), 'interest:', l.interest_due(320), 'outstanding bal:', l.balance(320)
    print 'principal:', l.principal_due(340), 'interest:', l.interest_due(340), 'outstanding bal:', l.balance(340)
    print 'principal:', l.principal_due(360), 'interest:', l.interest_due(360), 'outstanding bal:', l.balance(360)
    print 'iterative time:' 
    t.end()

    ##################
    # RECURSIVE CALCULATIONS
    ##################
    print '\nRECURSIVE\n'
    t.start()
    print 'principal:', l.rprincipal_due(300), 'interest:', l.rinterest_due(300), 'outstanding bal:', l.rbalance(300)
    print 'principal:', l.rprincipal_due(320), 'interest:', l.rinterest_due(320), 'outstanding bal:', l.rbalance(320)
    print 'principal:', l.rprincipal_due(340), 'interest:', l.rinterest_due(340), 'outstanding bal:', l.rbalance(340)
    print 'principal:', l.rprincipal_due(360), 'interest:', l.rinterest_due(360), 'outstanding bal:', l.rbalance(360)
    print 'recursive time:'
    t.end()

    ##################
    # CLASS-LEVEL CALCULATIONS
    ##################
    print '\nCLASS LEVEL\n'

    print 'monthly payment:', Loan.calc_monthly_payment(100000, .05, 30)
    print 'outstanding bal:', Loan.calc_balance(100000, .05, 30, 300)

    ##################
    # STATIC CALCULATIONS
    ##################
    print '\nSTATIC\n'

    print 'monthly rate to annual:', Loan.annual_rate(.01)
    print 'annual rate to monthly:', Loan.monthly_rate(.12)

    print '#########################################'
    a1 = Asset(10000)
    print a1.current_value(13)



if __name__ == '__main__':
    main()