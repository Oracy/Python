from time import time
# from datetime import datetime, timedelta
import datetime

year = 2022
month = 2
day = 2
hour = 8
minutes = 30
seconds = 0

cicle_to_wakeup = datetime.timedelta(minutes=90)
to_wakeup = datetime.datetime(year, month, day, hour, minutes, seconds)
date = to_wakeup - cicle_to_wakeup * 10

for cicle in range(0, 6):
    date = to_wakeup - cicle_to_wakeup * cicle
    to_wakeup_str = to_wakeup.strftime('%Y-%m-%d %H:%M:%S.%f')[11:-7]
    if date != to_wakeup:
        print(f"Dormir as: {date.strftime('%Y-%m-%d %H:%M:%S.%f')[11:-7]}, para acordar as: {to_wakeup_str}, sono total de: {to_wakeup - date}")