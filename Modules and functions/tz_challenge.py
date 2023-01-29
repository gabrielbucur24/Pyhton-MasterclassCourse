# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in format suitable for the
# user of your program to understand and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

timezones = {1: 'Europe/Bucharest',
             2: 'Europe/Stockholm',
             3: 'Indian/Christmas',
             4: 'Pacific/Fiji',
             5: 'US/Alaska',
             6: 'US/Hawaii',
             }

# print(pytz.common_timezones)

while True:
    for key in timezones:
        print(f"\t{key}: {timezones[key]}")
    choice = int(input("Enter the number of a timezone from the list: "))
    # print(timezones[choice])
    if choice == 0:
        print("Exiting...")
        break
    elif choice not in timezones:
        print("ERROR, better try again")
        continue
    else:
        tz_to_display = pytz.timezone(timezones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("-" * 80)
        print("In the timezone {} the time is {} {}".format(timezones[choice], world_time.strftime('%A %x %X %z'),
                                                            world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print("-" * 80)
