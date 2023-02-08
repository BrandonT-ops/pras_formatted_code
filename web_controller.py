""" Imports neccesary for the work of web controller """
import asyncio
import websockets
import requests
#import RPi.GPIO as GPIO
import time
from requests.auth import HTTPBasicAuth


#GPIO section
#GPIO.cleanup()
#GPIO.setmode(GPIO.BCM)

#internet connectivity led
#GPIO.setup(23, GPIO.OUT)

    
class Web_controller():
    """ A class to handle all web affaires  """
    def __init__(self):
        """ Initialising the web controller class """

    def get_instructions(self):
        """ function to get instructions from web """
        asyncio.run(Web_controller.data_reception())

    def get_central_structure(self):
        """ function to get central structure """
        data = jsonReadFromFile("JSON/centraleData.json")
	
        url = "https://abodeappheroku.herokuapp.com/models/composant/?search="+data['id']
	
        myHeaders = {'Authorization' : 'Token d1168d0f616c34d1792b8c1a8faa820129505160'}
	
        timeout = 5
        try:
            response = requests.post(url,headers=myHeaders)
		
            if(response.status_code == 201 or response.status_code == 200):
                jsonWriteToFile(response.json(),"JSON/abodeConfig.json")
			
        except (response.ConnectionError,response.Timeout) as exception:
		
                print("Error fetching Centrale Structure")
    
    def verify_internet_connection(self):
        """ function to verify internet connection """ 
        url = "https://www.google.com"
        timeout = 5
        try:
            request = requests.get(url,timeout = timeout)
            ans = True
            print("Connected to the internet")
            time.sleep(1)
 #           GPIO.output(23, GPIO.HIGH)
		
        except (requests.ConnectionError,requests.Timeout) as exception:
            ans = False
            print("Not connected to the internet")
            time.sleep(1)
  #          GPIO.output(23, GPIO.LOW)
		
        return ans

    def enrol_central_in_web(self):
        """ function to enrol central in the web API """
        url = "https://abodeappheroku.herokuapp.com/models/centrale/"
        data={"identifiant":"abode0000000001cid"}
	
        myHeaders = {'Authorization' : 'Token d1168d0f616c34d1792b8c1a8faa820129505160'}

        timeout = 5
        try:
            response = requests.post(url,headers=myHeaders,data={"identifiant":"abode0000000001cid"})
            ans = False
            if(response.status_code == 201):
                ans= True
                jsonWriteToFile(response.json(),"JSON/centraleData.json")
                Web_controller.get_central_structure()			
		
        except (response.ConnectionError,response.Timeout) as exception:
            ans = False
            print("Could not access the server")
		
        return ans

    
    async def data_reception(self):
        """ function to receive data from web """
        websocket= await websockets.connect("ws://abodeappheroku.herokuapp.com/ws/url/")
        while 1:
            info = await websocket.recv()
            print(info)
        