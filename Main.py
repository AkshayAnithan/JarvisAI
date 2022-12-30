import speech_recognition as sr
import os
#from Jarvis import MainExe
from Features.Clap import Tester


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #listens in 8 sec sessions

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en") #ml for malayalam
        
    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

# def WakeupDetected():
#     queery = Listen().lower()
#     if "jarvis" in queery:
#         print("Wake up detected..!")
#         MainExe()
    
#     else:
#         pass
        
# while True:
#     WakeupDetected()
    
data = Tester()
if "True-Mic" == data:
    from Jarvis import MainExecution
    MainExecution()
    