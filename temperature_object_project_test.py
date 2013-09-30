import unittest
from temperature_object_project import Temperature, Celsius, Kelvin, Fahrenheit

class temperature_test(unittest.TestCase):

 def test_fahrenheit(self):
  """Tests if fahrenheit initializes properly""" 
  my_temp = Temperature({"f":75})
  self.assertAlmostEqual(my_temp.celsius, 23.9, 1)
 
 def test_kelvin(self):
  """Tests if kelvin initializes properly"""
  my_temp = Temperature({"k":273.15})
  self.assertAlmostEqual(my_temp.celsius, 0.0, 1)
  
 def test_in_fahrenheit(self):
  """Tests if in_fahrenheit converts from celsius correctly"""
  my_temp = Temperature({"c":100.0})
  self.assertAlmostEqual(my_temp.in_fahrenheit(), 212.0, 1)
  
 def test_in_celsius(self):
  """Tests if in_celsius converts from celsius correctly"""
  my_temp = Temperature({"c":200.0})
  self.assertAlmostEqual(my_temp.in_celsius(), 200.0, 1)
 
 def test_in_kelvin(self):
  """Tests if in_kelvin converts from celsius correctly"""
  my_temp = Temperature({"c":100.0})
  self.assertAlmostEqual(my_temp.in_kelvin(), 373.15, 1)
 
 def test_Celsius_class(self):
  """Tests if the Celsius class inherits properly from Temperature"""
  my_temp = Celsius(100.0)
  self.assertAlmostEqual(my_temp.celsius, 100.0, 1)
  
 def test_Fahrenheit_class(self):
  """Tests if the Fahrenheit class inherits properly from Temperature"""
  my_temp = Fahrenheit(30.0)
  self.assertAlmostEqual(my_temp.celsius, -1.1, 1)
  
 def test_Kelvin_class(self):
  """Tests if the Kelvin class inherits properly from Temperature"""
  my_temp = Kelvin(300.0)
  self.assertAlmostEqual(my_temp.celsius, 26.9, 1)
 
 
    
 
 
 
 
 