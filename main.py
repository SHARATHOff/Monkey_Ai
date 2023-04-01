import speech_recognition
import pyaudio
import time , datetime
import pyttsx3
import pywhatkit
import webbrowser
import wikipedia
import subprocess
import passwordsfile

def Power_off():
    subprocess.run("shutdown /s")

def Wikipedia_info(person):
    try:
        result = wikipedia.summary(person, sentences=2)
        print(result)
        Output_audio(result)
    except:
        print("Unable to")
        Output_audio("Sorry, I couldn't find anything about that")
def Main():
    global input_text
    r = speech_recognition.Recognizer()
    my_mic = speech_recognition.Microphone(device_index=1)
    with my_mic as source:
        audio = r.listen(source)
    input_text = r.recognize_google(audio)
def Output_audio(text):
    engine = pyttsx3.init()
    #engine.say("Hai Sharath Iam Virus Your Assistant")
    engine.say(text)
    engine.runAndWait()
def passwords():
    passwordsfile.Read()

def Check_Time():
    dict_month = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    dict_time = {1:"One   O    clock",2:"Two   O    clock",3:"Three   O    clock",4:"Four   O    clock",5:"Five   O    clock",6:"Six   O    clock",7:"Seven   O    clock",8:"Eight   O    clock",9:"Nine   O    clock",10:"Ten   O    clock",11:"Eleven   O    Clock",12:"Twelve   O    clock",13:"Thirteen   O    clock",14:"Fourteen   O    clock",15:"Fifteen   O    clock",16:"Sixteen   O    clock",17:"Seventeen   O    clock",18:"eightteen   o    clock",19:"nineteen   o    clock",20:"Twenty   o    clock",21:"twentyone   o    clock",22:"TwentyTwo   o    clock",23:"twentyThree   o    clock",24:"TwentyFour   o    clock",25:"twentyFive   o    clock"}
    date_time = datetime.datetime.now().strftime("%H:%M")
   # list_date_time = date_time.split("#")
   # list_date = list_date_time[0].split("-")
    list_time = date_time.split(":")
    if list_time[0] == "1":
        Output_audio(dict_time[1])
    elif list_time[0] == "2":
        Output_audio(dict_time[0])
    elif list_time[0] == "3":
        Output_audio(dict_time[3])
    elif list_time[0] == "4":
        Output_audio(dict_time[4])
    elif list_time[0] == "5":
        Output_audio(dict_time[5])
    elif list_time[0] == "6":
        Output_audio(dict_time[6])
    elif list_time[0] == "7":
        Output_audio(dict_time[7])
    elif list_time[0] == "8":
        Output_audio(dict_time[8])
    elif list_time[0] == "9":
        Output_audio(dict_time[9])
    elif list_time[0] == "10":
        Output_audio(dict_time[10])
    elif list_time[0] == "11":
        Output_audio(dict_time[11])
    elif list_time[0] == "12":
        Output_audio(dict_time[12])
    elif list_time[0] == "13":
        Output_audio(dict_time[13])
    elif list_time[0] == "14":
        Output_audio(dict_time[14])
    elif list_time[0] == "15":
        Output_audio(dict_time[15])
    elif list_time[0] == "16":
        Output_audio(dict_time[16])
    elif list_time[0] == "17":
        Output_audio(dict_time[17])
    elif list_time[0] == "18":
        Output_audio(dict_time[18])
    elif list_time[0] == "19":
        Output_audio(dict_time[19])
    elif list_time[0] == "20":
        Output_audio(dict_time[20])
    elif list_time[0] == "21":
        Output_audio(dict_time[21])
    elif list_time[0] == "22":
        Output_audio(dict_time[22])
    elif list_time[0] == "23":
        Output_audio(dict_time[23])
    else:

        Output_audio("Unknown Error Sharath Please Fix It ...")
    

    
if __name__ == "__main__":
    while True:
        try:
            Main()
            if   "monkey" in input_text.lower():
                print("Yes..")
                Output_audio("Listening Sir...")
                Main()
                print(input_text)
                if  "time" in input_text.lower():
                    Check_Time()
                elif "passwords" in input_text.lower() or "password" in input_text.lower():
                    passwords()
                elif "play" in input_text.lower():
                    link = input_text.lower()
                    if  "favourite" in link :
                        webbrowser.open("https://www.youtube.com/watch?v=4Nx1iXxFUjU")
                    else:
                        link2 = link.split()
                        link2.remove("play")
                        link3 = ""
                        for  i in link2:
                            link3 +=f"{i}+"
                        webbrowser.open(f"https://www.youtube.com/results?search_query={link3}")
                elif  "about" in input_text.lower()   or "who" in input_text.lower():
                    Wikipedia_info(input_text.lower())
                    pywhatkit.search(input_text)
                elif  "open" or "start" in input_text.lower():
                    print("Yes..")
                    if "google" in input_text.lower():
                        webbrowser.open("www.google.com")
                    elif "youtube" in input_text.lower():
                        webbrowser.open("www.youtube.com")
                    elif "facebook" in input_text.lower():
                        webbrowser.open("www.facebook.com")    
                    elif "instagram" in input_text.lower():
                        webbrowser.open("www.instagram.com")
                    elif "programming" in input_text.lower():
                        if "my" in input_text.lower():
                            webbrowser.open("www.github.com/SHARATHOff")
                        else:
                            webbrowser.open("www.github.com")    
                        
                    
                    else:
                        print(input_text)

                elif input_text.lower() in ["about","who","is","about"] :
                    Output_audio("Searching ..")
                    pywhatkit.search(input_text)
                elif "crash" in input_text.lower() or "quit" in input_text.lower() or "exit" in input_text.lower():
                    Output_audio("Good Bai Sir........")
                    break

                
            else:
                continue                
        except speech_recognition.exceptions.UnknownValueError:
            continue
