# -*- coding: utf-8 -*-
"""
a web-based system to improve English (word) pronouncation, and give a marker

@author wenlong

"""
import datetime

from flask import Flask
from flask import render_template, request, redirect

import speech_recognition as sr
r = sr.Recognizer()

#import eng_to_ipa as ipa

app = Flask(__name__)

#


@app.route('/post', methods = ['GET', 'POST'])
def post():
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/'
    demo = sr.AudioFile( dir + 'english81.wav')

    txt = get_post(demo)

    #_ipa = ipa.convert(txt)
    return txt


def get_post(demo):
    #
    #microphone = sr.microphone()
    txt = ""

    with demo as source:
        #print("Calling microphone ...")
        # listen for 2 seconds, and filter out the ambient noise
        #r.adjust_for_ambient_noise(source, duration=2)
        #print("Say something!")
        #audio = r.listen(source)
        #
        # record voice
        
        audio = r.record(source)

    # recognize speech using Sphinx
    try:
        print("TEXT: ")
        txt = r.recognize_sphinx(audio)
        print(txt)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    #print(txt)  
    return txt

#main
if __name__ == '__main__':
    app.run(debug=True)

    #file
    

    #get_post(demo)
    print('Done')
#