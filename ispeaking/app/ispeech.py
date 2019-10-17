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
#from flask_uploads import UploadSet

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

from app.db import get_db

bp = Blueprint('app', __name__)
#socketio = SocketIO(bp, binary=True)
#socketio = (bp)
#
import speech_recognition as sr
r = sr.Recognizer()

import eng_to_ipa as ipa

from scipy.io import wavfile
import math
import numpy as np
#
from . import SpeechModel251


UPLOAD_FOLDER = "C:\\Users\\raymondzhao\\myproject\\dev.speech\\ispeaking\\data\\"
#UPLOAD_FOLDER = '/Users/zhaowenlong/workspace/proj/dev.speech/ispeaking/data/'
ALLOWED_EXTENSIONS = set(['wav'])
#
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from . import utils

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
    org_txt = "You have to take control of your learning. We’ll show you how to do it in a fun and effective way."
    #_ipa = ipa.convert(txt)
    diff_dict = {}
    
    #ws.send
    return render_template('ispeech/record.html', posts=org_txt, diff_dict=diff_dict)

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
        r.adjust_for_ambient_noise(source)
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

datapath = "C:\\Users\\raymondzhao\\myproject\\dev.speech\\ispeaking\\speech_model\\"
#datapath = '/data/raymond/workspace/speech/dataset/'
#datapath = '/Users/zhaowenlong/workspace/proj/dev.speech/ispeaking/speech_model/'
@bp.route('/uploader', methods= ['GET', 'POST'])
def upload_file():
    #  get the selected language from the user
    language = int(request.form['language'])
    print('org_language: ', language)
    # English
    #language = org_language
    """
    db = get_db()
        
    language = db.execute(
            'SELECT language FROM user WHERE username = ?', (username,) ).fetchone()

    print("language: ", language)
    """
    # mandarin
    #language = 2 
    #print('language: ', language)

    if request.method == 'POST':
        # get original txt
        org_txt = request.form['input'].lower()
        org_list = utils.extract_words(org_txt)
        print("Original txt: ", org_txt)

        # speech
        file = request.files['file']
        txt = ""
        _ipa = ""
        speech_list = []
        diff_dict = {}
        if file and allowed_file(file.filename):
            filename = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(filename)

            print('file uploaded successfully')

            if language == 0:
                _txt = get_post(filename)
                speech_list = utils.extract_words(_txt)
                print("Speech txt: ", speech_list)
                
                #_ipa = ipa.convert(_txt)
                #print(_ipa)
                print("org_list:", org_list)
                
                if speech_list:
                    for word, org_ipa, speech_ipa in zip(org_txt, org_list, speech_list):
                        if word not in speech_list:
                            diff_dict[word] = ipa.convert(word)
                            #diff_list.append(word)
            
            elif language == 1:
                #mandarin
                #load the module 
                ms = SpeechModel251.ModelSpeech(datapath)
                ms.LoadModel(datapath + 'speech_model251_e_0_step_266000.model')
                print("filename:", filename)
                speech_list = ms.RecognizeSpeech_FromFile(filename)
                print("speech_list:", speech_list)
                #
                import re
                import pinyin
                org_list = re.findall(r'(\w+?\d)', pinyin.get(org_txt,format="numerical"))
                print("org_list:", org_list)
                #
                """
                if speech_list:
                    for word, speech_ipa, org_ipa in zip(org_txt, speech_list, org_list):
                        print("word: %s, speech_ipa: %s, org_ipa: %s" % (word, speech_ipa, org_ipa))
                        if speech_ipa.lower() != org_ipa.lower():
                            diff_dict[word] = org_ipa
                """

                if speech_list:
                    for word, org_ipa, speech_ipa in zip(org_txt, org_list, speech_list):
                        if org_ipa not in speech_list:
                            print("word: %s, org_ipa: %s" % (word, org_ipa))
                            diff_dict[word] = {speech_ipa: org_ipa}

            else:
                pass


        #txt = " ".join(diff_list)
        print("diff txt: ", diff_dict)
        #ws.send
        return render_template('ispeech/record.html', posts=org_txt, diff_dict=diff_dict)

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
    bp.run(host='127.0.0.1', port='8000', debug=True, threaded=True, ssl_context="adhoc")
    
    #get_post(demo)
    print('Done')
#
