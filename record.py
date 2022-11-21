import sounddevice as sd
from scipy.io.wavfile import write
import time

class Recorder:
    def __init__(self) -> None:
        self.fs = 44100
        self.seconds = 10
    
    def record(self):
        self.recording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=1)
    
    def save (self, filename = "timestamp"):
        self.filename = filename
        write(f"{filename}.wav", self.fs, self.recording)