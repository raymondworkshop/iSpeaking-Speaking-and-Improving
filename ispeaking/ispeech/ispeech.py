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
from werkzeug.utils import secure_filename
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

from scipy.io import wavfile
import math
import numpy as np


UPLOAD_FOLDER = 'C:/Users/raymondzhao/myproject/dev.speech/speech/data/'
ALLOWED_EXTENSIONS = set(['wav'])
#
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/data/'
    demo = sr.AudioFile( dir + 'english81.wav')
    #demo = dir + 'english81.wav'

    txt = get_post(demo)
    #print(txt)
    _ipa = ipa.convert(txt)
    """
    txt = "Hello, World"
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_post(_demo, check_author=True):
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
    #dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/data/'
    #demo = sr.AudioFile( dir + 'english81.wav')
    print("_demo:", _demo)
    """
    rate, data = wavfile.read(_demo)
    #data2 = []
    # Convert `data` to 32 bit integers:
    data2 = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)

    wavfile.write(_demo,rate,data2)
    """

    demo = sr.AudioFile(_demo)

    
    # Convert Audio to Audio Source Format
    #harvard = sr.AudioData(demo, 16000, 2)
    
    with demo as source:
        #r.adjust_for_ambient_noise(source)
        #print("the demo: ", source)
        audio = r.record(source)
    
    #audio = r.record(demo)
    
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

    #dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/data/' 
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
        #_ipa = ipa.convert(txt)
    

    else:
        print("No file")

    return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)


@bp.route('/uploader', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        txt = ""
        _ipa = ""

        if file and allowed_file(file.filename):
            filename = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(filename)

            print('file uploaded successfully')

            txt = get_post(filename)
            print(txt)
            _ipa = ipa.convert(txt)
            print(_ipa)
    
        #ws.send
        return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)

"""
def genHeader(sampleRate, bitsPerSample, channels):
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o

@bp.route('/audio')
def audio():
    # start Recording
    def sound():

        CHUNK = 1024
        sampleRate = 44100
        bitsPerSample = 16
        channels = 2
        wav_header = genHeader(sampleRate, bitsPerSample, channels)

        stream = audio1.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,input_device_index=1,
                        frames_per_buffer=CHUNK)
        print("recording...")
        #frames = []

        while True:
            data = wav_header+stream.read(CHUNK)
            yield(data)

    return Response(sound())
"""
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
