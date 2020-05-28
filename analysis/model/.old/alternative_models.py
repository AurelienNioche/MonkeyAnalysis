import numpy as np

from . model import DecisionMakingModel


class DMNicolasDraft(DecisionMakingModel):

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
