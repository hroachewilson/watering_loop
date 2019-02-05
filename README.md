# watering_loop

This is a simple program that will print out a placeholder statement for turning a relay on / off during a 24 hour watering cycle.

The program will wait until the specified start time and then enter a watering loop, keeping a valve open for a given watering duration (for instance 20 seconds), repeating at a given watering interval (for instance 4 hours, 15 minutes).

`water_me.py -h`


```
Usage: water_me.py [-h] start_time %s watering_duration %s watering_interval %s

Watering timer code. Takes user input args and prints events to stdout

positional arguments:
  start_time %s         start time in HHMM format with leading zeroes
  watering_duration %s  watering duration in seconds
  watering_interval %s  watering interval in HHMM format with leading zeroes

optional arguments:
  -h, --help            show this help message and exit
```
