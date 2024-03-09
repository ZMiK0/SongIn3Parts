from pydub import AudioSegment
import tkinter
from tkinter import filedialog

print("Welcome to 3 Partes")
tkinter.Tk().withdraw()
path = filedialog.askopenfilename()

forma = int(input("What type of file do you want to use: \n1. mp3 \n2. wav\nAnswer: "))

goodChoice = False
while not goodChoice:
    if forma == 1:
        songName = path.replace(".mp3", "")
        goodChoice = True
    elif forma == 2:
        songName = path.replace(".wav", "")
        goodChoice = True
    else:
        print("Invalid file type")

songName = songName[::-1]
wrongCharacterFound = False
i = 0
while (not wrongCharacterFound and i < len(songName)):
    if songName[i] == "/":
        songName = songName.split("/", 1)
        songName = songName[0]
        wrongCharacterFound = True
    elif songName[i] == "\\":
        songName = songName.split("\\", 1)
        songName = songName[0]
        wrongCharacterFound = True
    else:
        i += 1

songName = songName[::-1]
print("Selected song: " + songName)
partAmmount = int(input("Introduce how many parts do you want: "))

partList = []

for i in range(partAmmount):
    print(f"Now choose the {i + 1}º interval in seconds:")
    st = int(input("Start: "))
    end = int(input("End: "))

    st = st * 1000  # Works in milliseconds
    end = end * 1000
    clip = AudioSegment.from_file(path)
    clip = clip[st:end]
    partList.append(clip)

path = filedialog.askdirectory()

for j in range(len(partList)):
    partList[j].export(path + "/" + songName + f"{j+1}Part.wav", format="wav")

print("DONE :D")
