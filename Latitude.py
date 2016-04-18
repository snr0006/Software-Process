'''
Created on April 15, 2016

@author: Shelby Regelman
'''

'''
Import Modules
'''
import csv
import re

class Latitude(object):
    
    
    
    def __init__(self, degrees=None, minutes=None, hemisphere="N"):
        
        '''
        Constructor
        '''
        #degrees
        if(degrees < 0 or degrees > 90):
            raise ValueError("Sighting.__init__ : degrees should be .GE. 0 and .LE. 90")
        else:
            self.degrees = int(degrees)
        
        #minutes
        if(minutes < 0 or minutes > 59):
            raise ValueError("Sighting.__init__ : minutes should be .GE. 0 and .LT. 60")
        else :
            self.minutes = minutes     
        
        #hemisphere 
        if(degrees == 0 and minutes == 0):
            hemisphere = ""
        elif ((hemisphere != "S") and (hemisphere != "N") and (hemisphere != "")):
            raise ValueError("Sighting.__init__ : hemisphere incorrect value")
        self.hemisphere = hemisphere
        
    
    def getDegrees(self):
        return self.degrees
    
    def getMinutes(self):
        return round(self.minutes, 1)
    
    def getHemisphere(self):
        if (self.hemisphere == "S") :
            self.hemisphere = -1
        if (self.hemisphere == "N") :
            self.hemisphere = 1
        if (self.hemisphere == "") :
            self.hemisphere = 0
        return self.hemisphere
    
    def getString(self):
        sDegrees = str(self.degrees)
        sMinutes = str(self.minutes)
        strn = (self.hemisphere + sDegrees + " " + sMinutes)
        return strn

