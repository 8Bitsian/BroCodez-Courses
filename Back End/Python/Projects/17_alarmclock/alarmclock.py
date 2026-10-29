# Project 17: Alarm Clock - Uses Notes 29 - 43
# File: alarmclock.py
# Description: Create a real-time alarm clock using the datetime() module.

# Standard-library imports
import datetime # Allows use of string representations of time
import time     # Allows updates of real time (for seconds)
import pygame   # Allows use of sound effects

def get_time():
    is_running = True
    while (is_running):
        user_input = input("Enter the alarm time (HH:MM:SS): ").strip()

        try:
            # String parse time (strptime)
            alarm_time = datetime.datetime.strptime(user_input, "%H:%M:%S")
            return alarm_time.strftime("%H:%M:%S")
        except ValueError:
            print("ERROR: Invalid Input - Enter a valid time in the HH:MM:SS format\n")

# Functions
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    sound_file = r"Python\Projects\17_alarmclock\bell.mp3"

    is_running = True
    while (is_running):
        # string format time (strftime)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, end="\r", flush=True)

        if (current_time == alarm_time):
            print("TIMES UP!⏰")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        # The time will update every second
        time.sleep(1)