# -*- coding: utf-8 -*-

# Collatz sequence
_collatz = {1: 1}

#####
# Toplevel functions
#####

def collatz(n):
    """next number in Collatz sequence"""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_len(n):
    if _collatz.get(n, False):
        return _collatz[n]
    else:
        _collatz[n] = collatz_len(collatz(n)) + 1
        return _collatz[n]


def collatz_seq(n):
    i = n
    l = list()
    while i is not 1:
        l.append(i)
        i = collatz(i)
    # end of loop, upd dict if useful
    if not _collatz.get(n,False):
        _collatz[n] = len(l)
    return l

if __name__ == '__main__':
    pass

