import wave, struct, math, random

sampleRate=20000.0 #Hz

obj = wave.open('sound.wav', 'w')
obj.setnchannels(1) # mono
obj.setsampwidth(16)
obj.setframerate(sampleRate)

for i in range(99999):
	value = random.randint(-32767, 32767)
	data=struct.pack('<h', value)
	obj.writeframesraw( data )

obj.close()