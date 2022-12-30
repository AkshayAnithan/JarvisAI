'''
def MainExe():
    Speak("Main Execution has been started.")
    while True:
        query = Listen()
        if "hello" in query:
            Speak("Hi! I am Jarvis!")
            
        elif "bye" in query:
            Speak("Hello Bye.")

MainExe()
'''

from Brain.AIBrain import ReplyBrain
from Body.speak import Speak
print(">> Initializing Jarvis....Just a moment Sir..!")
from Body.listen import MicExecution
from Features.Clap import Tester
print(">> Initializing Jarvis....Will be on rather soon..!")



def MainExecution():
    
    Speak("HellO Sir..!")
    Speak("Jarvis here, at your command.")
    
    while True:
        Data = MicExecution()
        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)

def ClapDetect():
    Speak( "Hello")
    query = Tester()
    if "True-Mic" == query:
        print(">>Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass
    
ClapDetect()