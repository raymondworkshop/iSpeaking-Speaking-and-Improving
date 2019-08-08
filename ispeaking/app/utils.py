import string
import re
import os

from pydub import AudioSegment
import scipy.io.wavfile

UPLOAD_FOLDER = 'C:/Users/raymondzhao/myproject/dev.speech/ispeaking/data/'

def extract_words(s):
    return [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in s.split()]


def gen_wave(input, output):
    fs = 16000
    seconds = 10
    #fs, wave = scipy.io.wavfile.read(input)
    #seconds = wave.size/fs

    sound = AudioSegment.from_file(input, format='mp3')
    sound.export(output, format='wav')


if __name__ == "__main__":
    input = UPLOAD_FOLDER + 'english81.mp3'
    output = gen_wave(input, UPLOAD_FOLDER+'_english81')

