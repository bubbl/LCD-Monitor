#!/usr/bin/env python
import httplib, time, os, sys, json
import pcd8544.lcd as lcd

# class Process dedicated to process data get from Client
# and send information to LCD and console
class Process:
  # Process constructor
  def __init__(self):
    # Initialize LCD
    lcd.init()
    # Turn the backlight on/off and adjust it
    lcd.backlight(0)

  def run(self, jsonString):
    # Parse data as json
    data = json.loads( jsonString )
    text1 = "RPi-Monitor"
    lcd.define_custom_char([0x00, 0x07, 0x05, 0x07, 0x00])
    # Try to get data from json or return default value 
    try:
      rpi_temperature = data['soc_temp']
    except:
      rpi_temperature="--.--"
    try:
      room_temp = data['living_room_temp']
    except:
      room_temp="--.--"
    # Construct string to be displayed on screens
    rpitemp = "%s" %rpi_temperature
    roomtemp = "%s" %room_temp
    lcd.centre_text(0, text1)
    lcd.gotorc(1,0)
    lcd.text("RPi Temp:")
    lcd.gotorc(2,0)
    lcd.text(rpitemp)
    lcd.gotorc(2,8)
    lcd.text("\x7fC")
    lcd.gotorc(4,0)
    lcd.text("Room Temp:")
    lcd.gotorc(5,0)
    lcd.text(roomtemp)
    lcd.gotorc(5,8)
    lcd.text("\x7fC")

# Class client design to work as web client and get information 
# from RPi-Monitor embedded web server
class Client:
  # Client constructor
  def __init__(self):
    # Create a Process object
    self.process = Process()

  def run(self):
    # Infinite loop
    while True:
     try:
       # Initiate a connection to RPi-Monitor embedded server
       connection = httplib.HTTPConnection("localhost", 8889)
       # Get the file dynamic.json
       connection.request("GET","/dynamic.json")
       # Get the server response
       response = connection.getresponse()
       if ( response.status == 200 ):
         # If response is OK, read data
         data = response.read()
         # Run process object on extracted data
         self.process.run(data)
       # Close the connection to RPi-Monitor embedded server
       connection.close()
     finally:
       # Wait x seconds before restarting the loop
       time.sleep(3)

# Main function
def main():
  try:
    # Create a Client object
    client = Client()
    # Run it
    client.run()
  except KeyboardInterrupt:
    # if Ctrl+C has been pressed
    # turn off the lcd backlight
    lcd.backlight(0); 
    lcd.cls()
    # exit from the program 
    sys.exit(0)

# Execute main if the script is directly called
if __name__ == "__main__":
    main()
