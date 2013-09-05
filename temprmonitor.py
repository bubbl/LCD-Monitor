''' Author: Bartlomiej Bania
    Webpage: http://www.bartbania.com/
    Project Webpage: https://github.com/bubbl/rpimonitor_stats/

    PARTS USED:
    - Nokia 5110 LCD screen
    - DS18B20 1-WIRE Digital Thermometer
    - 6 x 10k ohm resistors
    - 1x 1k ohm resistor
    - jumper cables
    - breadboard

    HARDWARE SETUP:
    The PCD8544 and Digital Thermometer can be installed on the breadboard 
    as shown here: http://www.bartbania.com/wp-content/uploads/2013/09/rpimonitor_bb.png
    
        Note: If you want to reproduce this assembly, check carefully the
        pin order, it may be different, as the PCD8455 board pinning differs
        from model to model.
    
    DS18B20 1-WIRE Digital Thermometer Setup:
    http://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/

    INSTALLATION:
        git clone https://github.com/bubbl/rpimonitor_stats.git
        cd /path/to/your/rpimonitor_stats

    RUN:
    1) use with RPi-Monitor installed (http://rpi-experiences.blogspot.fr/):
        sudo python rpimonitor.py
    2) use as a self-dependent application:
        sudo python tempmonitor.py
    * To run the app in background, add & (Shift + 7) after the command
'''
# Application starts here

#!/usr/bin/python
import pcd8544.lcd as lcd
import time, sys ,os, subprocess
from datetime import datetime

    # optional load of drivers if not listed in /etc/modules
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

lcd.init()
            # Turn backlight on/off. The number corrensponds to backlight
            # brightness, 0 being light off, 10 being the brightest.
lcd.backlight(1)
lcd.set_contrast(512)
            # Prepare degrees celsius symbol
lcd.define_custom_char([0x00, 0x07, 0x05, 0x07, 0x00])

class Process:
    def run(self):

        def get_temp(file):
                # The '28-xxx' in the file name should be changed accordingly 
                # to name in your /sys/bus/w1/devices folder.
            file = "/sys/bus/w1/devices/28-000004e4b880/w1_slave"
                # Open file written to by temp sensor
            tfile = open(file)
                # Read all text in file
            text = tfile.read()
                # Close file once text is read
            tfile.close()
                # Pull out the temperature value
            temprdata = text.split("\n")[1].split(" ")[9]
                # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
            temperature = float(temprdata[2:])
                # Put the decimal point in the right place and display it.
            temperature = temperature / 1000
            return(temperature)
        
        def get_soc():
                # Read CPU temperature and extract the numbers only
            res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
            return(res.replace("temp=","").replace("'C",""))

        try:
            rmtemp = get_temp(file)
        except:
            rmtemp = "--.-"
        try:
            rpitemp = get_soc()
        except:
            rpitemp = "--.-"

        roomtemp = "%s" %rmtemp
        cputemp = "%s" %rpitemp
        tm = datetime.now().strftime('%H:%M')
        tm2 = datetime.today().strftime('%d %b %Y')
        lcd.centre_text(0,"Today is:")
            # Go to second line of screen and print current time and date
        lcd.centre_text(1,tm2)
        lcd.centre_text(2,tm)
            # Go to fifth screen line and print room/CPU temperature
        lcd.centre_text(4,"--Room | RPi--")
        lcd.gotorc(5,0)
        lcd.text(roomtemp)
        lcd.gotorc(5,4)
        lcd.text("\x7fC")
        lcd.gotorc(5,8)
        lcd.text(cputemp)
        lcd.gotorc(5,12)
        lcd.text("\x7fC")

class Client:
    def __init__(self):
        self.process = Process()
    def run(self):
        while True:
            try:
                client = Process()
                client.run()
            finally:
                    # Refresh every x seconds
                time.sleep(5)

def main():
  while 1:
    try:
      client = Client()
      client.run()
    except KeyboardInterrupt:
            # If Ctrl+C has been pressed
            # turn off the lcd backlight
        lcd.cls()
        lcd.backlight(0);
            # Exit from the program
        sys.exit(0)

if __name__=="__main__":
    main()
