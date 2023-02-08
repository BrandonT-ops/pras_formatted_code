""" Classes neccesary for the central class to work"""
from data_manager import Data_manager
from data_manager import Json_manager as jm
from data_manager import File_manager as fm
from web_controller import Web_controller as wb

""" Imports neccesary """
import threading

class Central():
    """ Modeling the raspberry pi central controller """
    def __init__(self, id, name):
        """ Initialising controller attributes """
        self.id = id
        self.name = name

    def run(self):
        """ run the central """
        threadSocketStart = False
        print("The central is working")
        wb.verify_internet_connection()
        self.listen_for_instructions()
        
        while True:
            if fm.check_if_file_exists("/home/pi/Desktop/PY_CODE/ABODE_CENTRAL/data.txt"):
                print("Configuration file present, we continue...")
                if fm.read_from_file("/home/pi/Desktop/PY_CODE/ABODE_CENTRAL/data.txt","fc") == "True" +"\n":
                    print ("First connection")
                    #verifies internet connection
                    if wb.verify_internet_connection():
                        #sends information to the server
                        if wb.enrol_central_in_web():
                            print("Enrollment Successful")
                            fm.write_to_file("/home/pi/Desktop/PY_CODE/ABODE_CENTRAL/data.txt","False\n","fc")
                        else:
                            print("Enrollment failed") 
                    else:
                        print("verify your internet connection")
                else:
                    print("nth connection")
                    wb.get_central_structure()


                    self.set_pin_variables()
                    if threadSocketStart == False :
                        # starting threadSocket
                        threadSocket.start()
                        threadSocketStart = True
            else:
                print("Config file missing. Contact technical support!")                   


    def stop(self):
        """ stop the central """
        print("The central has stopped")

    def get_central_id(self):
        """ Get central identifier """
        print(" This central's identifier is " + self.id)

    def get_central_name(self):
        """ Get central name """
        print(" This central's name is " + self.name)

    def listen_for_instructions(self):
        """function to listen for instructions given by user from web """
        thread_socket =  threading.Thread(target= wb.get_instructions)

    def set_pin_variables(self):
        """ function to set pin variables before running"""
        centralInfo = {}
	
	    #reading the config file to set pins 
        data = jm.json_read_from_file('abodeConfig.json')
    
        for i in range(0,len(data['centrale'])):
            name = data['centrale'][i]['name']
            types = data['centrale'][i]['type']
            port = data['centrale'][i]['port']
            state = data['centrale'][i]['state']
            pinMode =  data['centrale'][i]['pinMode']
        
        centralInfo[name] = port
        
        GPIO.setup(centralData[name], pinMode)
        if pinMode == 0:
            GPIO.output(centralData[name], state)
        return centralInfo