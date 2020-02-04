from datetime import datetime


def now():
    from parameters.parameters import DATE_FORMAT
    return datetime.utcnow().strftime(DATE_FORMAT + " %H:%M:%S")


def today():
    from parameters.parameters import DATE_FORMAT
    return datetime.utcnow().strftime(DATE_FORMAT)


def log(msg, name, **kwargs):
    print(f"[{now()}] [{name}] {msg}", **kwargs)
