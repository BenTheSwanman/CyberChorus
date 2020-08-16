import pyaudio
import wave
import sys
import time

chunk = 1024
sample_format = pyaudio.paInt16 # 16 bit sample
channels = 1 
fs = 20000 # 20kHz makes max recorded freq 10kHz
seconds = 5

p = pyaudio.PyAudio()

stream = p.open(format=sample_format,
	channels=channels,
	rate=fs,
	frames_per_buffer=chunk,
	input=True,
	output=True)

frames = []

print('Recording...')
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

print('Playing back...')
#for i in range(0, int(fs / chunk * seconds)):
for f in frames:
	stream.write(f)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finishing.')

# Play back recording