# M7_GPIO
A Python GPIO library for the M7 single-board computer ([RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/) clone).

## Python Libraries and Scripts

**M7_GPIO**<br>
A re-implementation of the RPi.GPIO library for the NOVASOM M7. Currently under development.<br>
See Docs folder for the documentation.

**M7-GPIO-test.py**<br>
A simple test script. Outputs a list of internal vars, sets the GPIO mode to "BOARD", sets up a GPIO output (blinks an LED if connected to pin 16), sets up a GPIO input (pulls-up and reports the state of pin 18), then cleans up all GPIO exports and exits.

## Library Installation and Usage:
**Importing M7.GPIO**<br>
Below is the reccomended method for importing this library into your project.
1. Download the entire "M7" folder from the repo.
1. Place the "M7" folder in the same directory as the Python script you're working with.
1. Within your script, substitute the traditional "`import RPi.GPIO as GPIO`" line for "`import M7.GPIO as GPIO`".

Once imported, syntax for implemented functions should be identical to RPi.GPIO.

# Test Platform

All testing of this library is done on a Novasom M7 board (2GB model) running Armbian.

Compatibility with other versions of Linux running on the Novasom M7 is not guaranteed.

# Resources
List of resources and reference material used while building the scripts and libraries in this repository
* [Sourceforge - RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/)
* [Kernel.org - GPIO/SYSFS Documentation](https://www.kernel.org/doc/Documentation/gpio/sysfs.txt)
* [Novasom Page ](http://www.novasomindustries.com)

# Credits
Developed by Pier Francesco Maria Santi aka PFM ([Send a mail to PFM]pfm.santi@hexcape.com [View PFM linkedin profile]https://www.linkedin.com/in/pierfrancescomariasanti/)
