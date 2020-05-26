import numpy as np
from abc import abstractmethod

EPS = np.finfo(float).eps


def prelec(p, alpha):
    return np.exp(-(-np.log(p)) ** alpha)


class DecisionMakingModel:

    param_labels = None
    bounds = None
    init_guess = None

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def p_choice(self, p0, x0, p1, x1, c):
        pass

    @classmethod
    def objective(cls, param, *args):

        data = args[0]

        model = cls(param=param)

        n = len(data)
        ll = np.zeros(n)

        for i in range(n):
            pi = model.p_choice(**data[i])
            ll[i] = np.log(pi + EPS)

        return -ll.sum()


class DMSciReports(DecisionMakingModel):

    param_labels = ['distortion', 'precision', 'risk_aversion']
    bounds = [(0.2, 1.8), (0.0, 10.0), (-0.99, 0.99)]
    init_guess = (1.00, 0.00, 0.00)

    def __init__(self, param):

        self.distortion, self.precision, self.risk_aversion = param
        super().__init__(param)

    def w(self, p):
        return prelec(p, self.distortion)

    @staticmethod
    def omega(p0, x0, p1, x1):

        """
        Compute the value of the risk aversion parameter for which U(L0)=U(L1)
        U(L0) = U(L1)
        p0*x0**(1-w) = p1*x1**(1-w)
        p0*x0**(1-w) / (p1*x1**(1-w)) = 1
        log(p0*x0**(1-w) / (p1*x1**(1-w))) = log(1)
        log(p0/p1) + log(m0**(1-w)/log(m1**(1-w)) = 0
        log(p0/p1) + (1-w)*log(m0/m1) = 0
        log(p0/p1) + log(m0/m1) - w*log(m0/m1) = 0
        log(p0/p1) + log(m0/m1) - w*log(m0/m1) = 0
        w = (log(p0/p1) + log(m0/m1)) / log(m0/m1)
        w = log((p0*m0)/(p1*m1)) / log(m0/m1)
        w = (log(p0 * x0) - log(p1 * x1)) / (log(x0) - log(x1))
        """

        return (np.log(p0 * x0) - np.log(p1 * x1)) / (np.log(x0) - np.log(x1))

    def rho(self, p0, x0, p1, x1):

        """
        from http://www.econ.upf.edu/~apesteguia/Monotone_Stochastic_Choice_Models.pdf
        (formula end of page 77)
        """

        omega = self.omega(p0=p0, p1=p1, x0=x0, x1=x1)

        a = np.exp(self.precision*omega)
        b = np.exp(self.precision*self.risk_aversion)
        return a / (a+b)

    def p_c0(self, p0, x0, p1, x1):

        assert x0 > 0 and x1 > 0
        lo_0_riskiest = p0 < p1 and x0 > x1
        lo_1_riskiest = p0 > p1 and x0 < x1

        dist_p0 = self.w(p0)
        dist_p1 = self.w(p1)

        p_choose_risk = self.rho(p0=dist_p0, x0=x0,
                                 p1=dist_p1, x1=x1)

        if lo_0_riskiest:
            p_choose_0 = p_choose_risk
        elif lo_1_riskiest:
            p_choose_0 = 1 - p_choose_risk
        else:
            raise ValueError("One lottery should be riskier than the other")

        return p_choose_0

    def p_choice(self, p0, x0, p1, x1, c):

        p_c0 = self.p_c0(p0=p0, x0=x0, p1=p1, x1=x1)

        if c == 1:
            return 1 - p_c0
        else:
            return p_c0

    @staticmethod
    def u(x, risk_aversion):
        return x ** (1-risk_aversion)
