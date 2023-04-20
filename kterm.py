# kterm 
# ist ein Micropythonscript für ein einfaches Thermometer 
# mit einem M5Stick C und einer K-Meter Unit.

name = 'kterm.py'
version = '00.00.001'
date = '20.04.2023'
author = 'Peter Stöck'

# TODO:
# 

# Versionen:
# 00.00.001:
# Zugriff auf K-Meter implementiert.

from m5imports import *
import unit

lcd.setRotation(3)

setScreenColor(0x111111)
KMeter_0 = unit.get(unit.KMETER, unit.PORTA)

while True:
    temp = str(KMeter_0.get_kmeter(1))
    addr = hex(KMeter_0.rw_i2c_address())
    ver = str(KMeter_0.get_firmware_version())
    lcd.clear()
    lcd.print('Version: ' + version, 5, 5, 0xffffff)
    lcd.print('I2C Adr: ' + addr, 5, 25, 0xffffff)
    lcd.print('Temp: ' + temp, 5, 50, 0xffffff)
    wait_ms(300)

