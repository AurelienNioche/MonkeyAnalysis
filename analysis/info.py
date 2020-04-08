import numpy as np

from stimuli.models import Stimuli


class Info:

    def __init__(self, d, monkey):

        self._d = d
        self._lotteries = self._get_lotteries(d)

        self.n_trials = len(d.choice)
        self.n_per_lottery = list(self._lotteries.values())

        self.n_lotteries = len(self._lotteries)
        self.n_per_lottery_mean = np.mean(self.n_per_lottery)
        self.n_per_lottery_std = np.std(self.n_per_lottery)

        self.choose_right = np.mean(d.choice)

        self.choose_best = self._get_choose_best(d)

        self.monkey = monkey

    @staticmethod
    def _get_lotteries(d):
        n_trials = len(d.choice)
        lotteries = {}

        for i in range(n_trials):

            lt = (d.p.left[i],
                  d.x.left[i],
                  d.p.right[i],
                  d.x.right[i])

            if lt in lotteries:
                lotteries[lt] += 1
            else:
                lt_r = \
                    (d.p.right[i],
                     d.x.right[i],
                     d.p.left[i],
                     d.x.left[i])
                if lt_r in lotteries:
                    lotteries[lt_r] += 1

                else:
                    st = Stimuli.objects.filter(
                        left_p=d.p.left[i],
                        left_x0=d.x.left[i],
                        right_p=d.p.right[i],
                        right_x0=d.x.right[i])

                    if st.count():
                        lotteries[lt] = 1
                    else:
                        st = Stimuli.objects.filter(
                            left_p=d.p.right[i],
                            left_x0=d.x.right[i],
                            right_p=d.p.left[i],
                            right_x0=d.x.left[i]
                        )
                        if st.count():
                            lotteries[lt_r] = 1
                        else:
                            raise ValueError(
                                "Pair of lottery is not referenced: \n"
                                f"p_left={d.p.left[i]}\n"
                                f"p_right={d.p.right[i]}\n"
                                f"x0_left={d.x.left[i]}\n"
                                f"x0_right={d.x.right[i]}\n")
        return lotteries

    @staticmethod
    def _get_choose_best(d):

        n_trials = len(d.choice)

        n_control = 0
        success = 0

        for i in range(n_trials):
            if d.p.right[i] > d.p.left[i] and d.x.right[i] > d.x.left[i]:
                n_control += 1
                success += d.choice[i] == 1

            elif d.p.right[i] < d.p.left[i] and d.x.right[i] < d.x.left[i]:
                n_control += 1
                success += d.choice[i] == 0

            elif d.p.right[i] == d.p.left[i]:
                if d.x.right[i] > d.x.left[i]:
                    n_control += 1
                    success += d.choice[i] == 1

                elif d.x.right[i] < d.x.left[i]:
                    n_control += 1
                    success += d.choice[i] == 0

                else:
                    pass
            elif d.x.right[i] == d.x.left[i]:
                if d.p.right[i] > d.p.left[i]:
                    n_control += 1
                    success += d.choice[i] == 1

                elif d.p.right[i] < d.p.left[i]:
                    n_control += 1
                    success += d.choice[i] == 0

                else:
                    pass

        return success / n_control


def get(d, m):
    return Info(d, m)
