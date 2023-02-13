""" Here's where everything starts """

""" Importations neccesary """
from central import Central
from components import Light 
from web_controller import Web_controller
from data_manager import File_manager

"""
input_components = Components("input", [1,2,3] )
output_components = Components("output", [4,5,6])

input_components.initialisation()
output_components.initialisation()

light1 = Light("output", [1] , "parlour lights")
light1.initialisation()

light1.switch_on()
light1.switch_off()

#

"""
central1 =  Central(1200, "Central salon")

#wc = Web_controller()

#wc.verify_internet_connection()

#f1 = File_manager("C:\\Brandon\\School Documents\\Year 3 Notes\\S2\\Projet d'integration\\pras_formatted_code\\Data\\TEXT")

#f1.write_to_file("Here's a lot of text and blah blah", "fc")

# Begin
central1.run()