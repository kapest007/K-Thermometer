# mk_dev_config.py

from m5stack import *
from m5ui import *
from uiflow import *
import json

dev_config = {'fixIP' : '192.168.5.192',
              'dev_name' : 'K-Term_01',
              'dev_typ' : 'M5StickC + K-Meter',
              '' : '',
          } 
        

print(dev_config)

json_dev_config = json.dumps(dev_config)

print(json_dev_config)

f = open('dev_config.json', 'w')
f.write(json_dev_config)
f.close()