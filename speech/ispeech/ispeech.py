"""
A view function 
* Blueprint 
- organize a group of related views and other code 
* The blueprint is registered with the speech functions 

@wenlong 
"""

import datetime

import functools

from flask import Blueprint, flash, g, render_template, request, redirect, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug import secure_filename
from werkzeug.exceptions import abort


from ispeech.db import get_db

bp = Blueprint('ispeech', __name__)

#
import speech_recognition as sr
r = sr.Recognizer()

#import eng_to_ipa as ipa


@bp.route('/')
def index():
    # fetch from db
    #
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    demo = sr.AudioFile( dir + 'english81.wav')

    txt = get_post(demo)
    return render_template('ispeech/index.html', posts=txt)


@bp.route('/record', methods = ['GET', 'POST'])
def record():

    return 0

@bp.route('/post', methods = ['GET', 'POST'])
def post():
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    demo = sr.AudioFile( dir + 'english81.wav')

    txt = get_post(demo)

    #_ipa = ipa.convert(txt)
    #return txt
    return render_template('base.html', posts=txt)


def get_post(demo, check_author=True):
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


@bp.route('/upload', methods=['POST', 'GET'])
def upload():
    return render_template('upload.html')

@bp.route('/uploader', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


#main
if __name__ == '__main__':
    bp.run(debug=True)

    #file
    
    #get_post(demo)
    print('Done')
#
