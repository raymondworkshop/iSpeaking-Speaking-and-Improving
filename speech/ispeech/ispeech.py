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
from flask_socketio import SocketIO, emit
#from flask_socketio import SocketIO, emit, disconnect

#import scipy.io.wavfile
import numpy as np
from collections import OrderedDict
import sys

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

from ispeech.db import get_db

bp = Blueprint('ispeech', __name__)
#socketio = SocketIO(bp, binary=True)
#socketio = (bp)
#
import speech_recognition as sr
r = sr.Recognizer()

import eng_to_ipa as ipa


@bp.route('/')
def index():
    # fetch from db
    #
    """
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    demo = sr.AudioFile( dir + 'english81.wav')

    txt = get_post(demo)
    _ipa = ipa.convert(txt)
    return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)
    """
    return render_template('ispeech/index.html')


@bp.route('/record', methods = ['GET', 'POST'])
def record():
    txt = ""
    _ipa = "" 

    """
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    demo = sr.AudioFile( dir + 'english81.wav')

    txt = get_post(demo)
    _ipa = ipa.convert(txt)
    """

    #ws.send
    return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)

"""
@bp.route()
def show_entry():

    return render_template()
"""


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
    # source = sr.microphone(sample_rate = 48000, chunk_size=8192)
    txt = ""

    """
    with sr.Microphone() as source:
        print("Calling microphone ...")
        # listen for 2 seconds, and filter out the ambient noise
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something!")
        speech = r.listen(source)
        #
        # record voice
        
        #audio = r.record(source)
    """

    
    
    #dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    #demo = sr.AudioFile( dir + 'english81.wav')

    with demo as source:
        audio = r.record(demo)

    #txt = get_post(demo)

    # recognize speech using Sphinx
    try:
        #txt = r.recognize_google(speech, language = 'hi-IN')
        #txt = r.recognize_google(speech)
        txt = r.recognize_sphinx(speech)
        print('TEXT: ' + txt)
    except sr.UnknownValueError:
        print("Could not recognize the audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))

    #print(txt)  
    return txt

#
@bp.route('/messages', methods=['POST'])
def upload(request):
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    file = dir + 'recording.wav'

    f = open(file, "wb")
    # the actual file is in request.body
    f.write(request.data)
    f.close()

    demo = sr.AudioFile(file)

    txt = get_post(demo)
    _ipa = ipa.convert(txt)

    return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)


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
