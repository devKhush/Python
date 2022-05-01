import time
# https://www.geeksforgeeks.org/python-time-module/

# epoch time
epochTimeInSeconds = time.time()
print(epochTimeInSeconds, '\n')

localTime = time.localtime(epochTimeInSeconds)
print(localTime)
print("Year: ", localTime.tm_year)
print("Month: ", localTime.tm_mon)
print("Day: ", localTime.tm_mday)
print("Hour: ", localTime.tm_hour)
print("Minute: ", localTime.tm_min)
print("Seconds: ", localTime.tm_sec)
print()

currTime = time.ctime(epochTimeInSeconds)
print(currTime)


time.sleep(2)
print('Done')
