#!/usr/bin/python
import time
import argparse
from datetime import datetime


def main(start_time_hour, start_time_minute, watering_duration, watering_interval_hour, watering_interval_minute):

    # This should loop once every 24 hours
    while True:

        # Sleep until start time is reached
        current_time = datetime.now()
        while current_time.hour < start_time_hour:              # This loop will only break after start hour is reached,
            time.sleep(1)                                       # at which point it will only pass for remainder of 24h
            current_time = datetime.now()
            while current_time.minute <= start_time_minute:     # This loop will only break after start minute is reached,
                time.sleep(1)                                   # at which point the watering routine will execute for
                current_time = datetime.now()                   # the remainder of the 24 hour period

        # Commence watering loop
        print("call function to turn sprinkler valve relay ON here")
        time.sleep(watering_duration)
        print("call function to turn sprinkler valve relay OFF here")
        time.sleep(watering_interval_hour * 3600 + watering_interval_minute * 60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Watering timer code. Takes user input args and prints events to stdout")
    parser.add_argument('start_time', metavar='start_time %s', help='start time in HHMM format')
    parser.add_argument('watering_duration', metavar='watering_duration %s', help='watering duration in seconds')
    parser.add_argument('watering_interval', metavar='watering_interval %s', help='watering interval in HHMM format')
    args = parser.parse_args()

    main(int(args.start_time[0:2]), int(args.start_time[2:4]), int(args.watering_duration),
         int(args.watering_interval[0:2]), int(args.watering_interval[2:4]))
