class Temperature(object):
 def __init__(self, options = {}):
  if "c" in options:
   self.celsius = options["c"]
  if "f" in options:
   self.celsius = (options["f"] - 32) * 5.0 / 9
  if "k" in options: 
   self.celsius = options["k"] - 273.15
   
 def in_fahrenheit(self):
  return ((self.celsius * 9.0) / 5) + 32

 def in_celsius(self):
  return self.celsius
 
 def in_kelvin(self):
  return self.celsius + 273.15
  

class Celsius(Temperature):
 def __init__(self, cel):
  super(Celsius, self).__init__({"c":cel})
  
class Fahrenheit(Temperature):
 def __init__(self, fah):
  super(Fahrenheit, self).__init__({"f":fah})
  
class Kelvin(Temperature):
 def __init__(self, kel):
  super(Kelvin, self).__init__({"k":kel})
  
  
 