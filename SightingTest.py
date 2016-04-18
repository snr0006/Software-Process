'''
Created on Mar 28, 2016

@author: Shelby Regelman
'''
import prod.Sighting as Sighting
import math
import unittest
from datetime import datetime, date, time
from prod.Sandbox import temperature

#Tmr0012
class SightingTest(unittest.TestCase):

    def setUp(self):
        self.body = 'star'
        self.date = date(2016, 1, 16)
        self.time = time(10, 45, 30)
        self.altitude = 30, 10.4
        self.height = 6
        self.defaultHeight = 0
        self.temperature = 100
        self.defaultTemperature = 72
        self.pressure = 999
        self.defaultPressure = 1010
        self.artificialHorizon = True
        self.defaultArtificialHorizon = False

    def tearDown(self):
        pass
    

    # 100 constructor
    # Happy path tests
    def test100_010_ShouldConstructSighting(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                temperature=self.temperature,
                                pressure=self.pressure,
                                artificialHorizon=self.artificialHorizon
                                )
        self.assertIsInstance(theSighting, Sighting.Sighting)
    
    def test100_020_ShouldConstructSightingWithDefaultHeight(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                temperature=self.temperature,
                                pressure=self.pressure,
                                artificialHorizon=self.artificialHorizon
                                )
        self.assertIsInstance(theSighting, Sighting.Sighting)
    
    def test100_030_ShouldConstructSightingWithDefaultTemperature(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                pressure=self.pressure,
                                artificialHorizon=self.artificialHorizon
                                )
        self.assertIsInstance(theSighting, Sighting.Sighting)
    
    def test100_040_ShouldConstructSightingWithDefaultPressure(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                temperature=self.temperature,
                                artificialHorizon=self.artificialHorizon
                                )
        self.assertIsInstance(theSighting, Sighting.Sighting)
        
    def test100_050_ShouldConstructSightingWithDefaultHorixon(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                temperature=self.temperature,
                                pressure=self.pressure,
                                )
        self.assertIsInstance(theSighting, Sighting.Sighting)
    
    def test100_060_ShouldGetBody(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                temperature=self.temperature,
                                pressure=self.pressure,
                                )
        print "Testing getBody()...."
        print "Should return: star"
        self.assertEquals('star', theSighting.getBody())
        print "Passed: " + theSighting.getBody()
    
    def test200_010_ShouldGetGHADate(self):
        aries = 'C:\\Users\\Shelby\\workspace\\CA03\\aries.txt'
        stars = 'C:\\Users\\Shelby\\workspace\\CA03\\stars.txt'
        degrees = 30
        minutes = 47.6
        hemisphere = "S"
        
        body = "Betelgeuse"
        dates = date(2016, 1, 17)
        times = time(03, 15, 42)
        altitude = 30, 10.4
        height = 5
        temperature = 70
                                
        print "Testing getGHA: aries, stars"
        myS = Sighting.Sighting(body, dates, times, altitude, 
                            height, temperature, pressure=1010, 
                            artificialHorizon=None)
        
        self.assertEquals(('75\xc2\xb054.3', '7\xc2\xb024.3'), myS.getGHA(aries, stars))
        print "Passed returned " + str(myS.getGHA(aries, stars))
    
    
    
    
    
    
    
    def test100_900_ShouldFailOnMissingBody(self):
        expectedString = "Sighting.__init__: body can not be empty"
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                pressure=self.pressure,
                                artificialHorizon=self.artificialHorizon
                                )
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            date=self.date,
                                            time=self.time,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
            pass
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for missing body")
    
    def test100_901_ShouldFailOnNonStringBody(self):
        expectedString = "Sighting.__init__: invalid entry for body"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=42,
                                            date=self.date,
                                            time=self.time,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for non-string body")      
        
    def test100_902_ShouldFailOnEmptyBody(self):
        expectedString = "Sighting.__init__: invalid entry for body"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body="",
                                            date=self.date,
                                            time=self.time,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for body length")  
       
# date parm
    '''def test100_911_ShouldFailOnMissingDateDate(self):
        expectedString = "Sighting.__init__: date needs to be in the correct format: Y-M-D"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body="",
                                            time=self.time,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for missing date") 
    '''    
    def test100_912_ShouldFailOnMissingNondateDate(self):
        expectedString = "Sighting.__init__: date needs to be in the correct format: Y-M-D"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=42,
                                            time=self.time,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for invalid type for date") 
    
