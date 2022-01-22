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

amplifier = 8 # Amplifier value

fig.setAmplifier(amplifier) # Set general scale (I must rename)
cube.setAmplifier(amplifier)

#cube.tam('cube', 1)

#cube.resize('cube', 2, 1, 2) # amplify x, y or z size coordinate of specific figure
#cube.move('cube', 0, 0, 0)
#""" Rotate + Move 
for i in range(181):
    oled.fill(0)
    #"""
    oled.text('Drawer Test', 21, 5)
    oled.text('Rotate + Move', 13, 55)
    
    cube.resize('cube', 2)
    cube.rotate('cube', i*2, i*2, i*2)
    cube.move('cube', 4, 0, 0)
    cube.rotate('cube', 0, 0, i*2)
    cube.draw('cube') # Apply changes
    
    cube.resize('cube', 2)
    cube.rotate('cube', -i*2, -i*2, -i*2)
    cube.move('cube', -4, 0, 0)
    cube.rotate('cube', 0, 0, -i*2)
    cube.draw('cube') # Apply changes
    #"""
    """
    cube.resize('cube', 1)
    cube.rotate('cube', -i*2, -i*2, -i*2)
    cube.move('cube', (i/45), 0, 0)
    cube.draw('cube') # Apply changes
    
    cube.resize('cube', 1)
    cube.rotate('cube', i*2, i*2, i*2)
    cube.move('cube', (-i/45)+2, 0, 0)
    cube.draw('cube') # Apply changes
    """
    
    oled.show() # Show the shapes on the Display
#"""
"""
oled.fill(0)
cube.rotate('cube', 0, 0, 30)
cube.move('cube', 1, 0, 0)
cube.draw('cube') # Apply changes
oled.show()
"""
