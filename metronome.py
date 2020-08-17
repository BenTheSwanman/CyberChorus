import wave, struct, math


class Metronome:
	def __init__(self, bpm): # TODO, 1st note, time signature
		self.bpm = bpm
		self.sampleRate = 20000.0 # Hz
		self.metronomeHz = int(self.sampleRate * (60/self.bpm))
		self.duration = 300000 # in frames

	def writeWavData(self, wav):
		for i in range(self.duration):
			value = -32767
			if(i%self.metronomeHz == 0):
				value = 32676
			data = struct.pack('<h', value)
			wav.writeframes( data )
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