from pydub import AudioSegment
import tkinter
from tkinter import filedialog

print("Welcome to 3 Partes")
#path = str(input("Lets start choosing the song, please, input your directory: "))
tkinter.Tk().withdraw()
path = filedialog.askopenfilename()
songName = path.replace(".wav","")
songName = songName [::-1]
print(songName)
wrongCharacterFound = False
i = 0
while(not wrongCharacterFound and i < len(songName)):
    if songName[i] == "/":
        songName = songName.split("/", 1)
        songName = songName[0]
        wrongCharacterFound = True
    else:
        i+=1
songName = songName[::-1]
print(songName)

print("Now choose the first interval IN SECONDS:")
st1 = int(input("Start: "))
end1 = int(input("End: "))
print("Great, let's choose the second interval:")
st2 = int(input("Start: "))
end2 = int(input("End: "))
print("Good, let's choose the third")
st3 = int(input("Start: "))
end3 = int(input("End: "))
print("NICE")


st1 = st1 * 1000 #Works in milliseconds
end1 = end1 * 1000
st2 = st2 * 1000
end2 = end2 * 1000
st3 = st3 * 1000
end3 = end3 * 1000

firstPart = AudioSegment.from_file(path)
secondPart = AudioSegment.from_file(path)
thirdPart = AudioSegment.from_file(path)

firstPart = firstPart[st1:end1]
secondPart = secondPart[st2:end2]
thirdPart = thirdPart[st3:end3]

path = filedialog.askdirectory()
print(path)


firstPart.export(path + "/" + songName + "1Part.wav", format="wav")
secondPart.export(path + "/" + songName + "2Part.wav", format="wav")
thirdPart.export(path + "/" + songName + "3Part.wav", format="wav")