# time parm
    def test100_921_ShouldFailOnMissingMissingTime(self):
        expectedString = "Sighting.__init__: time can not be empty"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for missing time") 
    '''  
    def test100_922_ShouldFailOnMissingNontimeTime(self):
        expectedString = "Sighting.__init__: time needs to be in the correct format: H:M:S"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=42,
                                            altitude=self.altitude,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad time") 
    
# altitude parm
    def test100_931_ShouldFailOnMissingAltitude(self):
        expectedString = "Sighting.__init__ : incorrect amounts"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for missing altitude") 
    '''   
    def test100_932_ShouldFailOnMalformedAltitude(self):
        expectedString = "Sighiting.__init__: incorrect amounts"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=42,
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for missing altitude") 
    '''   
    def test100_933_ShouldFailOnBelowBoundAltitudeDegrees(self):
        expectedString = "Sighting.__init__: incorrect amounts"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=(-1, 10),
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad altitude") 
        
    def test100_934_ShouldFailOnAboveBoundAltitudeDegrees(self):
        expectedString = "Sighting.__init__: incorrect amounts"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=(90, 10),
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad altitude") 
        
    def test100_935_ShouldFailOnBadAltitudeDegrees(self):
        expectedString = "Sighting.__init__:"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=('a', 60),
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad altitude")
        
    def test100_936_ShouldFailOnBelowBoundAltitudeMinutes(self):
        expectedString = "Sighting.__init__:"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=(0, -1),
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad altitude")
        
    def test100_937_ShouldFailOnAboveBoundAltitudeMinutes(self):
        expectedString = "Sighting.__init__:"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=(0, 60),
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad altitude")
        
    def test100_938_ShouldFailOnAboveInvalidAltitudeMinutes(self):
        expectedString = "Sighting.__init__: incorrect amounts"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=(0, 'a'),
                                            height=self.height,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for bad altitude")
    '''    
# height parm       
    def test100_942_ShouldFailOnBelowBoundHeight(self):
        expectedString = "Sighting.__init__: height can't be less than 0"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=self.altitude,
                                            height=-1,
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for below bound height ")
        
    def test100_943_ShouldFailOnBelowInvalidHeight(self):
        expectedString = "Sighting.__init__: height must be an integer"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                            body=self.body,
                                            date=self.date,
                                            time=self.time,
                                            altitude=self.altitude,
                                            height='a',
                                            temperature=self.temperature,
                                            pressure=self.pressure,
                                            artificialHorizon=self.artificialHorizon
                                            )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for invalid height")
    
# temperature parm
    def test100_951_ShouldFailOnBelowBoundTemperature(self):
        expectedString = "Sighting.__init__: temperature should be .GE. -20 and .LE. 120"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body=self.body,
                                    date=self.date,
                                    time=self.time,
                                    altitude=self.altitude,
                                    height=self.height,
                                    temperature=-21,
                                    pressure=self.pressure,
                                    artificialHorizon=self.artificialHorizon
                                    )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for below bound temperature") 
       
    def test100_952_ShouldFailOnAboveBoundTemperature(self):
        expectedString = "Sighting.__init__: temperature should be .GE. -20 and .LE. 120"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body=self.body,
                                    date=self.date,
                                    time=self.time,
                                    altitude=self.altitude,
                                    height=self.height,
                                    temperature=121,
                                    pressure=self.pressure,
                                    artificialHorizon=self.artificialHorizon
                                    )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for above bound temperature") 
    
    '''    
    def test100_953_ShouldFailOnAboveInvalidTemperature(self):
        expectedString = "Sighting.__init__: temperature must be an integer"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body=self.body,
                                    date=self.date,
                                    time=self.time,
                                    altitude=self.altitude,
                                    height=self.height,
                                    temperature='a',
                                    pressure=self.pressure,
                                    artificialHorizon=self.artificialHorizon
                                    )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for invalid temperature") 
    '''    
#  pressure parm
    def test100_961_ShouldFailOnBelowBoundPressure(self):
        expectedString = "Sighting.__init__: pressure should be .GE. 100 and .LE. 1100"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body=self.body,
                                    date=self.date,
                                    time=self.time,
                                    altitude=self.altitude,
                                    height=self.height,
                                    temperature=self.temperature,
                                    pressure=99,
                                    artificialHorizon=self.artificialHorizon
                                    )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for below bound temperature") 
        
    def test100_962_ShouldFailOnAboveBoundPressure(self):
        expectedString = "Sighting.__init__: pressure should be .GE. 100 and .LE. 1100"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body=self.body,
                                    date=self.date,
                                    time=self.time,
                                    altitude=self.altitude,
                                    height=self.height,
                                    temperature=self.temperature,
                                    pressure=1101,
                                    artificialHorizon=self.artificialHorizon
                                    )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for above bound pressure") 
    
    '''    
    def test100_963_ShouldFailOnAboveInvalidPressure(self):
        expectedString = "Sighting.__init__: pressure must be an integer"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body=self.body,
                                    date=self.date,
                                    time=self.time,
                                    altitude=self.altitude,
                                    height=self.height,
                                    temperature=self.temperature,
                                    pressure='a',
                                    artificialHorizon=self.artificialHorizon
                                    )
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for invalid pressure") 
        
#   getters
    '''
    def test200_010_ShouldGetAllValues(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                height=self.height,
                                temperature=self.temperature,
                                pressure=self.pressure,
                                artificialHorizon=self.artificialHorizon
                                )
        self.assertEqual(self.body, theSighting.getBody())
        self.assertEqual(self.date, theSighting.getDate())
        self.assertEqual(self.time, theSighting.getTime())
        self.assertTupleEqual(self.altitude, theSighting.getAltitude())
        self.assertEqual(self.height, theSighting.getHeight())
        self.assertEqual(self.temperature, theSighting.getTemperature())
        self.assertEqual(self.pressure, theSighting.getPressure())
        self.assertEqual(self.artificialHorizon, theSighting.isArtificialHorizon())  
    
    def test200_010_ShouldGetDefaultValues(self):
        theSighting = Sighting.Sighting(
                                body=self.body,
                                date=self.date,
                                time=self.time,
                                altitude=self.altitude,
                                )
        self.assertEqual(self.defaultHeight, theSighting.getHeight())
        self.assertEqual(self.defaultTemperature, theSighting.getTemperature())
        self.assertEqual(self.defaultPressure, theSighting.getPressure())
        self.assertEqual(self.defaultArtificialHorizon, theSighting.isArtificialHorizon())  
        
