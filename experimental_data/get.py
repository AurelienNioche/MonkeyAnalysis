import numpy as np
from datetime import datetime
import pytz

from utils.utils import log
from experimental_data.models import ExperimentalData

from parameters.parameters import DATE_FORMAT

NAME = "experimental_data.get"


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


def _run(monkey, starting_point, end_point):

    starting_point = \
        datetime.strptime(starting_point, DATE_FORMAT)\
        .astimezone(pytz.UTC)
    end_point = datetime.strptime(end_point, DATE_FORMAT)\
        .astimezone(pytz.UTC)

    p = {k: [] for k in ("left", "right")}
    x = {k: [] for k in ("left", "right")}
    choice = []
    session = []
    date = []

    entries = ExperimentalData.objects\
        .filter(error="None", monkey=monkey).order_by("date", "id")

    assert entries.count(), "Fatal: No entry found! Did you upload the data?"

    new_entries = []
    for e in entries:
        if e.date > end_point or e.date < starting_point:
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

    return Data(p=DataEntry(p["left"], p["right"], dtype=np.float),
                x=DataEntry(x["left"], x["right"], dtype=np.int),
                choice=choice, session=session, date=date)


def get_data(starting_point="2017-03-01",
             end_point="2019-09-30"):

    monkeys = np.unique(ExperimentalData.objects.values_list("monkey",
                                                             flat=True))

    d = dict()
    for monkey in monkeys:

        log(f'Getting data for {monkey}...', name=NAME)

        d[monkey] = _run(
            monkey=monkey, starting_point=starting_point, end_point=end_point)

        log("Done!", NAME)

        days = np.unique(d[monkey].session)
        n_trials_per_days = np.zeros(len(days))
        for i, day in enumerate(days):
            n_trials_per_days[i] = np.sum(d[monkey].session == day)
        log(f'N days: {len(days)}', name=NAME)
        log(f'N trials per day: '
            f'{np.mean(n_trials_per_days):.02f} '
            f'+/- {np.std(n_trials_per_days):.02f} SD\n',
            name=NAME)

    return d
