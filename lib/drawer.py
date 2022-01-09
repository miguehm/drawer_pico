"""
The Drawer - A rendering of 3D figures simulator for Raspberry Pi Pico
A dvorak-hdz-mor's project

Check my github repository for updates
> https://github.com/dvorak-hdez-mor/drawer_pico

Check the tutorials on my YT's channel
> https:// 

"""

# ====== Matrices of Transformation ======
# >>>>>>>>>>> Rotation Matrix >>>>>>>>>>>>

def rotation(oled, data, name, alpha, beta, theta, amplifier):
    from math import sin, cos, pi
    # Debuging
    # Showing name
    #if(data['shapes'][name]):
        #print(f'> Name: {name}')
    
    RAD = pi/180 # 3.141/180 # Radian value

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
            oled.line(coord1[0], coord1[1], coord2[0], coord2[1], 1) # Check for white screens
            
            # Restarting the auxiliaries variables
            coord1 = coord2
            coord2 = [None, None]
    
    # Debuging
    #print('\n')
        

class Drawer(object):
    def __init__(self, oled, data):
        self.oled = oled
        self.data = data
        self.amplifier = 6 # Default value

    def rotation(self, name, alpha, beta, theta):
        try:
            self.name = name
            self.alpha = alpha
            self.beta = beta
            self.theta = theta
            
            rotation(self.oled, self.data, self.name, self.alpha, self.beta, self.theta, self.amplifier)
            
        except:
            print(f'The shape \"{self.name}\" does not exist!')
    
    def setAmplifier(self, amplifier):
        self.amplifier = int(amplifier)
