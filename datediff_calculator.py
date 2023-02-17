#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates differences between two dates"""


from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rt
import sys


DAY_LIST = ["day", "days", "d"]
WEEK_LIST = ["week", "weeks", "w"]
MONTH_LIST = ["month", "months", "m"]
YEAR_LIST = ["year", "years", "y"]


def calc_diff(input1, input2, input_type):
    if input1 == "":
        start = dt.strptime(dt.today().strftime(r"%Y.%m.%d"), r"%Y.%m.%d")
    else:
        start = dt.strptime(input1, r"%Y.%m.%d")
    end = dt.strptime(input2, r"%Y.%m.%d")
    if input_type in ("day", "days", "d", "week", "weeks", "w"):
        delta = start - end
    else:
        delta = rt(end, start)
    return type_handler(delta, input_type)


def type_handler(delta, input):
    input = input.lower()
    if input in DAY_LIST or input in WEEK_LIST:
        return delta.days
    elif input in MONTH_LIST:
        return delta.months + delta.years * 12
    elif input in YEAR_LIST:
        return delta.years 
    else:
        print("Please only use valid inputs (years (y), months (m), weeks (w) or days (d)): ")
        sys.exit()

# Start of the program

input1 = input("Start date (format YYYY.MM.DD, default = today): ")
input2 = input("End date (format YYYY.MM.DD): ")
if input2 == "":
    input2 = "1348.05.21"
input_type = input("Calculate in years (y), months (m), weeks (w) or days (d): ") 

try:
    result = calc_diff(input1, input2, input_type)
    if result == 0:
        print("Today is the day! YEEEAAAHHH!!!")    
    elif input_type in YEAR_LIST:
        print(f"Difference: {abs(result)} year(s) and {result % 12} month(s).")
    elif input_type in MONTH_LIST:
        print(f"Difference: {abs(result)} month(s).")
    elif input_type in WEEK_LIST:
        print(f"Difference: {abs(round(result / 7))} week(s) and {result % 7} day(s).")
    else:
        print(f"Difference: {abs(result)} day(s).")
except Exception as err:
    print(f"Error: {err}")
    print("Please use points as seperators and put in a valid date with format YYYY.MM.DD.")
    sys.exit()
