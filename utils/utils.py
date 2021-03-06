from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def now():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def log(msg="", name=""):
    print("[{}] [{}] {}".format(now(), name, msg))
