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
with open('cube.json', 'r+') as file:
    data3 = json.load(file)

# User code
rx = 0
ry = 0
rz = 0

cube = Drawer(oled, data3) # dictionary

amplifier = 12 # Amplifier value # Change 'amplifier' name for 'scale'

#fig.setAmplifier(amplifier) # Set general scale (I must rename)
cube.setAmplifier(amplifier)

# Rotation Test

def testRotateX():
    for i in range(90):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate X-axis', 13, 55)
        cube.rotate('cube', i*2, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()

def testRotateY():
    for i in range(90):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate Y-axis', 13, 55)
        cube.rotate('cube', 180, i*2, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
def testRotateZ():
    for i in range(90):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate Z-axis', 13, 55)
        cube.rotate('cube', 180, 180, i*2)
        cube.draw('cube') # Apply changes
        oled.show()
        
def testRotateXYZ():
    for i in range(91):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate XYZ axes', 5, 55)
        cube.rotate('cube', i*4, i*4, i*4)
        cube.draw('cube') # Apply changes
        oled.show()
        
def testRotateAndMove():
    for i in range(91):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate + Move', 13, 55)
        cube.rotate('cube', i*4, i*4, i*4)
        cube.move('cube', i/30, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(91):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate + Move', 13, 55)
        cube.rotate('cube', i*4, i*4, i*4)
        cube.move('cube', 3-i/30, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(91):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate + Move', 13, 55)
        cube.rotate('cube', i*4, i*4, i*4)
        cube.move('cube', -i/30, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(91):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate + Move', 13, 55)
        cube.rotate('cube', i*4, i*4, i*4)
        cube.move('cube', -3+i/60, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()
    
def testMoveAndRotate():
    for i in range(181):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Move + Rotate', 13, 55)
        cube.rotate('cube', i*2, i*2, i*2)
        cube.move('cube', -1.5, 0, 0)
        cube.rotate('cube', 0, 0, i*2)
        
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(91):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Move + Rotate', 13, 55)
        cube.rotate('cube', i*2, i*2, i*2)
        cube.move('cube', -1.5+i/60, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
def testResize():
    for i in range(15):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Move + Rotate', 13, 55)
        cube.rotate('cube', i*2, 0, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Move + Rotate', 13, 55)
        cube.rotate('cube', 30, i*2, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Resize X', 30, 55)
        cube.resize('cube', (i/10)+1, 1, 1)
        cube.rotate('cube', 30, 30, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Resize X', 30, 55)
        cube.resize('cube', 3-(i/10), 1, 1)
        cube.rotate('cube', 30, 30, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Resize Y', 30, 55)
        cube.resize('cube', 1, (i/10)+1, 1)
        cube.rotate('cube', 30, 30, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Resize Y', 30, 55)
        cube.resize('cube', 1, 3-(i/10), 1)
        cube.rotate('cube', 30, 30, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Resize Z', 30, 55)
        cube.resize('cube', 1, 1, (i/10)+1)
        cube.rotate('cube', 30, 30, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    for i in range(20):
        oled.fill(0)
        oled.text('Drawer Test', 21, 5)
        oled.text('Resize Z', 30, 55)
        cube.resize('cube', 1, 1, 3-(i/10))
        cube.rotate('cube', 30, 30, 0)
        cube.draw('cube') # Apply changes
        oled.show()
        
    
        
def run():
    testRotateX()
    testRotateY()
    testRotateZ()
    testRotateXYZ()
    testRotateAndMove()
    testMoveAndRotate()
    testResize()

def rotateAndMove():
    #""" Rotate + Move 
    for i in range(181):
        oled.fill(0)
        #"""
        oled.text('Drawer Test', 21, 5)
        oled.text('Rotate + Move', 13, 55)
        
        cube.resize('cube', 1, 2, 3)
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

if __name__ == '__main__':
    run()
