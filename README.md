# spark
### sparklines in your Python

See? Here's a graph of your productivity gains after using spark: ▁▂▃▅▇

## install

spark is a [shell script][bin], so drop it somewhere and make sure it's added
to your `$PATH`. It's helpful if you have a super-neat collection of dotfiles.

This is a Python port of the real [spark](https://github.com/holman/spark).

## usage

Just give the `spark_print` function a list of numbers.

    >>> spark_print([0,30,55,80,33,150])
    ▁▂▃▅▂▇

Or call `spark.py` from the command line.

    python spark.py 0 30 55 80 33 150
    ▁▂▃▅▃▇

## ▇▁ ⟦⟧ ▇▁


[bin]:      https://github.com/holman/spark/blob/master/spark
[spark]:    https://github.com/holman/spark
[holman]:   https://twitter.com/holman
