from drawer import Drawer, rotation

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

# User code

rx = 0
ry = 0
rz = 0

fig = Drawer(oled, data)
test = Drawer(oled, data2)

amplifier = 9

fig.setAmplifier(amplifier)

for i in range(180):
    oled.fill(0)
    fig.rotation("letterM", i, i, i)
    fig.rotation("hyphen", i, i, i)
    fig.rotation("letterM2", i, i, i)
    #fig.rotation("x", i, i, i)
    #fig.rotation("y", i, i, i)
    #fig.rotation("z", i, i, i)
    #fig.rotation("cube", 0, 0, i)
    test.rotation('x', -i, -i, -i)
    oled.show() # Show the shapes on the Display

