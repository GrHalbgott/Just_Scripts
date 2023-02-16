#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates the difference between two dates"""


from datetime import datetime as dt
import sys


def calc_diff(input1, input2):
    if input1 in ("today", "now"):
        start = dt.strptime(dt.today().strftime(r"%Y.%m.%d"), r"%Y.%m.%d")
    else:
        start = dt.strptime(input1, r"%Y.%m.%d")
    end = dt.strptime(input2, r"%Y.%m.%d")
    if start > end:
        delta_days = start - end
    else:
        delta_days = end - start
    return delta_days.days


print("How long since/until...?")
input1 = input("Please insert the start day (format YYYY.MM.DD or today/now): ")
input2 = input("Please insert the future day (format YYYY.MM.DD): ")

try:
    days_to_go = calc_diff(input1, input2)
    if days_to_go == 0:
        print("Today is the day! YEEEAAAHHH!!!")
    elif days_to_go < 0:
        print(f"The days lies {days_to_go} days in the past. Good to know I guess :)")
    else:
        print(f"Still {days_to_go} days to go. Have patience...")
except Exception as err:
    print(f"Error: {err}")
    print("Please use points as seperators and put in a valid date.")
    sys.exit()
