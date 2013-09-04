rpimonitor stats
================

    Author: Bartlomiej Bania
    Webpage: http://www.bartbania.com/
    Project Webpage: https://github.com/bubbl/rpimonitor_stats/

PARTS USED:
===========

    - Nokia 5110 LCD screen
    - DS18B20 1-WIRE Digital Thermometer
    - 6 x 10k ohm resistors
    - 1x 1k ohm resistor
    - jumper cables
    - breadboard

HARDWARE SETUP:
===============

    The PCD8544 and Digital Thermometer can be installed on the breadboard 
    as shown here: http://www.bartbania.com/wp-content/uploads/2013/09/rpimonitor_bb.png
    
        Note: If you want to reproduce this assembly, check carefully the 
        pin order, it may be different, as the PCD8455 board pinning differs 
        from model to model.
    
    DS18B20 1-WIRE Digital Thermometer Setup:
    http://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/

INSTALLATION:
=============

        git clone https://github.com/bubbl/rpimonitor_stats.git
        cd /path/to/your/rpimonitor_stats

RUN:
====

    1) use with RPi-Monitor installed (http://rpi-experiences.blogspot.fr/):
        sudo python rpimonitor.py
    2) use as a self-dependent application:
        sudo python tempmonitor.py
    * To run the app in background, add & (Shift + 7) after the command

RUN AT STARTUP:
===============

    Copy init script to init directory:
        sudo cp lcdtempr /etc/init.d/
    Make script exetutable: 
        sudo chmod +x /etc/init.d/lcdtempr
    Make the lcdtempr init script known to the system by using the update-rc.d command:
        sudo update-rc.d lcdtempr defaults
