# Dates and Times
import datetime

# Runs the main program
def main():
    date = datetime.date(2026, 9, 12)
    print(date)     # 2026-09-12

    today = datetime.date.today()
    print(today)    # 2026-09-11

    time = datetime.time(12, 30, 0)
    print(time)     # 12:30:00

    now = datetime.datetime.now()
    print(now)      # 2026-09-11 23:11:50.406569

    now_f = now.strftime("%H:%M:%S %m/%d/%Y")
    print(now_f)    # 23:23:34 09/11/2026

    target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
    current_datetime = datetime.datetime.now()

    if (target_datetime < current_datetime):
        print(f"We have passed target date of {target_datetime}")
        # We have not passed target date of 2030-01-02 12:30:01
    elif (target_datetime == current_datetime):
        print(f"Today is {target_datetime}")
    else:
        print(f"We have not passed target date of {target_datetime}")

if __name__ == "__main__":
    main()