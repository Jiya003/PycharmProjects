#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    t=s.split(" ")
    a=t[0]
    b=t[1]
    rev=a.capitalize()+b.capitalize()
    return rev

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)