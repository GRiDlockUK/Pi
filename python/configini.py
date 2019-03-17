#!/usr/bin/env python

import os
import datetime
import time

def load_ini(configfile):
 import io
 import ConfigParser
 with open(configfile) as f:
    config_data = f.read()
 config = ConfigParser.RawConfigParser(allow_no_value=True)
 config.readfp(io.BytesIO(config_data))
 return config

config = load_ini("configini.ini")
status_flag = False

while True:
 now = datetime.datetime.now()
 todayAM = now.replace(hour=(config.getint('time', 'am')), minute=0, second=0, microsecond=0)
 todayPM = now.replace(hour=(config.getint('time', 'pm')), minute=0, second=0, microsecond=0)

 #print(now)
 
 # do something once per hour
 if now.minute == 00 and now.second == 00:
  print("reloading the ini file")
  config = load_ini("configini.ini")
 
 # do something once every minute
 if now.second == 10:
  print("checking for status file")
  if os.path.isfile('status.txt'):
   status_flag = True
   print("show status file contents")
  else: 
   status_flag = False
   
 # actions to run in daytime
 if now > todayAM and now < todayPM and status_flag == False:
  print("stats update")

 time.sleep(1)

