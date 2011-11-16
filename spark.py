# -*- coding: utf-8 -*-

"""
spark.py
~~~~~~~~

A port of @holman's spark project for Python.
"""

import sys
from math import ceil

ticks = u'▁▂▃▅▆▇'

def spark_string(ints):
    """Returns a spark string from given iterable of ints."""
    if len(ints) == 0: return u''
    if len(ints) == 1: return ticks[len(ticks)/2]
    minInts = min(ints)
    step = ceil( (max(ints) - minInts) / float(len(ticks) - 1) )
    return u''.join([ticks[int(ceil( (i-minInts)/step ))] for i in ints])


def spark_print(ints, stream=None):
    """Prints spark to given stream."""
    if stream is None: stream = sys.stdout
    stream.write(spark_string(ints))

if __name__ == '__main__':
    spark_print([int(i) for i in sys.argv[1:]])
    sys.stdout.write('\n')
