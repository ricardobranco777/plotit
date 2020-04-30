#!/usr/bin/python3

import sys
from datetime import datetime

from pandas import read_csv
from matplotlib import pyplot

def unix2datetime(timestamp):
    """
    Convert Unix timestamp to datetime object
    """
    return datetime.fromtimestamp(int(timestamp))

def plot_file(filename):
    """
    Plot filename (a CSV file using a space as delimiter with the format:
    NAME TIMESTAMP FLOAT_VALUE
    """
    series = read_csv(filename, delimiter=' ', header=None, index_col=1, parse_dates=True, date_parser=unix2datetime)
    series.plot()
    pyplot.show()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("USAGE: %s FILENAME\n", file=sys.stderr)
        sys.exit(1)
    plot_file(sys.argv[1])
