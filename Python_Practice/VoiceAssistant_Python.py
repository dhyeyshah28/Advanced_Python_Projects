#!/usr/bin/env python
# coding: utf-8

# ## Personal Voice Assistant - Python Project

# ### Importing Libraries

# In[56]:


import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import nltk


# ### Setting up TTS Engine

# In[2]:


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices)


# In[71]:


engine.setProperty('voice', voices[1].id)
print(voices[1].id)


# ### Main Project Code:
# Naming of my Voice Assistant: June (Uses inbuilt Microsoft sapi5 voices - Zira)

# In[72]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
        print("Good Morning Sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening")
        print("Good Evening Sir")
    print("My Name is June, How can i help you ?")
    speak("My Name is June, How can i help you ?")
    
def listenCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")
    except Exception as e:
        print("Please say that again...")
        return "None"
    return query


if __name__ == '__main__':
    greetMe()
    while True:
        query = listenCommand().lower()
        
        if 'hey june' in query:
            speak('Yes sir, what can i do for you')
            
        elif 'who is' in query:
            keyword = query.replace('who is', '')
            #keyword = keyword.replace('who is', '')
            while True:
                print(f'Do you want me to search about {keyword}')
                speak(f'Do you want me to search about {keyword}')
                query_sec = listenCommand().lower()
                if 'yes' in query_sec:
                    print('Should I search up Google or Read from Wikipedia?')
                    speak('Do you want me to look it up on google or read it for you from Wikipedia?')
                    query_third = listenCommand().lower()
                    if 'google' in query_third:
                        speak("Okay, here are your Google results sir")
                        webbrowser.open(f'www.google.com/search?q={keyword}')
                        break
                    else:
                        search_result = wikipedia.summary(keyword, sentences=2)
                        speak('Heres what i found online, According to Wikipedia')
                        print(search_result)
                        speak(search_result)
                        break
                else:
                    print('Oh, I am sorry, can you please say what do you want to search again?')
                    speak('Oh, I am sorry, can you please say what do you want to search again?')
                    break
        
        elif 'temperature' in query:
            temp_loc = nltk.word_tokenize(query)
            temp = webbrowser.open(f'https://duckduckgo.com/?q=temperature+in+{temp_loc[-1]}+today&t=brave&ia=weather')
            speak(f"Showing results for the current Temperature in {temp_loc[-1]}")
        
        elif 'open' in query:
            web_key = query.replace('open', '')
            final_web_key = web_key.replace(' ', '')
            speak(f'Okay, opening {final_web_key}')
            print(f'Okay, opening {final_web_key}')
            webbrowser.open(f'www.{final_web_key}.com')
        
        elif 'play music' in query:
            speak("Playing your playlist")
            music_folder = "C:\\Users\\HP\\Desktop\\music"
            songs = os.listdir(music_folder)
            curr_song = os.startfile(os.path.join(music_folder, songs[0]))
            print(f"Playing {curr_song}")
        elif 'stop music' in query:
            os.abort(curr_song)
        
        elif 'the time' in query:
            curr_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time right now is {curr_time} Sir")
            speak(f"The exact time right now is {curr_time} Sir")
            
        elif 'shutdown' in query:
            print('Okay, Shutting down, do call me back if you need help with anything else. Have a great day sir.')
            speak('Okay, Shutting down, do call me back if you need help with anything else. Have a great day sir.')
            break
            

