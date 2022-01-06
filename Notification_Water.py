import time
from plyer import notification
from win32com.client import Dispatch

if __name__ == "__main__":
    while True:  
        notification.notify(
            title = "Please Drink Water Now !",
            message = "The National Science Academies of Science,Research that Human Drink water 3.5 liter per day",
            app_icon = "F:\harry_programmes\icons\glass+soda+water+icon-1320167995413105413_128.ico",
            timeout=10
        )
        speak = Dispatch('SAPI.SpVoice')
        speak.Speak("Please Drink Water Now")  
        time.sleep(60*60)