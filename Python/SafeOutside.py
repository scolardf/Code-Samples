import datetime

now = datetime.datetime.now()
currentTime = now.strftime("%H:%M")
if (now.hour >= 8 and now.hour < 20):
    print ("It's ", currentTime,"so it's daytime! Nothing bad happens during the day! Go outside!")
else:
    print ("It's ",currentTime,", which means that every murderer ever is currently lurking outside. Don't leave. It's scary out there.")
