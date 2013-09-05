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

    # The '28-xxx' in the file name should be changed accordingly to name in your /sys/bus/w1/devices folder.
file = "/sys/bus/w1/devices/28-000004e4b880/w1_slave"

    #Initiate LCD
lcd.init()
        # Turn backlight on/off. The number corrensponds to backlight
        # brightness, 0 being light off, 10 being the brightest.
lcd.backlight(3)
        # Prepare degrees celsius symbol
lcd.define_custom_char([0x00, 0x07, 0x05, 0x07, 0x00])

def get_temp(file):
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

while 1:
    try:
        tempVal = get_temp(file)
            # To adjust number of decimal places, change the '1' in "%.1f" value
        roomtemp = "%.1f" %tempVal
        cputemp = get_soc()
        time = datetime.now().strftime('%H:%M:%S')
            # Go to first line of screen and print current time
        lcd.centre_text(0,time)
            # Go to third screen line and print CPU temperature
        lcd.gotorc(2,0)
        lcd.text("CPU Temp:")
        lcd.gotorc(3,0)
        lcd.text(cputemp)
        lcd.gotorc(3,5)
        lcd.text("\x7fC")
            # Go to fifth screen line and print room temperature
        lcd.gotorc(4,0)
        lcd.text("Room Temp:")
        lcd.gotorc(5,0)
        lcd.text(roomtemp)
        lcd.gotorc(5,5)
        lcd.text("\x7fC")
    except KeyboardInterrupt:
            # If Ctrl+C has been pressed
            # turn off the lcd backlight
        lcd.cls()
        lcd.backlight(0);
            # Exit from the program
        sys.exit(0)
