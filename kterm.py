# kterm 
# ist ein Micropythonscript für ein einfaches Thermometer 
# mit einem M5Stick C und einer K-Meter Unit.

name = 'kterm.py'
version = '00.00.002'
date = '20.04.2023'
author = 'Peter Stöck'

# TODO:
# 

# Versionen:
# 00.00.003:
# Temperaturanzeige formatiert.
#
# 00.00.002:
# Grafische Oberfläche gestaltet.
# Grundlegende Darstellung und
# Farbsignalisierung implementiert.
#
# 00.00.001:
# Zugriff auf K-Meter implementiert.

from m5imports import *
import unit

temp = '20.0'
diplay_breite = 160
display_hoehe = 80

warn_temperatur = 22
alarm_temperatur = 25

temp_farbe = 0x00ff00

normal_farbe = 0x00ff00
warn_farbe = 0xffff00
alarm_farbe = 0xff0000

lcd.setRotation(3)

setScreenColor(0x404040)
KMeter_0 = unit.get(unit.KMETER, unit.PORTA)

# grafische Oberfläche gestalten:

rectangle_title = M5Rect(0, 0, diplay_breite, 20, 0x3366ff, 0x3366ff)
label_prog_name = M5TextBox(2, 2, name + ' V:' + version, lcd.FONT_Default, 0x0, rotate=0)
label_temperatur = M5TextBox(5, 30, temp, lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label_grad = M5TextBox(90, 28, 'o', lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label_celsius = M5TextBox(105, 30, 'C', lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

lcd.clear()
rectangle_title.show()
label_prog_name.show()
    
while True:
    temp = int(KMeter_0.get_kmeter(1))
    if temp > alarm_temperatur:
        temp_farbe = alarm_farbe
    elif temp > warn_temperatur:
        temp_farbe = warn_farbe
    else:
        temp_farbe = normal_farbe

    label_temperatur.setColor(temp_farbe)
    label_temperatur.setText(str(temp))
    label_temperatur.show()
    
    label_grad.show()
    
    label_celsius.show()

    wait_ms(300)

