from pydub import AudioSegment
t1 = 0 * 1000 #Works in milliseconds
t2 = 30 * 1000
newAudio = AudioSegment.from_wav("CancionGiantsVoe.wav")
newAudio = newAudio[t1:t2]
newAudio.export('newSong.wav', format="wav") #Exports to a wav file in the current path.