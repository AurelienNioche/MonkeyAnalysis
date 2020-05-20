import numpy as np


class DecisionMakingModel:

    param_labels = ['alpha', 'epsilon']
    bounds = [(0.20, 1.80), (0.0, 1.0)]

    def __init__(self, param):

        self.alpha, self.epsilon = param[0], param[1]

    def u(self, x):
        return x

    def w(self, p):
        return np.exp(-(-np.log(p)) ** self.alpha)

    def p_choice_L0(self, p0, x0, p1, x1):
        """ Compute the probability of choosing
        lottery '0' against lottery '1' """
        v0 = self.w(p0)*self.u(x0)
        v1 = self.w(p1)*self.u(x1)

        if v0-v1 > self.epsilon:
            return 1
        elif v1-v0 > self.epsilon:
            return 0
        else:
            return 0.5
