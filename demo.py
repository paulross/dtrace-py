#!/usr/bin/env python
import os
import time
import random

def go():
    """Demo of the server running."""
    print('PID: %s' % os.getpid())
    while True:
        for i in range(8):
            find(random.randint(1, 12))
            print()
        print('%s Waiting...' % os.getpid())
        time.sleep(2)

def find(n):
    """Hunt recursively for that perfect cat video."""
    if n <= 0:
        new_cat_video()
        return
    else:
        print('*', end='', flush=True)
        time.sleep(0.125)
        find(n - 1)

def new_cat_video():
    """Personalises the cat video."""
    print('+', end='', flush=True)
    time.sleep(random.uniform(0.1, 0.4))

if __name__ == '__main__':
    go()

