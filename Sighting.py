'''
Created on Mar 22, 2016

@author: Shelby Regelman
'''
'''
Import Modules
'''
from datetime import datetime, date, time, timedelta
import math
from prod import Sandbox
    
class Sighting(object):
    
    def __init__(self, body=None, date=None, time=None, altitude=None, height=0, temperature=72, pressure=1010, artificialHorizon=None):
        
        '''
        Constructor
        '''
        
        #body
        if(body == None):
            raise ValueError("Sighting.__init__: body can not be empty")
        elif (isinstance(body, str)):
            if(len(body) <= 1):
                raise ValueError("Sighting.__init__: invalid entry for body")
            elif(len(body) > 1):
                self.body = body
        else :
            raise ValueError("Sighting.__init__: invalid entry for body")
        
        #date
        if(date == None):
            raise ValueError("Sighting.__init__: date can not be empty")
        elif(len(str(date)) == 0) :
            raise ValueError("Sighting.__init__: date can not be empty")
        else:
            try:
                #self.date = datetime.strptime(date,'%Y-%m-%d')
                self.date = date
            except(TypeError):
                raise TypeError("Sighting.__init__: date needs to be in the correct format: Y-M-D")
            
            try:
                datetime.strptime(str(self.date), '%Y-%m-%d')
            except ValueError:
                raise ValueError("Sighting.__init__: date needs to be in the correct format: Y-M-D")
        
        #time
        if(time == None):
            raise ValueError("Sighting.__init__: time can not be empty")
        else:
            try:
                #self.time = datetime.strptime(time, "%H:%M:%S")
                self.time = time
            except(TypeError):
                raise TypeError("Sighting.__init__: time needs to be in the correct format: H:M:S")
            
            try:
                datetime.strptime(str(self.time), '%H:%M:%S')
            except(TypeError):
                raise TypeError("Sighting.__init__: time needs to be in the correct format: H:M:S")
        
        #altitude
        if(altitude == None):
            raise ValueError("Sighting.__init__: altitude can not be empty")
        elif not altitude:
            raise ValueError("Sighting.__init__: altitude can not be empty")
        else:
            '''alt=altitude.split()
            #alt[0] for degrees
            #alt[1] for minutes
            if((int(alt[0]) < 0 or  int(alt[0]) >= 90) or (float(alt[1]) < 0 or float(alt[1]) >= 60)):
                raise ValueError("Sighiting.__init__: incorrect amounts")
            else:
                self.altitude=int(alt[0]),float(alt[1]) '''
            if isinstance(altitude, int):
                raise ValueError("Sighiting.__init__: incorrect amounts")
            else :
                deg, min = altitude
                if((deg < 0 or  deg >= 90) or (min < 0 or min >= 60)):
                    raise ValueError("Sighiting.__init__: incorrect amounts")
                else:
                    self.altitude=int(deg),float(min)

        #height
        if(height < 0 ):
            raise ValueError("Sighting.__init__: height can't be less than 0")
        elif(isinstance(height, int) == False):
            raise ValueError("Sighting.__init__: height must be an integer")
        else:
            self.height = height
        
        #temperature
        if((temperature < -20) or (temperature > 120)):
            raise ValueError("Sighting.__init__: temperature should be .GE. -20 and .LE. 120")
        elif(isinstance(temperature, int) == False):
            raise ValueError("Sighting.__init__: temperature must be an integer")
        else:
            self.temperature= int(temperature)
        
        #pressure
        if(pressure < 100 or pressure > 1100):
            raise ValueError("Sighting.__init__: pressure should be .GE. 100 and .LE. 1100")
        elif(isinstance(pressure, str)):
            raise ValueError("Sighting.__init__: pressure must be an integer")
        else:
            self.pressure = pressure
        
        #artificialHorizon
        if(artificialHorizon == None):
            self.artificialHorizon = False
        else:
            self.artificialHorizon = artificialHorizon
    
    '''
    add values from xml file
    '''
    '''def add (self, tag, text):
        if(tag == "body"):
            body = text
        if(tag == "date"):
            date = text 
        if(tag == "time"):
            time = text
        if(tag == "observation"):
            altitude = text
        if(tag == "height"):
            height = text
        if(tag == "temperature"):
            temperature = text
        if(tag == "pressure"):
            pressure = text
        if(tag == "horizon"):
            artificialHorizon = text'''
              
        
    def getBody(self) : 
        return self.body
    
    def getDate(self) :
        return self.date
    
    def getTime(self) :
        return self.time
    
    def getAltitude(self) :
        return self.altitude
    
    def getHeight(self) : 
        return self.height
    
    def getTemperature(self) :
        return self.temperature
    
    def getPressure(self) : 
        return self.pressure
    
    def isArtificialHorizon(self) :
        if(self.artificialHorizon == True):
            return True
        else:
            return False
    
    def getAltitudeCorrection(self) : 
        if (self.artificialHorizon == False):
            dip = (-0.97 * math.sqrt(float(self.height)) / 60)
        else:
            dip = 0         
        '''
        ref1 = (-0.00452 * self.pressure)
           
        temperature = float(self.temperature - 32) * (5/9)             
        ref2 = (273 + temperature)
                        
        ref3 = math.tan(self.altitude[0])
                        
        refraction = ref1 / ref2 / ref3
                        
        correctedAltitude = (self.altitude[0] + dip + refraction)
        return "fix this"
        '''
        pass
    
    def getGHA(self, aries=None, stars=None):
        st = []
        stn = []
        timeArray = []
        digitArray = []
        ghaAries1 = ""
        ghaAries2 = ""
        ghaAries = ""
        
        if(aries == None):
            raise ValueError("Sighting.__init__: aries can not be empty")
        elif(stars == None):
            raise ValueError("Sighting.__init__: stars can not be empty")
        else:
            self.aries = aries
            self.stars = stars
            
            searchStar = self.body
            searchD = self.date
            searchDate = searchD.strftime('%m-%d-%Y')
            searchTime = self.time
            
            with open(stars) as starsfile:
                for line in starsfile:
                    stn.append([n for n in line.strip().split('\t')])
                    
                        #q1 = str(starsName).strip('[]')
                        #queue = q1.strip("\'")
                        #if (searchStar == queue) :
                            #return searchStar
                for entry in stn :
                    if(entry[0] == None):
                        raise ValueError("Sighting.__init__: Body can not be empty")
                    if(entry[1] == None):
                        raise ValueError("Sighting.__init__: Date can not be empty")
                    if(entry[2] == None):
                        raise ValueError("Sighting.__init__: DMS can not be empty")
                    if(entry[3] == None):
                        raise ValueError("Sighting.__init__: DMS can not be empty")
                    
                    if (searchStar == entry[0]) :
                        slashDate = entry[1]
                        s1 = str.replace(entry[1], '/', '-')
                        s2 = datetime.strptime(entry[1], '%m/%d/%y')
                        strippedDate = s2.date()    #mm/dd/yyyy
                        
                        dashDate = s2.strftime('%m-%d-%Y')  #mm-dd-yyyy
                        
                        if (searchDate >= dashDate) :
                            tableDate = dashDate
                            shaS = entry[2]
                            if(shaS == None):
                                raise ValueError("Sighting.__init__: Sidereal angle can not be empty")
                            shaStar = str.replace(shaS, '\xc2\xb0', '*')
                            latitude = entry[3]
                            if(latitude == None):
                                raise ValueError("Sighting.__init__: latitude angle can not be empty")
                        
                        '''s4 = s2 - timedelta(days=1)
                        s4b = s4.strftime('%m-%d-%Y')
                        s5 = s2 - timedelta(days=2)
                        s5b = s5.strftime('%m-%d-%Y')
                        
                        if (searchDate == dashDate or searchDate == s4b or searchDate == s5b) :
                            dateToMatch = str(slashDate)
                            starsDate.append(dateToMatch)'''
                
                        '''
                        if (searchDate == s3) :
                            return searchDate
                        else :
                            sd = searchDate + timedelta(days=-1)
                            if (sd == s3) :
                                return searchDate
                            
                            else :
                                sda = searchDate + timedelta(days=1)
                                if (sda == s3) :
                                    return searchDate
                        
                        '''
            
            with open(aries) as ariesfile:
                digitArray = list(str(searchTime))
                hour = ''.join(digitArray[0:2])
                min = ''.join(digitArray[3:5])
                sec = ''.join(digitArray[6:])
                s = (int(min) * 60) + int(sec)
                
                if (digitArray[0] == '0') :
                    hour = digitArray[1]
                
                for line in ariesfile:
                    st.append([n for n in line.strip().split('\t')])
                            
                for valz in st :        
                    if(valz[0] == None):
                        raise ValueError("Sighting.__init__: Date can not be empty")
                    if(valz[1] == None):
                        raise ValueError("Sighting.__init__: Hour can not be empty")
                    if(valz[2] == None):
                        raise ValueError("Sighting.__init__: DMS can not be empty")
                                   
                    slashDate2 = valz[0]
                    d1 = str.replace(valz[0], '/', '-')
                    d2 = datetime.strptime(valz[0], '%m/%d/%y')
                    stripDate = d2.date()    #mm/dd/yyyy
                        
                    dashedDate = d2.strftime('%m-%d-%Y')  #mm-dd-yyyy
                        
                    if (searchDate == dashedDate) :                          
                        timeArray.append(str(searchTime))

                        if (hour == valz[1]) :
                            ghaAries1 = valz[2]
                            
                        if (str(int(hour) + 1) == valz[1]) :
                            ghaAries2 = valz[2]
                        
                ast1 = ghaAries1.index('*')
                dot1 = ghaAries1.index('.')
                deg1 = ghaAries1[0:ast1]
                m1 = ghaAries1[(ast1+1):dot1]
                s1 = ghaAries1[(dot1+1):]
                
                ast2 = ghaAries2.index('*')
                dot2 = ghaAries2.index('.')
                deg2 = ghaAries2[0:ast2]
                m2 = ghaAries2[(ast2+1):dot2]
                s2 = ghaAries2[(dot2+1):]
                
                ast3 = shaStar.index('*')
                dot3 = shaStar.index('.')
                deg3 = shaStar[0:ast3]
                m3 = shaStar[(ast2+1):dot3]
                s3 = shaStar[(dot3+1):]
                
                #Formula for ghaAries1 to seconds
                f1p1 = int(deg1) * 60
                f1p2 = f1p1 + int(m1)
                f1p3 = f1p2 * 60
                f1p4 = f1p3 + int(s1)
                
                #Formula for ghaAries2 to seconds
                f2p1 = int(deg2) * 60
                f2p2 = f2p1 + int(m2)
                f2p3 = f2p2 * 60
                f2p4 = f2p3 + int(s2)
                
                #Formula for shaStar to seconds
                f3p1 = int(deg3) * 60
                f3p2 = f3p1 + int(m3)
                f3p3 = f3p2 * 60
                f3p4 = f3p3 + int(s3)
                
                
                fp1 = float(f2p4 - f1p4)
                fp2 = float(fp1 / 3600)
                fp3 = (float(s) / 3600)
                fp4 = fp2 * fp3
                fp5 = float(f1p4) / 3600
                fp6 = fp5 + fp4
                
                finalDeg = int(fp6/1)
                fp7 = fp6 - finalDeg
                fp8 = fp7 * 60
                finalMin = int(fp8/1)
                fp9 = fp8 - finalMin
                fp10 = fp9 * 60
                finalSec = int(fp10/1) - 1
                
                ghaA = str(finalDeg), '*', str(finalMin), '.', str(finalSec)
                ghaAries = ''.join(ghaA)
                
                #Find ghaObservation in seconds
                ariesSec = fp6 * 3600
                ghaObsSec = f3p4 + ariesSec
                gOS = ghaObsSec / 3600
                
                #Convert to DMS
                ObsDeg = int(gOS/1)
                obs1 = gOS - ObsDeg
                obs2 = obs1 * 60
                ObsMin = int(obs2/1)
                obs3 = obs2 - ObsMin
                obs4 = obs3 * 60
                ObsSec = int(obs4/1) - 1
                
                if (ObsDeg > 360) :
                    ObsDeg = ObsDeg - 360
                ghaObserv = str(ObsDeg), '*', str(ObsMin), '.', str(ObsSec)
                ghaObservate = ''.join(ghaObserv)
                
                ghaObservation = str.replace(ghaObservate, '*', '\xc2\xb0')                    
                
                return ghaObservation, latitude
                
                
                 
                        
                        
                        
                        
                        
                        