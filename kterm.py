# kterm 
# ist ein Micropythonscript für ein einfaches Thermometer 
# mit einem M5Stick C und einer K-Meter Unit.
# Über ein Webinterface können Einstellungen vorgenommen werden
# und die Temperatur abgefragt werden.

name = 'kterm.py'
version = '00.01.000'
date = '20.04.2023'
author = 'Peter Stöck'

# TODO:
# Fehlerbehandlung wenn dev_config.json
# nicht geladen werden kann.

# Versionen:
# 00.01.000:
# dev_config.json integriert.
# Wlan integriert.
# Anzeige angepasst.
# y_offset_temperatur eingeführt.
#
# 00.00.005:
# Farbgebung auch für °C implementiert.
# ° 2 Pixel höher gesetzt.
#
# 00.00.004:
# Temperaturanzeige für positive 2 und 3 stellige Zahlen
# positioniert.
#
# 00.00.003:
# Temperaturanzeige formatiert.
# °C erzeugt.
# Temperatur wird als int verarbeitet.
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
import network
from wlansecrets import SSID, PW
import json

temp = '20.0'
diplay_breite = 160
display_hoehe = 80

warn_temperatur = 22
alarm_temperatur = 25

temp_farbe = 0x00ff00

normal_farbe = 0x00ff00
warn_farbe = 0xffff00
alarm_farbe = 0xff0000

x_offset_2stellig = 35
x_offset_3stellig = 10

y_offset_temperatur = 37

lcd.setRotation(3)

setScreenColor(0x404040)
KMeter_0 = unit.get(unit.KMETER, unit.PORTA)


##########################################
# Geräte Definitionen laden.
##########################################
  
try:
    f = open('dev_config.json','r')
    dc = f.read()
    f.close()
    dev_config = json.loads(dc)
except:
    print('dev_config.json konnte nicht geladen werden.')
#    write_log('dev_config.json konnte nicht geholt werden!')
#    abbruch = True


##########################################
# Wlan einrichten und verbinden:
##########################################

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.ifconfig((dev_config['fixIP'], '255.255.255.0', '192.168.5.1', '192.168.5.1'))

wlan.connect(SSID, PW)
time_out = 10
while not wlan.isconnected():
    time.sleep(1)
    time_out -= 1
    if time_out == 0:
        print('Keine Wlan Verbindung!')
        # write_log('Wlan nicht gefunden.')
        # abbruch = True
        break

print('IP: '+ wlan.ifconfig()[0])




# grafische Oberfläche gestalten:

rectangle_title = M5Rect(0, 0, diplay_breite, 28, 0x3366ff, 0x3366ff)
label_prog_name = M5TextBox(2, 2, name + ' V:' + version, lcd.FONT_Default, 0x0, rotate=0)
label_IP = M5TextBox(2, 15, ' IP:' + wlan.ifconfig()[0], lcd.FONT_Default, 0x0, rotate=0)
label_temperatur = M5TextBox(5, y_offset_temperatur, temp, lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label_grad = M5TextBox(90, y_offset_temperatur - 4, 'o', lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label_celsius = M5TextBox(105, y_offset_temperatur, 'C', lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)

lcd.clear()
rectangle_title.show()
label_prog_name.show()
label_IP.show()
    
while True:
    temp = int(KMeter_0.get_kmeter(1))
    if temp > alarm_temperatur:
        temp_farbe = alarm_farbe
    elif temp > warn_temperatur:
        temp_farbe = warn_farbe
    else:
        temp_farbe = normal_farbe
        
    if temp < 100:
        label_temperatur.setPosition(x=x_offset_2stellig)
    else:
        label_temperatur.setPosition(x=x_offset_3stellig)

    label_temperatur.setColor(temp_farbe)
    label_temperatur.setText(str(temp))
    label_temperatur.show()
    
    label_grad.setColor(temp_farbe)
    label_grad.show()
    
    label_celsius.setColor(temp_farbe)
    label_celsius.show()

    wait_ms(300)

