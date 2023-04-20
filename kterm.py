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
# 00.00.002:
# Grafische Oberfläche gestaltet.
#
# 00.00.001:
# Zugriff auf K-Meter implementiert.

from m5imports import *
import unit

temp = '20.0'
diplay_breite = 160
display_hoehe = 80

temp_farbe = 0x00ff00

normal_farbe = 0x00ff00
warn_farbe = 0xffff00
alarm_farbe = 0xff0000

lcd.setRotation(3)

setScreenColor(0x404040)
KMeter_0 = unit.get(unit.KMETER, unit.PORTA)

# grafische Oberfläche gestalten:

rectangle_title = M5Rect(0, 0, diplay_breite, 20, 0x3366ff, 0x3366ff)
label_Prog_name = M5TextBox(2, 2, name + ' V:' + version, lcd.FONT_Default, 0x0, rotate=0)
label_Temperatur = M5TextBox(5, 30, temp, lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

lcd.clear()
rectangle_title.show()
label_Prog_name.show()
    
while True:
    temp = KMeter_0.get_kmeter(1)
    if temp > 25:
        temp_farbe = alarm_farbe
    elif temp > 22:
        temp_farbe = warn_farbe
    else:
        temp_farbe = normal_farbe
#    addr = hex(KMeter_0.rw_i2c_address())
#    ver = str(KMeter_0.get_firmware_version())
    label_Temperatur.setColor(temp_farbe)
    label_Temperatur.setText(str(temp))
    label_Temperatur.show()
#    lcd.clear()
#    label_Prog_name.show()
#    lcd.print('Version: ' + version, 5, 5, 0xffffff)
#    lcd.print('I2C Adr: ' + addr, 5, 25, 0xffffff)
#    lcd.print('Temp: ' + temp, 5, 50, 0xffffff)
    wait_ms(300)

