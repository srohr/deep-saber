import librosa as librosa
import librosa.display
import soundfile as sf
import io

FILE = "/home/steven/deep-saber/api/data/mr-blue-sky/song.egg"

data, samplerate = sf.read(file=FILE)
x , sr = librosa.load(FILE)

print(data)
print(samplerate)
print(x)

mfccs = librosa.feature.mfcc(x, sr=sr)
print(mfccs)
