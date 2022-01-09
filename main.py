# from time import sleep

# ========== Display Libraries ===========
import machine
i2c = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19))
i2c.scan()

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

# ========= Figures information ==========
import json
from math import sin, cos, pi #, ceil, floor

# Reading the figures file
with open('figures.json', 'r+') as file: # Open the JSON file
    data = json.load(file) # Saving file to 'data'

# My program
# ====== Matrices of Transformation ======
# >>>>>>>>>>> Rotation Matrix >>>>>>>>>>>>

def rotation(name, alpha, beta, theta):
    try:
        # Debuging
        # Showing name
        #if(data['shapes'][name]):
            #print(f'> Name: {name}')
        
        RAD = pi/180 # 3.141/180 # Radian value
        
        # high values may cause flickering -- May I'll create a transformation matrix of amplifier...?
        # only integers!
        amplifier = 6

        # Angles in gradians
        """
        alpha: respect to the 'x' axis
        beta: respect to the 'y' axis
        theta: respect to the 'z' axis
        """

        # Auxiliaries variables
        coord1 = [None, None]
        coord2 = [None, None]
        
        # Getting the Sine and Cosine values of the angles (alpha, beta, theta)
        presicion = 100 # Number of decimals for sine and cosine
        s_alpha = int(sin(alpha*RAD)*presicion)/presicion
        c_alpha = int(cos(alpha*RAD)*presicion)/presicion
        
        s_beta = int(sin(beta*RAD)*presicion)/presicion
        c_beta = int(cos(beta*RAD)*presicion)/presicion
        
        s_theta = int(sin(theta*RAD)*presicion)/presicion
        c_theta = int(cos(theta*RAD)*presicion)/presicion
        
        # Set lines on Display Oled process
        for j in range(len(data['shapes'][name]['coordinates'])/3): # divide to 3 'cause the coordinates has three values (x,y,z)
            x = data['shapes'][name]['coordinates'][j*3]
            y = data['shapes'][name]['coordinates'][j*3+1]
            z = data['shapes'][name]['coordinates'][j*3+2]
            
            # Transformation Matrix
            rx = ((x*c_theta*c_beta)+y*(-s_theta*c_alpha+c_theta*s_beta*s_alpha)+z*(s_theta*s_alpha+c_theta*s_beta*c_alpha))*amplifier
            ry = ((x*s_theta*c_beta)+y*(c_theta*c_alpha+s_theta*s_beta*s_alpha)+z*(-c_theta*s_alpha+s_theta*s_beta*c_alpha))*amplifier
            
            # Prepare the coordinates to line function
            # 60: oled width / 2
            # 30: oled height / 2
            if(j != 0):
                coord2 = [int(rx)+60, -(int(ry))+30]
            else:
                coord1 = [int(rx)+60, -(int(ry))+30]
                
            if(coord2[0]):
                """
                # Debuging
                # Getting values for each shape
                print(f'rx1: {coord1[0]}, ry1: {coord1[1]}')
                print(f'rx2: {coord2[0]}, ry2: {coord2[1]}')
                print('================')
                """
                # Creating line
                oled.line(coord1[0], coord1[1], coord2[0], coord2[1], 1)
                
                # Restarting the auxiliaries variables
                coord1 = coord2
                coord2 = [None, None]
        
        # Debuging
        #print('\n')
        
    except:
        print(f'The shape \"{name}\" does not exist!')
        
# User code

rx = 0
ry = 0
rz = 0

for i in range(360):
    oled.fill(0)
    rotation("letterM", i, i, i)
    rotation("hyphen", i, i, i)
    rotation("letterM2", i, i, i)
    rotation("x", i, i, i)
    rotation("y", i, i, i)
    rotation("z", i, i, i)
    rotation("cube", 0, 0, i)
    oled.show() # Show the shapes on the Display
    #sleep(0.1)
