import threading
import speech_recognition as sr
from datetime import datetime
from googlesearch import search
from tkinter import *
import tkinter
import pyttsx3

def voiceAssistant():
    voice= pyttsx3.init()
    recognizer = sr.Recognizer()
    text=""
    while(text!="exit"):
        with sr.Microphone() as source: 
            print("Speak something...")
            output_text.set("Speak something..."+"\n")
            voice.say("Speak something...")
            voice.runAndWait()
            try:
                audio_data = recognizer.listen(source, timeout=5) 
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected after 5 seconds")
                output_text.set("Timeout"+"\n")
                voice.say("Timeout")
                voice.runAndWait()


        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            output_text.set("You said: "+text+"\n")
            if text=="hello" or text=="hi":
                response = "Hi, I am voice Assistant"
                print("System:", response)
                output_text.set("System: "+response+"\n")
                voice.say("Hi, I am voice Assistant")
                voice.runAndWait()
                break
            elif text=="tell me time" or text=="time":
                time = datetime.now().time()
                print(time)
                output_text.set( str(time)+"\n")
                voice.say(time)
                voice.runAndWait()
                break
            elif text=="tell me date" or text=="day" or text=="date":
                date = datetime.now().date()
                print(date)
                output_text.set( str(date)+"\n")
                voice.say(date)
                voice.runAndWait()
                break
            elif text.startswith("search for"):
                query = text[11:]
                for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                    print(j)
                    output_text.set( output_text.get()+j +"\n")
                break
            elif text=="good bye" or text=="bye":
                response = "feel free to reach out any time! Good luck"
                print("System:", response)
                output_text.set( "System: " + response + "\n")
                voice.say(response)
                voice.runAndWait()
                break
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            output_text.set("Sorry, could not understand audio."+"\n")
            voice.say("Sorry, could not understand audio.")
            voice.runAndWait()
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")
            output_text.set("Error: Could not request results from Google Speech Recognition service;"+"\n")
            voice.say("Error: Could not request results from Google Speech Recognition service;")
            voice.runAndWait()
        root.after(100, update_gui)
def update_gui():
    output_label.update_idletasks()
def start_voiceAssistant_thread():
    voice_thread = threading.Thread(target=voiceAssistant)
    voice_thread.start()
root = Tk()
root.title("Voice Assistant" )
root.configure(bg="#000926")
root.state('zoomed')

Label(root,text='Voice Chat',font=('Verdana', 20),bg="#000926",fg="white").pack(side=TOP, pady=10)

photo = PhotoImage(file=r"D:\aditya\project1\mic.png")
photoimage = photo.subsample(7, 7)

Button(root,image=photoimage,activebackground="#000926",width=100,height=100,borderwidth=0,relief=FLAT,bg="#000926",command=start_voiceAssistant_thread).pack()

output_text = tkinter.StringVar()
output_label = tkinter.Label(root, textvariable=output_text, wraplength=380,font=('Verdana', 15), justify="left",bg="#000926",fg="white")
output_label.pack(side=TOP,pady=20)

root.mainloop()
