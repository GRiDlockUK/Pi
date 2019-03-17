#!/usr/bin/env python

import time
import datetime
import subprocess

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def load_ini(configfile):
 import io
 import ConfigParser
 with open(configfile) as f:
  config_data = f.read()
 config = ConfigParser.RawConfigParser(allow_no_value=True)
 config.readfp(io.BytesIO(config_data))
 return config

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Initialize library.
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

config = load_ini("/share/Git/Pi/python/stats2.ini")

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('/share/Fonts/Minecraftia.ttf', 8)
#font = ImageFont.truetype(config.getint('other', 'font'), 8)

page = 0

while True:
 now = datetime.datetime.now()

 # Draw a black filled box to clear the image.
 draw.rectangle((0,0,width,height), outline=0, fill=0)
 
 # do something once per minute
 #if now.second == 00:
 # draw.text((x, top), str(now.strftime("%Y-%m-%d %H:%M:%S")), font=font, fill=255)
 # time.sleep(3)
 
 # do something once per hour
 if now.minute == 00 and now.second == 00:
  config = load_ini("/share/Git/Pi/python/stats2.ini")
  time.sleep(1)
 
 todayAM = now.replace(hour=(config.getint('time', 'am')), minute=0, second=0, microsecond=0)
 todayPM = now.replace(hour=(config.getint('time', 'pm')), minute=0, second=0, microsecond=0)
 
 if now > todayAM and now < todayPM:
 
   cmd = "hostname -I | cut -d\' \' -f1"
   IP = subprocess.check_output(cmd, shell = True )
   cmd = "top -bn1 | grep 'load average' | awk '{printf \"CPU: %.2f%\", $(NF-2)}'"
   CPU = subprocess.check_output(cmd, shell = True )
   cmd = "free -m | awk 'NR==2{printf \"MEM: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
   MEM = subprocess.check_output(cmd, shell = True )
   cmd = "df -h | awk '$NF==\"/\"{printf \"SD : %d/%dGB %s\", $3,$2,$5}'"
   DSK = subprocess.check_output(cmd, shell = True )

   # Write lines
   if page == 0:
    draw.text((x, top),       "IP : " + str(IP),  font=font, fill=255)
    page = 1
   else:
    draw.text((x, top),       "IP.: " + str(IP),  font=font, fill=255)   
    page = 0

   draw.text((x, top+8),     str(CPU),  font=font, fill=255)
   draw.text((x, top+16),    str(MEM),  font=font, fill=255)
   draw.text((x, top+25),    str(DSK),  font=font, fill=255)
   
 # Display image.
 disp.image(image)
 disp.display()
 time.sleep(.5)



