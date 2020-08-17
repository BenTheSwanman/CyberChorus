import wave, struct, math
import numpy as np
import matplotlib.pyplot as plt

A4_FREQ = 440
A5_FREQ = 880

class Metronome:
	def __init__(self, bpm): # TODO, 1st note, time signature
		self.bpm = bpm
		self.sampleRate = 20000.0 # Hz
		self.metronomeHz = int(self.sampleRate * (60/self.bpm))
		self.duration = 60000 # in frames

	def tickSine(self):
		sample_size = 10000 #.1s
		sine_wave = []
		for n in range(sample_size):
			sin = np.sin(2*np.pi*A4_FREQ*n/self.sampleRate)
			sine_wave.append(int(sin * 32767))
		return sine_wave

	def writeWavData(self, wav):
		valuesStep = []
		valuesWav = []
		skipFrames = 0
		for i in range(self.duration):
			if skipFrames > 0:
				skipFrames = skipFrames - 1
				continue

			value = -32767
			if(i%self.metronomeHz == 0):
				sine_wave = self.tickSine()
				for value in sine_wave:
					valuesWav.append(value)
					data = struct.pack('<h', value)
					skipFrames = 10000
			valuesWav.append(value)
			data = struct.pack('<h', value)
			# print("data = " + str(data))
			wav.writeframes( data )

		for i in range(self.duration):
			value = -32767
			if(i%self.metronomeHz == 0):
				value=32767
			valuesStep.append(value)

		print("Step length = " + str(len(valuesStep)))
		print("Wav length = " + str(len(valuesWav)))
		plt.plot(valuesStep, 'g*', valuesWav, 'ro')
		plt.show()
		wav.close()

	def createWav(self):
		# Setup metadata and file
		wav = wave.open('metronome.wav', 'w')
		wav.setnchannels(1) # mono
		wav.setsampwidth(2)
		wav.setframerate(self.sampleRate)

		self.writeWavData(wav)

if __name__ == "__main__":
	m = Metronome(100)
	m.createWav()