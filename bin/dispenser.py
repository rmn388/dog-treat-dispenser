import time
import RPi.GPIO as GPIO

class Dispenser(object):
    """
    Controls the treat dispenser mechanism using the Raspberry Pis
    GPIO pins to trigger functions on the arduino that control
    the servo motor.
    """
    
    def __init__(self, alert_pin = 17, treat_pin = 18):
        self.alert_pin = alert_pin
        self.treat_pin = treat_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.alert_pin, GPIO.OUT)
        GPIO.setup(self.treat_pin, GPIO.OUT)
        GPIO.output(self.alert_pin, 1)
        GPIO.output(self.treat_pin, 1)
        
        
    def alert_pet(self, reps=3):
        """Twitch Servo to get the pet's attention"""
        for x in range(0,reps):
            time.sleep(1)
            GPIO.output(self.alert_pin, 0)
            time.sleep(1)
            GPIO.output(self.alert_pin, 1)
        return
   
    def give_treat(self, num_treats = 1):
        """Trigger servo to give treat"""
        for x in range(0,num_treats):
            GPIO.output(self.treat_pin, 0)
            time.sleep(.5)
            GPIO.output(self.treat_pin, 1)
            time.sleep(.5)
        return
    

if (__name__ == "__main__"):
    dispenser = Dispenser()
    dispenser.alert_pet()
    dispenser.give_treat()