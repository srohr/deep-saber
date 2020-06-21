import io

import librosa
import soundfile as sf
import zipfile as zf


FILE = "/home/steven/projects/deep-saber/api/data/mr-blue-sky/song.egg"


# data, samplerate = sf.read(FILE)
data, samplerate = librosa.load(FILE)
stft = librosa.stft(data)
stftdb = librosa.amplitude_to_db(abs(stft))


print(samplerate)
print(data)
print(stftdb)