# getAltitudeCorrection
# Happy path
    '''
    def test300_010_ShouldGetAltitudeCorrectionForNaturalHorizon(self):
        theSighting = Sighting.Sighting(
                                body='star',
                                date=self.date,
                                time=self.time,
                                altitude=(15, 4.6),
                                height=6,
                                temperature=72,
                                pressure=1010,
                                artificialHorizon=False
                                )
        result = theSighting.getAltitudeCorrection()
        self.assertEqual(result[0], 14)
        self.assertAlmostEquals(result[1], 58.8, 2)
       
    def test300_020_ShouldGetAltitudeCorrectionForArtificialHorizon(self):
        theSighting = Sighting.Sighting(
                                body='star',
                                date=self.date,
                                time=self.time,
                                altitude=(15, 4.6),
                                height=6,
                                temperature=72,
                                pressure=1010,
                                artificialHorizon=True
                                )
        result = theSighting.getAltitudeCorrection()
        self.assertEqual(result[0], 15)
        self.assertAlmostEquals(result[1], 1.2, 2)
        
# Sad path
    def test300_910_ShouldFailOnLowAltitude(self):
        expectedString = "Sighting.getAltitudeCorrection:"
        with self.assertRaises(ValueError) as context:
            theSighting = Sighting.Sighting(
                                    body='star',
                                    date=self.date,
                                    time=self.time,
                                    altitude=(0, 0),
                                    height=6,
                                    temperature=72,
                                    pressure=1010,
                                    artificialHorizon=False
                                    )
            theSighting.getAltitudeCorrection()
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)],
                          "Minor:  failure to check for invalid pressure") 
        
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
    
    
    
    '''
    '''
    def test100_010_ShouldConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test100_020_ShouldConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        height = '13'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)

    def test100_030_ShouldConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        height = '13'
        temperature = 70
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height, temperature, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test100_040_ShouldConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        height = '13'
        temperature = 70
        pressure = 1000
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height, temperature, pressure, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test100_050_ShouldConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        height = '13'
        temperature = 70
        pressure = 1000
        artificialHorizon = True
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height, temperature, pressure, 
                            artificialHorizon), Sighting.Sighting)
    
    def test100_060_ShouldConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        height = '13'
        temperature = 70
        pressure = 1000
        artificialHorizon = False
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height, temperature, pressure, 
                            artificialHorizon), Sighting.Sighting)
    
    def test100_070_ShouldGetBody(self):
        body="Sierra"
        date = '2016-05-10'
        time = '23:40:01'
        altitude = '015 04.9'
        myS = Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None)
        self.assertEquals("Sierra", myS.getBody())
    
    
    
    
    
    
        
    """def test100_030_ShouldConstruct(self): 
        f = "C:\Users\Shelby\Desktop\CA02\sightingFile"
        data = parse(f)
            
        stg = data.getElementsByTagName("sighting")
        for st in stg:
            body = st.getElementsByTagName("body").firstChild.data
            date = body = st.getElementsByTagName("date")
            time = body = st.getElementsByTagName("time")
            altitude = body = st.getElementsByTagName("observation")
            height = body = st.getElementsByTagName("height")




        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)"""
        
    
        


    """
    THESE ARE SAD PATHS, or red lights
    BUT I CANNOT RUN THEM BECAUSE MY RED/GREEN
    LIGHT PLUGIN DOES NOT WORK
    
    #Sad Paths
    def test200_010_ShouldNotConstruct(self): 
        body = ""
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test200_020_ShouldNotConstruct(self): 
        body = "a"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)

    def test200_030_ShouldNotConstruct(self): 
        body = "ALtair"
        date = ''
        time = '23:40:01'
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)

    def test200_040_ShouldNotConstruct(self): 
        body = "Altair"
        date = '2016/03/30'
        time = '23:40:01'
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test200_050_ShouldNotConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = ''
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test200_060_ShouldNotConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23 40 01'
        altitude = '015 04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    def test200_070_ShouldNotConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '015'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
                            
    def test200_080_ShouldNotConstruct(self): 
        body = "Altair"
        date = '2016-03-30'
        time = '23:40:01'
        altitude = '04.9'
        self.assertIsInstance(Sighting.Sighting(body, date, time, altitude, 
                            height=0, temperature=72, pressure=1010, 
                            artificialHorizon=None), Sighting.Sighting)
    
    
    '''
