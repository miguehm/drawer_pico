from drawer import Drawer

# ========== Display Libraries ===========
import machine
i2c = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19))
#i2c.scan()

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

# ========= Figures information ==========
import json

# Reading the figures file
with open('figures.json', 'r+') as file: # Open the JSON file
    data = json.load(file) # Saving file to 'data'
    
with open('line.json', 'r+') as file: # Open the JSON file
    data2 = json.load(file) # Saving file to 'data'

with open('cube.json', 'r+') as file:
    data3 = json.load(file)

# User code
rx = 0
ry = 0
rz = 0

fig = Drawer(oled, data) # figures.json
test = Drawer(oled, data2) # line.json

cube = Drawer(oled, data3) # dictionary

amplifier = 15 # Amplifier value

fig.setAmplifier(amplifier) # Set amplifier
cube.setAmplifier(amplifier)

#""" rotation animation
for i in range(181):
    oled.fill(0)
    #fig.rotation("letterM", 2*i, 2*i, 2*i)
    #fig.rotation("hyphen", 2*i, 2*i, 2*i)
    #fig.rotation("letterM2", 2*i, 2*i, 2*i)
    #fig.rotation("x", i, i, i)
    #fig.rotation("y", i, i, i)
    #fig.rotation("z", i, i, i)
    cube.rotation("cube", i*2, i*2, i*2)
    cube.rotation("cube", -i*2, -i*2, -i*2)
    #fig.rotation('x', -2*i, -2*i, -2*i)
    oled.show() # Show the shapes on the Display
#"""

#fig.painter('letterM')
#oled.show()

"""
oled.fill(0)
#fig.rotation("letterM", 0, 0, 0)
fig.rotation('x', 0, 0, 0)
#fig.rotation('x', 0, 0, 30)
#fig.rotation('x', 0, 0, 45)
#fig.rotation('x', 0, 0, 60)
#fig.rotation('x', 0, 0, 90)
oled.show()
"""
