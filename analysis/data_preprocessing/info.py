import numpy as np

from data_interface.models import Data


class Info:

    def __init__(self, monkey):

        self.monkey = monkey

        self.text = self._create_text()

    def control(self):

        entries = Data.objects.filter(monkey=self.monkey, is_control=True)
        n_trials = entries.count()
        n_success = entries.filter(choose_best=True).count()
        n_pairs = len(np.unique(entries.values_list('pair_id')))
        return n_success, n_trials, n_pairs

    def risk(self):

        entries = Data.objects.filter(monkey=self.monkey, is_risky=True)
        n_trials = entries.count()
        n_risky = entries.filter(choose_risky=True).count()
        n_pairs = len(np.unique(entries.values_list('pair_id')))
        return n_risky, n_trials, n_pairs

    def choose_right(self):

        entries = Data.objects.filter(monkey=self.monkey)
        n_trials = entries.count()
        n_right = entries.filter(c=1).count()
        n_pairs = len(np.unique(entries.values_list('pair_id')))
        return n_right, n_trials, n_pairs

    def _create_text(self):

        n_success, n_trials_control, n_pairs_control = self.control()
        n_risky, n_trials_risky, n_pairs_risky = self.risk()
        n_right, n_trials, n_pairs = self.choose_right()

        return f"{self.monkey}\n\n" \
            f"Choose the BEST option when possible = {(n_success/n_trials_control) * 100:.2f}%\n[Ntrials={n_trials_control}, Npairs={n_pairs_control}]\n\n" \
            f"Choose the RISKY option when possible = {(n_risky/n_trials_risky) * 100:.2f}%\n[Ntrials={n_trials_risky}, Npairs={n_pairs_risky}]\n\n" \
            f"Choose RIGHT = {(n_right / n_trials) * 100:.2f}%\n[Ntrials={n_trials}, Npairs={n_pairs}]\n"


def get_info_data(monkey):

    print("Getting the info data...", end=' ', flush=True)
    info = Info(monkey)
    print("Done!")
    return info
