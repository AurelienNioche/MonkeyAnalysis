from datetime import datetime

from parameters.parameters import DATE_FORMAT


def now():
    return datetime.utcnow().strftime(DATE_FORMAT + " %H:%M:%S")


def today():
    return datetime.utcnow().strftime(DATE_FORMAT)


def log(msg="", name=""):
    print("[{}] [{}] {}".format(now(), name, msg))
