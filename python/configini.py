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

while True:
 now = datetime.datetime.now()
 todayAM = now.replace(hour=(config.getint('time', 'am')), minute=0, second=0, microsecond=0)
 todayPM = now.replace(hour=(config.getint('time', 'pm')), minute=0, second=0, microsecond=0)

 # actions to run in daytime
 if now > todayAM and now < todayPM:
  print(todayAM)

 time.sleep(5)
 os.path.isfile('.configini.ini') 
 f = open("configini.ini", "r")
 print(f.readline())

