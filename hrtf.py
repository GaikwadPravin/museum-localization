import scipy.io as scp
import HRIR
import ITD
import soundfile as sf
import numpy
from scipy.io import wavfile
import wave
import pyaudio
from Queue import *

# sound_wave, sample_rate = sf.read('white-noise.wav')


def new_audio(elevation, curr_azimuth):
    sound_wave, sample_rate = sf.read('white-noise.wav')
    zero_padding = [0] * int(sample_rate * 0.2)
    left_hrir = HRIR.HRIR_LEFT_HASH[elevation][curr_azimuth]
    right_hrir = HRIR.HRIR_RIGHT_HASH[elevation][curr_azimuth]
    delay = ITD.ITD[elevation][curr_azimuth]
    zeros_delay = [0] * abs(int(delay))
    if curr_azimuth > 0:
        left_audio = numpy.append(zeros_delay, left_hrir)
        right_audio = numpy.append(right_hrir, zeros_delay)
    # sound is coming from the left side
    elif curr_azimuth < 0:
        left_audio = numpy.append(left_hrir, zeros_delay)
        right_audio = numpy.append(zeros_delay, right_hrir)
    left_convolution = numpy.convolve(left_audio, sound_wave, 'full')
    right_convolution = numpy.convolve(right_audio, sound_wave, 'full')
    LEFT_SOUND = numpy.append(left_convolution, zero_padding)
    RIGHT_SOUND = numpy.append(right_convolution, zero_padding)
    sound_to_play = numpy.array([LEFT_SOUND, RIGHT_SOUND])
    max_left = max(sound_to_play[0])
    max_right = max(sound_to_play[1])
    maximum = max_left if max_left > max_right else max_right
    sound_to_play = sound_to_play / float(maximum)
    sound_to_play = numpy.transpose(sound_to_play)
    sound_to_play = sound_to_play.astype('float32')
    return sound_to_play


# the rate at which we are reading an audio file
CHUNK = 1024
BUFFER = []

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream - rate = bit rate or chunk 8192 increase the buffer size 8192
stream = p.open(format=pyaudio.paFloat32, channels=2, rate=44100, output=True)


def render_real_time(elevation, azimuth):
    print(azimuth)
    # head related t-function - not sure if the chunk is working correctly...
    head_related_func = new_audio(elevation, azimuth)
    data = head_related_func.astype(numpy.float32).tostring()
    stream.write(data, exception_on_underflow=False)


while True:
    isPlaying = raw_input("Are you done rendering sound? [Yes, No] ")
    if isPlaying == "No":
        user_elevation = "Elevation " + raw_input("Enter an elevation: ")
        user_azimuth = input("Enter an azimuth: ")
        render_real_time(user_elevation, user_azimuth)
    else:
        break

stream.stop_stream()
stream.close()
p.terminate()

