import time
import datetime
import subprocess

while True:
 now = datetime.datetime.now()
 todayAM = now.replace(hour=7, minute=0, second=0, microsecond=0)
 todayPM = now.replace(hour=23, minute=0, second=0, microsecond=0)

 if now > todayAM and now < todayPM:

   # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
   cmd = "hostname -I | cut -d\' \' -f1"
   IP = subprocess.check_output(cmd, shell = True )
   cmd = "top -bn1 | grep 'load average' | awk '{printf \"CPU: %.2f%\", $(NF-2)}'"
   CPU = subprocess.check_output(cmd, shell = True )
   cmd = "free -m | awk 'NR==2{printf \"MEM: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
   MEM = subprocess.check_output(cmd, shell = True )
   cmd = "df -h | awk '$NF==\"/\"{printf \"SD : %d/%dGB %s\", $3,$2,$5}'"
   DSK = subprocess.check_output(cmd, shell = True )

   # Write lines
   print("<"+str(IP)+">")
   print("<"+str(CPU)+">")
   print("<"+str(MEM)+">")
   print("<"+str(DSK)+">")

 time.sleep(5)


