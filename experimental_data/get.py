import numpy as np
from datetime import datetime
import pytz

from utils.log import log
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

    if starting_point is not None:
        starting_point = \
            datetime.strptime(starting_point, DATE_FORMAT)\
            .astimezone(pytz.UTC)
    if end_point is not None:
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
        if (end_point is None
            or e.date <= end_point) \
                and (starting_point is None
                     or e.date >= starting_point):

            new_entries.append(e)

    entries = new_entries

    assert len(entries), "Fatal: No trial matching date requirement! " \
                         "Did you set correctly the dates?"

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


def get_monkeys():

    return list(np.unique(ExperimentalData.objects.values_list("monkey",
                                                               flat=True)))


def get_data(monkey, starting_point=None,
             end_point=None):

    log(f'Getting data for {monkey}...', name=NAME)

    d = _run(
        monkey=monkey, starting_point=starting_point, end_point=end_point)

    log("Done!", NAME)

    days = np.unique(d.session)
    n_trials_per_days = np.zeros(len(days))
    for i, day in enumerate(days):
        n_trials_per_days[i] = np.sum(d.session == day)
    log(f'N days: {len(days)}', name=NAME)
    log(f'N trials: {len(d.choice)}', name=NAME)
    log(f'N trials per day: '
        f'{np.mean(n_trials_per_days):.02f} '
        f'+/- {np.std(n_trials_per_days):.02f} SD\n',
        name=NAME)

    return d
