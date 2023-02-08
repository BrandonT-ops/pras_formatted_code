#import RPi.GPIO as GPIO
import time
#import cv2
import time
import threading
import numpy as np
from enum import Enum

VERBOSE = False

class Components():
    """ Modeling the general components controlled by Central """
    def __init__(self, component_type, pin_number):
        """ Initialising components """
        self.component_type = component_type
        self.pin_number = pin_number

    def initialisation(self):
        """ function to initialise GPIO PINS as output or input """
     #   GPIO.setmode(GPIO.BCM)

        if self.component_type == "output":
            for i in self.pin_number:
      #          GPIO.setup(i, GPIO.OUT)
                print("Initilialised as output " + str(i))
        elif self.component_type == "input":
            for i in self.pin_number:
       #          GPIO.setup(i, GPIO.IN)
                 print("Initialised as input " + str(i))


class Light(Components):
    """ Specific model for lights """
    def __init__(self, component_type, pin_number, component_name):
        """ Initialising attributes of parent class, pin numbers are passed in a list """
        super().__init__(component_type, pin_number)
        self.component_name = component_name

    def switch_on(self):
        """ function to switch on the light bulb or bulbs """
        for i in self.pin_number:
            #GPIO.output(i, GPIO.HIGH)
            print("The " + self.component_name + " at pin " + str(self.pin_number) + " is on")
           

    def switch_off(self):
        """ function to switch off the light bulb """
        for i in self.pin_number:
            #GPIO.output(i, GPIO.LOW)
            print("The " + self.component_name + " at pin " + str(self.pin_number) + " is off")


class Camera(Components):
    """ Specific model of Camera """
    def __init__(self,component_type, pin_number, component_name):
        """ Initialising attributes of parent class """
        super().__init__(component_type, pin_number)
        self.component_name = component_name

    def get_camera_images(self):
        """ function to get camera images from IP Camera """

    def send_camera_images(self):
        """ function to send camera images from camera to web """


class Door(Components):
    """ """
    def __init__(self,component_type, pin_number, component_name):
        """ """
        super().__init__(component_type, pin_number)
        self.component_name = component_name
        

    def open_the_door(self):
        """ function to open the door """
        print("The " + self.component_name + " at pin " + str(self.pin_number) + " is opened")

    def close_the_door(self):
        """ function to close the door """
        print("The " + self.component_name + " at pin " + str(self.pin_number) + " is closed")

class Window(Components):
    """ """
    def __init__(self,component_type, pin_number, component_name):
        """ """
        super().__init__(component_type, pin_number)
        self.component_name = component_name
        

    def open_the_window(self):
        """ function to open the window """
        print("The " + self.component_name + " at pin " + str(self.pin_number) + " is opened")

    def close_the_window(self):
        """ function to close the window """
        print("The " + self.component_name + " at pin " + str(self.pin_number) + " is closed")

class Sensors(Components):
    """ Class to model sensors """
    def __init__(self, component_type, pin_number, component_name):
        """Initialising sensor attributes """
        super().__init__(component_type, pin_number)
        self.component_name = component_name

  
class Alarm(Components):
    """ Class to model alarms """
    def __init__(self, component_type, pin_number, component_name):
        """ Initialising alarm attributes """
        super().__init__(component_type, pin_number)

    def notification_sound(self):
        """ function to send a notification sound to the user """
        for i in range(0,3):
          #  GPIO.output(self.pin_number,GPIO.HIGH)
            print ("Beep")
            sleep(1) # Delay in seconds
           # GPIO.output(self.pin_number,GPIO.LOW)

    def alert_sound(self):
        """ function to give an alert sound to the user """
        for i in range(0,3):
           # GPIO.output(self.pin_number,GPIO.HIGH)
            print ("Beep")
            sleep(0.5) # Delay in seconds
           # GPIO.output(self.pin_number,GPIO.LOW)

    def danger_sound(self):
        """ function to send a danger sound to the user """
        for i in range(0,9):
          #  GPIO.output(self.pin_number,GPIO.HIGH)
            print ("Beep")
            sleep(0.25) # Delay in seconds
          #  GPIO.output(self.pin_number,GPIO.LOW)

class GSMModule(Components):
    """ Class to model GSM module and related funcitons"""
    def __init__(self, component_type, pin_number, component_name):
        """ Initialising alarm attributes """
        super().__init__(component_type, pin_number)

    def debug(text):
        if VERBOSE:
            print ("Debug:---", text)

    def resetModem():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(P_RESET, GPIO.OUT)
        GPIO.output(P_RESET, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(P_RESET, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(P_RESET, GPIO.LOW)
        time.sleep(3)

    def togglePower():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(P_POWER, GPIO.OUT)
        GPIO.output(P_POWER, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(P_POWER, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(P_POWER, GPIO.LOW)

    def isReady(ser):
        # Resetting to defaults
        cmd = 'ATZ\r'
        debug("Cmd: " + cmd)
        ser.write(cmd)
        time.sleep(2)
        reply = ser.read(ser.inWaiting())
        time.sleep(8) # Wait until connected to net
        return ("OK" in reply)
    
    def connectGSM(ser, apn):
        # Login to APN, no userid/password needed
        cmd = 'AT+CSTT="' + apn + '"\r'
        debug("Cmd: " + cmd)
        ser.write(cmd)
        time.sleep(3)
        
        # Bringing up network
        cmd = "AT+CIICR\r"
        debug("Cmd: " + cmd)
        ser.write(cmd)
        time.sleep(5)
        
        # Getting IP address
        cmd = "AT+CIFSR\r"
        debug("Cmd: " + cmd)
        ser.write(cmd)
        time.sleep(3)
        
        # Returning all messages from modem
        reply = ser.read(ser.inWaiting())
        debug("connectGSM() retured:\n" + reply)
        return reply

    def send_message(self):
        """ function to send an SMS to a number """

    def listen_for_incoming_messages(self):
        """ function to listen for incoming messages """

    def messages_settings(self):
        """ function to set the settings for the GSM Module """

    def connect_to_the_internet(self):
        """ function to connect to the internet through GSM """    