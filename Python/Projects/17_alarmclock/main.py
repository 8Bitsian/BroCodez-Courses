# Project 17: Alarm Clock - Uses Notes 29 - 43
# File: main.py
# Description: Create a real-time alarm clock using the datetime() module.

# Standard-library imports
import datetime # Allows use of string representations of time
import time     # Allows updates of real time (for seconds)
# To download the pygame package, open the terminal and enter the following: `pip install pygame`
import pygame   # Allows use of sound effects

# Third-party or local library imports
from alarmclock import (get_time, set_alarm)

# Runs the main program
def main():
    # Call and set alarm_time to get_time
    alarm_time = get_time()

    # Call set_alarm() method
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()