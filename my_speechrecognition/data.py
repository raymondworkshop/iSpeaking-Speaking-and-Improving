"""
feature engineering - convert data into log-spectrograms
"""

import numpy as np
from scipy.io import wavfile
import scipy
from scipy.signal import stft

import matplotlib.pyplot as plt

import json

DIR = "C:/Users/raymondzhao/myproject/dev.speech/Automatic-Speech-Recognition/LibriSpeech/train-clean-100/" 

filename = DIR + ""
fns = []

SAMPLE_RATE = 16000

def load_data(filename):
        """ Read metadata from a JSON-line file
            (possibly takes long, depending on the filesize)
        Params:
            DIR (str):  Path to a JSON-line file that contains labels and
                paths to the audio files
            partition (str): One of 'train', 'validation' or 'test'
        """
        max_duration=10.0
        audio_paths, durations, texts = [], [], []
        with open(filename) as json_file:
            for line_num, json_line in enumerate(json_file):
                try:
                    spec = json.loads(json_line)
                    if float(spec['duration']) > max_duration:
                        continue
                    audio_paths.append(spec['key'])
                    durations.append(float(spec['duration']))
                    texts.append(spec['text'])
                except Exception as e:
                    # Change to (KeyError, ValueError) or
                    # (KeyError,json.decoder.JSONDecodeError), depending on
                    # json module version
                    print('Error reading line #{}: {}'.format(line_num, json_line))


def read_wav_file(x):
    fs, wav = wavfile.read(x)
    # normalize -> embedding
    wav = wav.astype(np.float32) / np.iinfo(np.int16).max

    return wav

# convert wav to spectrograms using short-time fourier transfor (stft)
def log_spectrogram(wav):
    freqs, times, spec = stft(wav, SAMPLE_RATE, nperseg = 400, noverlap = 240, nfft = 512, 
                              padded = False, boundary = None)
    
    # log spectrogram
    amp = np.log(np.abs(spec)+1e-10)

    return freqs, times, amp


def plot_wav_file(x, maxf=None):
    wav = read_wav_file(x)
    # embeddings
    # maxf = max number of frames
    frames = scipy.arange(wav.size)
    if maxf:
        plt.plot(frames[:maxf], wav[:maxf])
        plt.sticks(scipy.arange(0, maxf, 1*SAMPLE_RATE), scipy.arange(0, maxf/SAMPLE_RATE, 1))
        plt.show()
    else:
        plt.plot(frames, wav)
        plt.xticks(scipy.arange(0, wav.size, 1*SAMPLE_RATE), scipy.arange(0, wav.size/SAMPLE_RATE, 1))
        plt.show()

    # spectrogram
    freqs, times, amp = log_spectrogram(wav)
    if maxf:
        plt.plot(frames[:maxf], wav[:maxf])
        plt.imshow(amp, aspect='auto', origin='lower', 
               extent=[times.min(), times.max(), freqs.min(), freqs.max()])
        plt.show()
    else:
        plt.plot(frames, wav)
        plt.imshow(amp, aspect='auto', origin='lower', 
               extent=[times.min(), times.max(), freqs.min(), freqs.max()])
        plt.show()
    

if __name__ == "__main__":
    filename = DIR + "/103/1240/103-1240-0000.wav"
    plot_wav_file(filename)