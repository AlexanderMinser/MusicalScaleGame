

class Scale():

    def __init__(self, name, letters):
        self.letters = letters
        self.name = name

    def __str__(self):
        return self.name + "\n" + self.getLetters()

    def setLetters(self, scale):
        self.scale = scale

    def getLetters(self):
        return self.letters

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
