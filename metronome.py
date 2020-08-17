import wave, struct, math, random

sampleRate=20000.0 #Hz

obj = wave.open('sound.wav', 'w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)

duration = 299999

for i in range(299999):
	value=0
	if(i%sampleRate == 0):
		value = 32767
	data=struct.pack('<h', value)
	obj.writeframesraw( data )

obj.close()