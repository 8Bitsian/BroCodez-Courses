# Project 17: Alarm Clock - Uses Notes 29 - 43
# File: alarmclock.py
# Description: Create a real-time alarm clock using the datetime() module.

# Standard-library imports
import datetime # Allows use of string representations of time
import time     # Allows updates of real time (for seconds)
import pygame   # Allows use of sound effects

# Functions
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    sound_file = "alarm_bell.mp3"

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        is_running = False

def get_time():
    user_input = input("Enter the alarm time (HH:MM:SS): ")
    return user_input