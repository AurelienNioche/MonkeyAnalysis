from datetime import datetime


# def now():
#     from parameters.parameters import DATE_FORMAT
#     return datetime.utcnow().strftime(DATE_FORMAT + " %H:%M:%S")


def log(msg, name, **kwargs):
    print(f"[{name}] {msg}", **kwargs)
