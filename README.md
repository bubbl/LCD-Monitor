LCD-Monitor
================

    Author: Bartlomiej Bania
    Webpage: http://www.bartbania.com/
    Project Webpage: https://github.com/bubbl/LCD-Monitor/

![alt tag](https://raw.github.com/bubbl/LCD-Monitor/master/doc/humble-pi.jpg)

PARTS USED:
===========

    - Nokia 5110 LCD screen with PCD8544 driver
    - DS18B20 1-WIRE Digital Thermometer
    - 1x 4.7k ohm resistor for thermometer
    - wires / jumper cables
    - Humble Pi / breadboard

![alt tag](https://raw.github.com/bubbl/LCD-Monitor/master/doc/humble-pi_wiring.jpg)

HARDWARE SETUP:
===============

    The PCD8544 and Digital Thermometer can be installed on the breadboard 
    as shown here: 
    
![alt tag](https://raw.github.com/bubbl/LCD-Monitor/master/doc/rpimonitor_bb.png)
    
        Note: If you want to reproduce this assembly, check carefully the 
        pin order, it may be different, as the PCD8455 board pinning differs 
        from model to model.
    
    DS18B20 1-WIRE Digital Thermometer Setup:
    http://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/

INSTALLATION:
=============

        git clone https://github.com/bubbl/LCD-Monitor.git
        cd /path/to/your/LCD-Monitor

RUN:
====

    1) use with RPi-Monitor installed (http://rpi-experiences.blogspot.fr/):
        sudo python rpimonitor.py
    2) use as a self-dependent application:
        sudo python lcdmonitor.py
    * To run the app in background, add & after the command
    
DEMO:
=====

http://youtu.be/6T7H8-_5dsA


RUN AT STARTUP (TESTING!):
===============

    Copy init script to init directory:
        sudo cp lcdtempr /etc/init.d/
    Make script exetutable: 
        sudo chmod +x /etc/init.d/lcdtempr
    Make the lcdtempr init script known to the system by using the update-rc.d command:
        sudo update-rc.d lcdtempr defaults
