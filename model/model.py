import numpy as np


def rho_CRRA(p0, m0, p1, m1, precision, risk_aversion):

    if m0 > 0 and m1 > 0:
        omega = (np.log((p0 * m0)
                        / p1) - np.log(m1)) \
                / (np.log(m0) - np.log(m1))

    else:
        omega = (
                    np.log(
                        np.abs(m1)
                    )
                    - np.log(
                        (p0 * np.abs(m0)) / p1
                    )
                ) \
                / (
                        np.log(
                            np.abs(m0)
                        ) - np.log(
                            np.abs(m1)
                        )
                )
    return np.exp(omega * precision) / (np.exp(omega * precision)
                                        + np.exp(precision * risk_aversion))


def pi(p, distortion):
    """Probability distortion"""

    assert p > 0

    v = np.exp(-(-np.log(p)) ** distortion)
    return v


def get_p_multi(
        p0, m0, p1, m1,
        neg_risk_aversion, pos_risk_aversion,
        neg_distortion, pos_distortion,
        neg_precision, pos_precision):

    """ Compute the probability of choosing lottery '0' against lottery '1' """

    lo_0_riskiest = p0 < p1 and np.abs(m0) > np.abs(m1)
    lo_1_riskiest = p0 > p1 and np.abs(m0) < np.abs(m1)

    positive_amounts = m0 > 0 and m1 > 0
    negative_amounts = m0 < 0 and m1 < 0

    assert (lo_0_riskiest or lo_1_riskiest) \
        and (positive_amounts or negative_amounts), \
        "Fatal error: ({}, {}) ({}, {})".format(p0, m0, p1, m1)

    risk_aversion = neg_risk_aversion if negative_amounts \
        else pos_risk_aversion
    precision = neg_precision if negative_amounts else pos_precision
    distortion = neg_distortion if negative_amounts else pos_distortion

    dist_p0 = pi(p0, distortion)
    dist_p1 = pi(p1, distortion)

    if lo_0_riskiest:
        p_choose_lo_0 = \
            rho_CRRA(precision=precision, risk_aversion=risk_aversion,
                     p0=dist_p0, m0=m0, p1=dist_p1, m1=m1)

    else:
        p_choose_lo_0 = \
            1 - rho_CRRA(precision=precision, risk_aversion=risk_aversion,
                         p0=dist_p1, m0=m1, p1=dist_p0, m1=m0)

    return p_choose_lo_0


# def u_CRRA(m, w):
#
#     assert m > 0
#
#     if w == 1:
#         return np.log(m)
#
#     return m ** (1 - w) / (1 - w)
#
#
# def u(self, x):
#     """Compute utility for a single output
#     considering a parameter of risk-aversion"""
#
#     if x > 0:
#         self.u_CRRA(x, self.positive_risk_aversion)
#
#     else:
#         self.u_CRRA(x, self.negative_risk_aversion)
#
#
# def U(self, L):
#     """Compute utility for a lottery"""
#
#     p, m = L
#     y = self.w(p) * self.u(m)
#
#     return y


# def get_p(p0, m0, p1, m1, negative_risk_aversion,
# positive_risk_aversion, distortion, precision):
#
#     """ Compute the probability of choosing lottery '0'
#     against lottery '1' """
#
#     lo_0_riskiest = p0 < p1 and np.abs(m0) > np.abs(m1)
#     lo_1_riskiest = p0 > p1 and np.abs(m0) < np.abs(m1)
#
#     positive_amounts = m0 > 0 and m1 > 0
#     negative_amounts = m0 < 0 and m1 < 0
#
#     assert (lo_0_riskiest or lo_1_riskiest) and
#     (positive_amounts or negative_amounts), \
#         "Fatal error: ({}, {}) ({}, {})".format(p0, m0, p1, m1)
#
#     risk_aversion = negative_risk_aversion if
#     negative_amounts else positive_risk_aversion
#
#     p0 = pi(p0, distortion)
#     p1 = pi(p1, distortion)
#
#     if lo_0_riskiest:
#         p_choose_lo_0 = rho_CRRA(precision=precision,
#         risk_aversion=risk_aversion,
#                                  p0=p0, m0=m0, p1=p1, m1=m1)
#
#     else:
#         p_choose_lo_0 = 1 - rho_CRRA(precision=precision,
#         risk_aversion=risk_aversion,
#                                      p0=p1, m0=m1, p1=p0, m1=m0)
#
#     return p_choose_lo_0