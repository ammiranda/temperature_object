class Temperature:
 def __init__(self, options = {}):
  if "c" in options:
   self.celsius = options["c"]
  if "f" in options:
   self.celsius = (options["f"] - 32) * 5.0 / 9
  if "k" in options: 
   self.celsius = options["k"] - 273.15
   
 def in_faharenheit:
  return ((self.celsius * 9.0) / 5) + 32

 def in_celsius:
  return self.celsius
 
 def in_kelvin:
  return self.celsius + 273.15
  

class Celsius(Temperature):
 def __init__(self, celsius):
  super(Celsius, self).__init__({"c":cel})
  
class Fahrenheit(Temperature):
 def __init__(self, fahrenheit):
  super(Fahrenheit, self).__init__({"f":fah})
  
class Kelvin(Temperature):
 def __init__(self, kelvin):
  super(Kelvin, self).__init__({"k":kel})
  
  
 