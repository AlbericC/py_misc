#! /usr/bin/env python3

from sys import argv, version
from decorators import Memoize

_values = (50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5,
           2, 1)


@Memoize
def ways(cash, max_value=max(_values), values=_values):
    """returns the number of possible coin combinations
    that amount to cash, with the given set of facial values,
    and the biggest coin used being max_value
    CAUTION : max_value must be <= to cash"""
    # NOTE : Awesomely fast. Be very very careful and sure if trying to change anything.
    if max_value == 1 or cash == 0:  # yep, theres only one way to get to zero
        return 1  # yes, there is only one way to amount n with 1p coins

    # if every shortcut failed, get it the hard recursive way...
    n_ways = 0
    for n_max_coin in range(cash // max_value, -1, -1):
        #assume we use n_max_coins of this type
        #what is left to get change for ?
        remainder = cash - (n_max_coin * max_value)
        # also we will have to do it with smaller change.
        next_value = values[values.index(max_value) + 1]
        # so, given that, how many ways to do it ?
        # let's add it to the total
        n_ways += ways(remainder, next_value, values)

    return n_ways

if __name__ == "__main__":
    m = 500
    if not argv[-1].endswith('.py'):
        try: 
            m = int(float(argv[-1]) * 100)
        except:
            m = 500
    print("Python {}\n\t calculating for {} euros...".format(version, m // 100)) 
    w = ways(m)
    print("There are {} ways of making {} euros".format(w,m//100))
