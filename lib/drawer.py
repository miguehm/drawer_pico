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

def rotate(coordinates, alpha, beta, theta):
    from math import sin, cos, pi
    
    RAD = pi/180 # 3.141/180 # Radian value

    # Angles in gradians
    """
    alpha: respect to the 'x' axis
    beta: respect to the 'y' axis
    theta: respect to the 'z' axis
    """
    
    # Getting the Sine and Cosine values of the angles (alpha, beta, theta)
    presicion = 100 # Number of decimals for sine and cosine
    s_alpha = int(sin(alpha*RAD)*presicion)/presicion
    c_alpha = int(cos(alpha*RAD)*presicion)/presicion
    
    s_beta = int(sin(beta*RAD)*presicion)/presicion
    c_beta = int(cos(beta*RAD)*presicion)/presicion
    
    s_theta = int(sin(theta*RAD)*presicion)/presicion
    c_theta = int(cos(theta*RAD)*presicion)/presicion
    
    # auxiliar variable
    newCoordinates = []
    
    # Set lines on Display Oled process
    for j in range(len(coordinates)/3): # divide to 3 'cause the coordinates has three values (x,y,z)
        x = coordinates[j*3]
        y = coordinates[j*3+1]
        z = coordinates[j*3+2]
        
        #print(coordinates[j*3])
        
        # Transformation Matrix
        rx = ((x*c_theta*c_beta)+y*(-s_theta*c_alpha+c_theta*s_beta*s_alpha)+z*(s_theta*s_alpha+c_theta*s_beta*c_alpha))#*amplifier
        newCoordinates.append(rx)
        
        ry = ((x*s_theta*c_beta)+y*(c_theta*c_alpha+s_theta*s_beta*s_alpha)+z*(-c_theta*s_alpha+s_theta*s_beta*c_alpha))#*amplifier
        newCoordinates.append(ry)
        
        rz = ((x*-s_beta)+(y*c_beta*s_alpha)+(z*c_beta*c_alpha))#*amplifier
        newCoordinates.append(rz)   
    
    # Add a function traslation and send newCoordinates?
    return newCoordinates

def move(coordinates, distanceX, distanceY, distanceZ):
    # auxiliar variable
    newCoordinates = []
    
    # Set lines on Display Oled process
    for j in range(len(coordinates)/3): # divide to 3 'cause the coordinates has three values (x,y,z)
        x = coordinates[j*3]
        y = coordinates[j*3+1]
        z = coordinates[j*3+2]
        
        mx = x+distanceX
        newCoordinates.append(mx)
        
        my = y+distanceY
        newCoordinates.append(my)
        
        mz = z+distanceZ
        newCoordinates.append(mz)
    
    return newCoordinates

def resize(coordinates, resizeX, resizeY, resizeZ):
    # auxiliar variable
    newCoordinates = []
    
    if(not resizeY):
        resizeZ=resizeY=resizeX
    
    for j in range(len(coordinates)/3):
        x = coordinates[j*3]
        y = coordinates[j*3+1]
        z = coordinates[j*3+2]
        
        # Transformation Matrix
        tx = x*resizeX
        ty = y*resizeY
        tz = z*resizeZ
        
        newCoordinates.append(tx)
        newCoordinates.append(ty)
        newCoordinates.append(tz)
        
    return newCoordinates

def draw(oled, coordinates, amplifier):
    
    # ================= Draw =================
    # Auxiliaries variables
    coord1 = [None, None]
    coord2 = [None, None]
    
    # Prepare the coordinates to 'line' function
    # 64: oled width / 2
    # 32: oled height / 2
    for j in range(len(coordinates)/3):
        x = (coordinates[j*3])*amplifier
        y = (coordinates[j*3+1])*amplifier
        
        if(j != 0):
            coord2 = [int(x)+64, -(int(y))+32]
        else:
            coord1 = [int(x)+64, -(int(y))+32]
            
        if(coord2[0]):
            # Creating line
            oled.line(coord1[0], coord1[1], coord2[0], coord2[1], 1) # Check for white screens
            
            # Restarting the auxiliaries variables
            coord1 = coord2
            coord2 = [None, None]

class Drawer(object):
    def __init__(self, oled, data):
        self.oled = oled
        self.data = data
        self.copy = {}
        self.amplifier = 6 # Default value
        
    def setAmplifier(self, amplifier):
        self.amplifier = int(amplifier)

    def existCopy(self, name):
        try:
            if(self.copy[name]):
                pass
        except:
            self.copy[name] = self.data['shapes'][name]['coordinates'].copy()

    def rotate(self, name, alpha, beta, theta):
        self.existCopy(name)
        coordinates = self.data['shapes'][name]['coordinates']
        coordinates = rotate(coordinates, alpha, beta, theta)
        self.data['shapes'][name]['coordinates'] = coordinates
        
    def move(self, name, distanceX, distanceY, distanceZ):
        self.existCopy(name)
        coordinates = self.data['shapes'][name]['coordinates']
        coordinates = move(coordinates, distanceX, distanceY, distanceZ)
        self.data['shapes'][name]['coordinates'] = coordinates
        
    def resize(self, name, x=1, y=None, z=None):
        self.existCopy(name)
        coordinates = self.data['shapes'][name]['coordinates']
        
        if(not y):
            z = y = x
            
        coordinates = resize(coordinates, x, y, z)
        self.data['shapes'][name]['coordinates'] = coordinates
    
    def draw(self, name):
        # Cheking if 'coordinates' has x, y, z coordinates format
        if(len(self.data['shapes'][name]['coordinates'])%3 == 0):
            # Sending information
            coordinates = self.data['shapes'][name]['coordinates']
            draw(self.oled, coordinates, self.amplifier)
            
            # Reset coordinates
            self.data['shapes'][name]['coordinates'] = self.copy[name].copy()
            self.copy = {}
            
        else:
            print(f'The coordinates are invalid!')
