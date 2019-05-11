# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:56:07 2019

@author: om8007
"""

import speech_recognition as sr

AUDIO_FILE = ("rec1.wav")                 #audio src file in wav 

r = sr.Recognizer()                       #initialisation

with sr.AudioFile(AUDIO_FILE) as src:
    audio = r.record(src)                 #reads audio file
    
try:
    print("File reads: "+ r.recognize_google(audio))   #output the result
except sr.UnknownValueError:
    print("GSR couldn't understand audio")
except sr.RequestError:
    print("Couldn't get results from GSR")