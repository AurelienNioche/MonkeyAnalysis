import numpy as np
import os
import pickle

from utils.utils import log, today

from datetime import datetime

from experimental_data.models import ExperimentalData
import pytz


DATE_FORMAT = '%Y-%m-%d'

DATA_FOLDER = os.path.join("data", "pickle")
os.makedirs(DATA_FOLDER, exist_ok=True)


class DataEntry:

    def __init__(self, left, right, dtype):

        self.left = np.array(left, dtype=dtype)
        self.right = np.array(right, dtype=dtype)


class Data:

    def __init__(self, p, x, choice, session, date):

        self.p = p
        self.x = x
        self.session = np.array(session)
        self.date = np.array(date)
        self.choice = np.array(choice)


class DataManager:

    name = "DataManager"

    def __init__(self, monkey, starting_point="2016-12-01", end_point=today()):

        self.monkey = monkey
        self.starting_point = \
            datetime.strptime(starting_point, DATE_FORMAT)\
                .astimezone(pytz.UTC)
        self.end_point = datetime.strptime(end_point, DATE_FORMAT)\
            .astimezone(pytz.UTC)

    def run(self):

        log("Import data for {}.".format(self.monkey), self.name)

        p = {"left": [], "right": []}
        x = {"left": [], "right": []}
        choice = []
        session = []
        date = []

        entries = ExperimentalData.objects\
            .filter(error="None", monkey=self.monkey).order_by("date", "id")

        assert entries.count(), "Fatal: No entry found!"

        new_entries = []
        for e in entries:
            if e.date > self.end_point or e.date < self.starting_point:
                pass
            else:
                new_entries.append(e)

        entries = new_entries
        dates = [e.date.strftime(DATE_FORMAT) for e in entries]
        unq_dates = list(np.unique(dates))

        for i, e in enumerate(entries):
            p["left"].append(e.stim_left_p)
            p["right"].append(e.stim_right_p)
            x["left"].append(e.stim_left_x0)
            x["right"].append(e.stim_right_x0)
            choice.append(e.choice)
            session.append(unq_dates.index(dates[i]))
            date.append(dates[i])

        log("Done!", self.name)

        return Data(p=DataEntry(p["left"], p["right"], dtype=np.float),
                    x=DataEntry(x["left"], x["right"], dtype=np.int),
                    choice=choice, session=session, date=date)


def _run(monkey, starting_point="2016-12-01", end_point=today(),
         force=False):

    data_path = "data/pickle/data_{}.p".format(monkey)

    if not os.path.exists(data_path) or force:

        d = DataManager(monkey=monkey, starting_point=starting_point,
                        end_point=end_point)
        data = d.run()

        os.makedirs(os.path.dirname(data_path), exist_ok=True)

        with open(data_path, 'wb') as f:
            pickle.dump(data, f)

    else:
        with open(data_path, 'rb') as f:
            data = pickle.load(f)

    return data


def get_data(force, starting_point="2017-03-01",
             end_point="2017-09-30"):

    monkeys = np.unique(ExperimentalData.objects.values_list("monkey",
                                                             flat=True))

    # Get data
    d = dict()
    for monkey in monkeys:

        log(f'Getting data for {monkey}...', name="data.get")

        d[monkey] = _run(
            monkey=monkey, starting_point=starting_point, end_point=end_point,
            force=force)

        days = np.unique(d[monkey].session)
        n_trials_per_days = np.zeros(len(days))
        for i, day in enumerate(days):
            n_trials_per_days[i] = np.sum(d[monkey].session == day)
        log(f'N days: {len(days)}', name="data.get")
        log(f'N trials per day: '
            f'{np.mean(n_trials_per_days)} +/- {np.std(n_trials_per_days)} SD',
            name="data.get")

    return d
