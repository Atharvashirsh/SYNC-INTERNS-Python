import datetime
import time
import winsound

print("*"*100)
print("\n\t\tAlarm Clock\n")
print("*"*100)

sethour = input("Enter hour :")
setminute = input("Enter minute :")
setsecond = input("Enter second :")
settime = sethour + ":" + setminute + ":" + setsecond

while True:
    if datetime.datetime.now().strftime("%H:%M:%S") == settime:
        print("\nAlarm Buzzing !!!\n")
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
        time.sleep(10)
        break
