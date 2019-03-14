import time
import datetime

import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"


now = datetime.datetime.now()
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
today11pm = now.replace(hour=23, minute=00, second=0, microsecond=0)

while True:
 now = datetime.datetime.now()
 print "blackout the screen"

 if now > today8am and now < today11pm:
  print now.strftime("%Y-%m-%d %H:%M:%S")

 else:
  print "sleeping"
  time.sleep(60)  

 time.sleep(2)


