""" Here's where everything starts """

""" Importations neccesary """
from enum import Enum
from central import Central as c
from components import Components, Light 

input_components = Components("input", [1,2,3] )
output_components = Components("output", [4,5,6])

input_components.initialisation()
output_components.initialisation()

light1 = Light("output", [1] , "parlour lights")
light1.initialisation()

light1.switch_on()
light1.switch_off()

#central1 =  c(1200, "Central salon")

# Begin
#central1.run()