'''
Created on Mar 31, 2016

@author: Shelby
'''
import unittest
import prod.Latitude as Latitude

#Tmr0012
class SightingTestSandbox(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    #####################
    #####GREEN LIGHT#####
    #####################
    def test100_010_ShouldConstruct(self):
        degrees = 40
        minutes = 50
        hemisphere = "S"
        print "Testing Constructor: degrees=40, minutes=50, hemisphere=S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
        print "Passed"
    
    def test100_020_ShouldConstruct(self):
        degrees = 40
        minutes = 50
        hemisphere = "N"
        print "Testing Constructor: degrees=40, minutes=50, hemisphere=N"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
        print "Passed"
    
    def test100_030_ShouldConstruct(self):
        degrees = 40
        minutes = 50
        hemisphere = ""
        print "Testing Constructor: degrees=40, minutes=50, hemisphere=''"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
        print "Passed"
    
    def test100_040_ShouldConstruct(self):
        degrees = 0
        minutes = 0
        hemisphere = "S"
        print "Testing Constructor: degrees=0, minutes=0, hemisphere=S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
        print "Passed"
    
    def test100_050_ShouldConstruct(self):
        degrees = 90
        minutes = 59
        hemisphere = "S"
        print "Testing Constructor: degrees=90, minutes=59, hemisphere=S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
        print "Passed"
    
    def test100_060_ShouldGetDegrees(self):
        degrees = 90
        minutes = 59
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getDegrees: degrees=90, minutes=59, hemisphere=S"
        print "Should return: 90"
        self.assertEquals(90, myL.getDegrees())
        print "Passed: returned ", myL.getDegrees()
    
    def test100_070_ShouldGetMinutes(self):
        degrees = 30
        minutes = 50
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getMinutes: degrees=30, minutes=50, hemisphere=S"
        print "Should return: 50.0"
        self.assertEquals(50.0, myL.getMinutes())
        print "Passed: returned ", myL.getMinutes()
    
    def test100_080_ShouldGetHemisphere(self):
        degrees = 90
        minutes = 59
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getHemisphere: degrees=90, minutes=59, hemisphere=S"
        print "Should return: -1"
        self.assertEquals(-1, myL.getHemisphere())
        print "Passed: returned ", myL.getHemisphere()
    
    def test100_090_ShouldGetHemisphere(self):
        degrees = 90
        minutes = 59
        hemisphere = "N"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getHemisphere: degrees=90, minutes=59, hemisphere=N"
        print "Should return: 1"
        self.assertEquals(1, myL.getHemisphere())
        print "Passed: returned ", myL.getHemisphere()
    
    def test100_100_ShouldGetHemisphere(self):
        degrees = 90
        minutes = 59
        hemisphere = ""
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getHemisphere: degrees=90, minutes=59, hemisphere=''"
        print "Should return: 0"
        self.assertEquals(0, myL.getHemisphere())
        print "Passed: returned ", myL.getHemisphere()
    
    def test100_110_ShouldGetString(self):
        degrees = 40
        minutes = 20.4
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getString: degrees=40, minutes=20.4, hemisphere=S"
        print "Should return: S40 20.4"
        self.assertEquals('S40 20.4', myL.getString())
        print "Passed: returned ", myL.getString()
    
    def test100_120_ShouldGetString(self):
        degrees = 60
        minutes = 49.7
        hemisphere = "N"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getString: degrees=60, minutes=49.7, hemisphere=N"
        print "Should return: N60 49.7"
        self.assertEquals('N60 49.7', myL.getString())
        print "Passed: returned ", myL.getString()
    
    def test100_130_ShouldGetString(self):
        degrees = 0
        minutes = 0
        hemisphere = ""
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getString: degrees=0, minutes=0, hemisphere=''"
        print "Should return: 0 0"
        self.assertEquals('0 0', myL.getString())
        print "Passed: returned ", myL.getString()
    
    def test100_140_ShouldGetMinutes(self):
        degrees = 30
        minutes = 55.6662
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getMinutes: degrees=30, minutes=55.6662, hemisphere=S"
        print "Should return: 55.7"
        self.assertEquals(55.7, myL.getMinutes())
        print "Passed: returned ", myL.getMinutes()
    
    def test100_150_ShouldGetMinutes(self):
        degrees = 30
        minutes = 25.98
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getMinutes: degrees=30, minutes=25.98, hemisphere=S"
        print "Should return: 26.0"
        self.assertEquals(26.0, myL.getMinutes())
        print "Passed: returned ", myL.getMinutes()
    
    def test100_160_ShouldGetMinutes(self):
        degrees = 30
        minutes = 47.6
        hemisphere = "S"
        myL = Latitude.Latitude(degrees, minutes, hemisphere)
        print "Testing getMinutes: degrees=30, minutes=47.6, hemisphere=S"
        print "Should return: 47.6"
        self.assertEquals(47.6, myL.getMinutes())
        print "Passed: returned ", myL.getMinutes()
    
    
'''
    ###################
    #####RED LIGHT#####
    ###################
    #THESE SHOULD HAVE BEEN RED LIGHT TESTED,
    #BUT I DON'T HAVE THAT PLUGIN WORKING CORRECTLY
    #ON MY COMPUTER. SO I HAVE POSTED SOME RED LIGHT
    #TESTS HERE, AND WHEN RUN THEY DO CAUSE AN ERROR
    
    
    def test200_010_ShouldNotConstruct(self):
        degrees = 120
        minutes = 50
        hemisphere = "S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_020_ShouldNotConstruct(self):
        degrees = -10
        minutes = 0
        hemisphere = "S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_030_ShouldNotConstruct(self):
        degrees = 40
        minutes = 80
        hemisphere = "S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_040_ShouldNotConstruct(self):
        degrees = 40
        minutes = -5
        hemisphere = "S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_050_ShouldNotConstruct(self):
        degrees = 40
        minutes = 50
        hemisphere = "G"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_060_ShouldNotConstruct(self):
        degrees = 90
        minutes = 60
        hemisphere = "S"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_070_ShouldNotConstruct(self):
        degrees = 90
        minutes = 59
        hemisphere = 90
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_080_ShouldNotConstruct(self):
        degrees = "A"
        minutes = 59
        hemisphere = "N"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    
    def test200_090_ShouldNotConstruct(self):
        degrees = 40
        minutes = "G"
        hemisphere = "N"
        self.assertIsInstance(Latitude.Latitude(degrees, minutes, hemisphere), Latitude.Latitude)
    '''