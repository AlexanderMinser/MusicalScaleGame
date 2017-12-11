
def printGreeting():
    print("Welcome to scales game")

def buildModes():
    scales = []
    letters = "ABCDEFG"
    modes = ["Ionian",
             "Dorian",
             "Phyrigian",
             "Lydian",
             "Mixolydian",
             "Aolian",
             "Locrian"]
    for letter in letters:
        for mode in modes:
            name = letter[0] + " " + mode
            scales.append(Scale(name, le))

def buildScales():
    modes = buildModes()

def getNextScale():


def runGame():
    while(True):
        scales = buildScales()
        print(getScale())


def main():
    printGreeting()
    runGame()
