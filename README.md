rpimonitor stats
================

An LCD to display my RPi and RPi-Monitor

This is a modified version of Xavier Berger's LCD display project. It can be found here: http://rpi-experiences.blogspot.fr/2013/08/a-lcd-display-my-rpi-and-rpi-monitor.html

This version adds a DS18B20 1-WIRE Digital Thermometer (<a href="http://learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf">wiring instructions</a>) to monitor room temperature.

It implements <a href="https://github.com/XavierBerger/RPi-Monitor">RPi-monitor</a> application to gather Raspberry Pi's and room temperature and display it on a screen.

Follow the instrucions provided by Xavier to set up RPi-monitor, install <a href="https://github.com/XavierBerger/pcd8544">pcd8544 library</a>, and run

<code>sudo ./rpimonitor.py</code>
or
<code>sudo python rpimonitor.py</code>
