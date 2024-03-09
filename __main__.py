from pydub import AudioSegment
import tkinter
from tkinter import filedialog
import song

print("Welcome to 3 Partes")
tkinter.Tk().withdraw()
path = filedialog.askopenfilename()

actualSong = song.Song()

actualSong.setFormat(path)
actualSong.setTitle()

partAmount = int(input("Introduce how many parts do you want: "))

actualSong.addPart(partAmount, path)

path = filedialog.askdirectory()

actualSong.exportParts(path)

print("DONE :D")
