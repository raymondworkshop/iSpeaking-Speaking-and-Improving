"""
"""

from server import OpusDecoderWS

import speech_recognition as sr
r = sr.Recognizer()

import eng_to_ipa as ipa

print("filename: ", OpusDecoderWS.filename)

txt = get_post(OpusDecoderWS.filename)
_ipa = ipa.convert(txt)

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


