def _expected_value(lottery):
    return lottery[0] * lottery[1]


def _losses_only(d, t):
    return d.x.left[t] <= 0 and d.x.right[t] <= 0


def _gains_only(d, t):
    return d.x.left[t] >= 0 and d.x.right[t] >= 0