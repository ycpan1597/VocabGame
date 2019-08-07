import csv
class wordBank():
    def __init__(self, startUnit, endUnit):
        self.wordDict = {}
        vocabRange = range(int(startUnit), int(endUnit) + 1)
        for i in vocabRange:
            with open(str(i) + '.csv') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    if row[0]:
                        self.wordDict[row[0].strip()] = row[1].strip()
    def getDict(self):
        return self.wordDict