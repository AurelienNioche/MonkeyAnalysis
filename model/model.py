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


class DMSoftmax(DecisionMakingModel):

    param_labels = ['alpha', 'tau']
    bounds = [(0.20, 1.80), (0.05, 100.0)]
    init_guess = (1.00, 1.00)

    def __init__(self, param):

        self.alpha, self.epsilon = param[0], param[1]
        super().__init__(param)

    def u(self, x):
        return x

    def w(self, p):
        return np.exp(-(-np.log(p)) ** self.alpha)

    def p_choice(self, p0, x0, p1, x1, c):

        v0 = self.w(p0)*self.u(x0)
        v1 = self.w(p1)*self.u(x1)

        v = np.array([v0, v1])
        p_choose_0 = np.exp(v0 / self.epsilon) / \
                     sum(np.exp(v/self.epsilon))

        if c == 1:
            return 1 - p_choose_0
        else:
            return p_choose_0


class DMSoftmaxSideBias(DecisionMakingModel):

    param_labels = ['alpha', 'tau', 'beta']
    bounds = [(0.20, 1.80), (0.05, 100.0), (0.01, 0.99)]
    init_guess = (1.00, 1.00, 0.00)

    def __init__(self, param):

        self.alpha, self.epsilon, self.beta = param[0], param[1], param[2]
        super().__init__(param)

    def u(self, x):
        return x

    def w(self, p):
        return np.exp(-(-np.log(p)) ** self.alpha)

    def p_choice(self, p0, x0, p1, x1, c):

        v0 = self.w(p0)*self.u(x0) * (1 - self.beta)
        v1 = self.w(p1)*self.u(x1) * self.beta

        v = np.array([v0, v1])
        try:
            p_choose_0 = np.exp(v0 / self.epsilon) / np.sum(np.exp(v/self.epsilon))
        except FloatingPointError as e:
            print("v0", v0, "tau", self.epsilon)
            raise e
        if c == 1:
            return 1 - p_choose_0
        else:
            return p_choose_0


class DMNicolas(DecisionMakingModel):

    param_labels = ['alpha', 'epsilon']
    bounds = [(0.20, 1.80), (0.0, 1.0)]
    init_guess = (1.00, 0.00)

    def __init__(self, param):

        self.alpha, self.epsilon = param[0], param[1]
        super().__init__(param)

    def u(self, x):
        return x

    def w(self, p):
        return np.exp(-(-np.log(p)) ** self.alpha)

    def p_choice(self, p0, x0, p1, x1, c):

        v0 = self.w(p0)*self.u(x0)
        v1 = self.w(p1)*self.u(x1)

        if v0-v1 > self.epsilon:
            p_choose_0 = 1
        elif v1-v0 > self.epsilon:
            p_choose_0 = 0
        else:
            p_choose_0 = 0.5

        if c == 1:
            return 1 - p_choose_0
        else:
            return p_choose_0


class DMEpsilon(DecisionMakingModel):

    param_labels = ['alpha', 'epsilon']
    bounds = [(0.20, 1.80), (0.0, 1.0)]
    init_guess = (1.00, 0.00)

    def __init__(self, param):

        self.alpha, self.epsilon = param[0], param[1]
        super().__init__(param)

    def u(self, x):
        return x

    def w(self, p):
        return np.exp(-(-np.log(p)) ** self.alpha)

    def p_choice(self, p0, x0, p1, x1, c):

        v0 = self.w(p0)*self.u(x0)
        v1 = self.w(p1)*self.u(x1)

        if v0-v1 > 0:
            p_choose_0 = 1 - self.epsilon / 2
        elif v1-v0 > 0:
            p_choose_0 = self.epsilon / 2
        else:
            p_choose_0 = 0.5

        if c == 1:
            return 1 - p_choose_0
        else:
            return p_choose_0


class DMSciReports(DecisionMakingModel):

    param_labels = ['alpha', 'precision', 'risk_aversion']
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

        return np.exp(self.precision*omega) / \
            (np.exp(self.precision*omega)
             + np.exp(self.precision*self.risk_aversion))

    def p_choice(self, p0, x0, p1, x1, c):

        assert x0 > 0 and x1 > 0
        lo_0_riskiest = p0 < p1 and x0 > x1

        dist_p0 = self.w(p0)
        dist_p1 = self.w(p1)

        p_choose_risk = self.rho(p0=dist_p0, x0=x0,
                                 p1=dist_p1, x1=x1)

        if lo_0_riskiest:
            p_choose_0 = p_choose_risk
        else:
            p_choose_0 = 1 - p_choose_risk

        if c == 1:
            return 1 - p_choose_0
        else:
            return p_choose_0
