import pyttsx3
import subprocess
import webbrowser
from PIL import Image

eng = pyttsx3.init()

def speak(command):
    v = eng.getProperty('voices')
    eng.getProperty('rate')
    eng.setProperty('voice',v[0].id)
    eng.setProperty('rate',200)
    eng.say(command)
    eng.runAndWait()

def elon_pic():
    im = Image.open(r'Desktop\D3K9v31XsAAhzF2.jpg')
    im.show()

def david_g():
    im = Image.open(r"Desktop\David goggins.jpg")
    im.show()

def ti():
    import time
    time.sleep(1)

def flux():
    import subprocess
    subprocess.Popen(r"file location")
    speak('opening flux, sir')

def shut():
    import os
    os.system('shutdown /s /t 1')

def whatsapp():
    subprocess.Popen(r"C:\Users\user\AppData\Local\WhatsApp\Application\WhatsApp.exe")
    speak('opening whatsapp, sir')

def key_blaze():
    subprocess.Popen(r"C:\Program Files (x86)\NCH Software\KeyBlaze\keyblaze.exe")
    speak('opening key blaze, sir')

def gmail():
    speak('opening Gmail, sir')
    url = 'https://mail.google.com/mail/u/0/#inbox'
    webbrowser.open_new_tab(url)

def youtube():
    speak('opening youtube, sir')
    url = 'https://www.youtube.com/'
    webbrowser.open_new_tab(url)

def app_o():
    subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    speak('Opening chrome sir')

def brave():
    subprocess.Popen("C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe")
    speak('Opening brave sir')
    ti()
    speak('is there anything else I can help you with')



print('hi I am your AI Desktop Voice Assistant')
import speech_recognition as sr

k = sr.Recognizer()

open = True
while open:
    print('your voice command:')
    try:
        with sr.Microphone() as source:
            k.adjust_for_ambient_noise(source,duration = 0.5)
            audio = k.listen(source)
            text = k.recognize_google(audio)
            text = text.lower()
            print(text)

            if 'hi david' in text:
                speak('Hello sir, hope you are having good day')

            elif 'chrome' in text:
                app_o()

            elif 'whatsapp' in text:
                whatsapp()

            elif 'blaze' in text:
                key_blaze()

            elif 'brave' in text:
                brave()

            elif 'youtube' in text:
                youtube()

            elif 'food' in text:
                flux()

            elif 'gmail' in text:
                gmail()

            elif 'elon musk pic' in text:
                elon_pic()

            elif 'david pic' in text:
                david_g()

            elif 'shutdown' in text:
                speak('shutting down')
                shut()

            elif 'hello' in text:
                print('Yes, sir I am listening')

            elif 'introduce yourself' in text:
                print('Myself david I am here to assist you sir.')

            elif 'close' in text:
                speak('ok sir closing, Thank you for your time')
                open = False

    except sr.RequestError:
        print('No internet')

    except sr.UnknownValueError:
        print('Not audible or speech is not recognized')