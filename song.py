from pydub import AudioSegment

class Song(object):
    title = ""
    partList = []

    def setFormat(self, path):
        goodChoice = False
        while not goodChoice:
            forma = int(input("What type of file do you want to use: \n1. mp3 \n2. wav\nAnswer: "))
            if forma == 1:
                self.title = path.replace(".mp3", "")
                goodChoice = True
            elif forma == 2:
                self.title = path.replace(".wav", "")
                goodChoice = True
            else:
                print("Invalid file type")

    def setTitle(self):
        self.title = self.title[::-1]
        wrongCharacterFound = False
        i = 0
        while (not wrongCharacterFound and i < len(self.title)):
            if self.title[i] == "/":
                self.title = self.title.split("/", 1)
                self.title = self.title[0]
                wrongCharacterFound = True
            elif self.title[i] == "\\":
                self.title = self.title.split("\\", 1)
                self.title = self.title[0]
                wrongCharacterFound = True
            else:
                i += 1

        self.title = self.title[::-1]
        return print("Selected song: " + self.title)

    def getName(self):
        return self.title

    def addPart(self,partAmount,path):
        for i in range(partAmount):
            print(f"Now choose the {i + 1}º interval in seconds:")
            st = int(input("Start: "))
            end = int(input("End: "))

            st = st * 1000  # Works in milliseconds
            end = end * 1000
            clip = AudioSegment.from_file(path)
            clip = clip[st:end]
            self.partList.append(clip)

    def exportParts(self, path):
        for j in range(len(self.partList)):
            self.partList[j].export(path + "/" + self.title + f"{j + 1}Part.wav", format="wav")