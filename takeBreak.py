import pyttsx3
from plyer import notification
import time


# Speak method
def Speak(audio):
    
    # Calling the initial constructor
    # of pyttsx3
    engine = pyttsx3.init('sapi5')
    
    # Calling the getter method
    voices = engine.getProperty('voices')
    
    # Calling the setter method
    engine.setProperty('voice', voices[1].id)
    
    engine.say(audio)
    engine.runAndWait()
    
    
def Take_break():
    
    Speak("Hi Pichu, Good Morning ! lets start the day, i will be there to help you have some rest in between! I have strict instructions from Amir")
    time.sleep(5)
    
    Speak("Lets start")
    
    # A notification we will held that
    # Let's Start sir and with a message of
    # will tell you to take a break after 45
    # mins for 10 seconds
    while(True):

        notification.notify(title="Let's Start Mam",
        message="will tell you to take a break after 45 mins",
        timeout=30)
        
        # For 45 min the will be no notification but
        # after 45 min a notification will pop up.
        time.sleep(45*60)

        Speak("Please Take a break Mam, lets walk for 10 minutes, ektu hete ai edil odik")
        time.sleep(5*60)

        Speak("Please Take a break Mam")
        
        notification.notify(title="Break Notification",
        message="Please do use your device after sometime as you have"
        "been continuously using it for 45 mins and it will affect your eyes and back",
        timeout=20)

        
# Driver's Code		
if __name__ == '__main__':
    Take_break()
