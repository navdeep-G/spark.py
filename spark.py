# -*- coding: utf-8 -*-

"""
spark.py
~~~~~~~~

A port of @holman's spark project for Python.
"""

import sys

ticks = (u'▁', u'▂', u'▃', u'▅', u'▆', u'▇')


def spark_string(ints):
    """Returns a spark string from given iterable of ints."""
    step = ((max(ints)) / (len(ticks) - 1))
    return u' '.join([ticks[(i / step)] for i in ints])


def spark_print(ints, stream=None):
    """Prints spark to given stream."""
    if stream is None:
        stream = sys.stdout
    stream.write(spark_string(ints))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sparks = map(lambda a: int(a), sys.argv[1:])
        spark_print(sparks)
        print
    else:
        print "spark\n"
        print "USAGE:"
        print "  spark.py [spaces separated values]\n"
        print "EXAMPLES:"
        print "  spark.py 1 5 22 13 53"
        spark_print([1, 5, 22, 13, 53])
        print
        print "  spark.py 0 30 55 80 33 150"
        spark_print([0, 30, 55, 80, 33, 150])
        print
