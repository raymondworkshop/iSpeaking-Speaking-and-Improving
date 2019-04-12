"""
A view function 
* Blueprint 
- organize a group of related views and other code 
* The blueprint is registered with the speech functions 

@wenlong 
"""
import os

import datetime

import functools

from flask import Blueprint, flash, g, render_template, request, redirect, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug import secure_filename
from werkzeug.exceptions import abort
#from flask_socketio import SocketIO, emit
#from flask_socketio import SocketIO, emit, disconnect
from werkzeug.serving import run_simple

#import scipy.io.wavfile
import numpy as np
from collections import OrderedDict
import sys
#from flask_sslify import SSLify
#from OpenSSL import SSL
#import ssl
import subprocess


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
#async_mode = None

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

    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/data/'
    demo = sr.AudioFile( dir + 'english81.wav')
    #demo = dir + 'english81.wav'

    txt = get_post(demo)
    #print(txt)
    _ipa = ipa.convert(txt)
    
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
    #demo = dir + 'english81.wav'

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
    
    with demo as source:
        #r.adjust_for_ambient_noise(source, duration=2)
        print("demo:", demo)
        audio = r.record(demo)
    
    #dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    #demo = sr.AudioFile( dir + 'english81.wav')

    #txt = get_post(demo)

    # recognize speech using Sphinx
    try:
        #txt = r.recognize_google(speech, language = 'hi-IN')
        #txt = r.recognize_google(speech)
        txt = r.recognize_sphinx(audio)
        print('TEXT: ' + txt)
    except sr.UnknownValueError:
        print("Could not recognize the audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))

    #print(txt)  
    return txt


@bp.route('/uploads', methods=['POST'])
def save_audio():
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    #demo = sr.AudioFile( dir + 'english81.wav')

    rawAudio = request.get_data()
    audioFile = open('RecordedFile.wav', 'wb')
    audioFile.write(rawAudio)
    audioFile.close()

    return speech_to_text()


def speech_to_text():
    subprocess.run('python3 speechtotext.py', shell=True)
    inFile = open(PATH + 'result/result.txt', 'r')
    transcript = ''
    for line in inFile:
        transcript += line
    print(transcript)
    return transcript

#
@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    txt = ""
    _ipa = ""

    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    #file = dir + 'recording.wav'
    file = dir + 'english81.wav'

    exists = os.path.isfile(file)

    if exists:
        """
        f = open(file, "wb")
        # the actual file is in request.body
        f.write(request.data)
        f.close()

        demo = sr.AudioFile(file)
        """
        demo = file

        txt = get_post(demo)
        _ipa = ipa.convert(txt)
    

    else:
        print("No file")

    return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)


@bp.route('/uploader', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

#main
if __name__ == '__main__':
    """
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations("ca.crt")
    context.load_cert_chain("server.crt", "server.key")
    serving.run_simple("0.0.0.0", 5000, bp, ssl_context="adhoc",debug=True)
    """
    #dir = 'C:/Users/raymondzhao/myproject/dev.speech/'
    #ssl_context=(dir + 'ssl.cert', dir + 'ssl.key')
    #context.load_verify_locations("ca.crt")
    #bp.run(host='127.0.0.1', port='80', debug=True, threaded=True,ssl_context=context)

    #run_simple('localhost', 4000, bp, debug=True, threaded=True, ssl_context=ssl_context)
    #bp.run(host='127.0.0.1', port=80, debug=True, threaded=True,ssl_context=context)
    #file

    #bp.run(ssl_context='adhoc', port='80', debug=True, threaded=True)
    bp.run(host='127.0.0.1', port='4000', debug=True, threaded=True, ssl_context="adhoc")
    
    #get_post(demo)
    print('Done')
#
