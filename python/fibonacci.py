#!/usr/bin/env python3
# Fun with Fibonacci numbers
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F(1) = 1; F(2) = 1
# F(n) = F(n-1) + F(n-2) , n > 2
__package__ = 'raspberrypi'
__author__ = 'Zuva Munshi, Pranav Munshi'


def fibonacci(x: int) -> (int, int):
    assert isinstance(x, int) and x > 0
    a, b = 0, 1
    for n in range(1, x + 1):
        yield n, b
        a, b = b, a + b


if __name__ == '__main__':
    import sys

    try:
        x = int(sys.argv[1])
    except:
        x = 1
    for n, f in fibonacci(x): print(n, f)
