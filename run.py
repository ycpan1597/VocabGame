from wordBank import wordBank
from utils import countScores
if __name__ == '__main__':
    unitRange = input('Welcome to the vocab game! Which units do you want to practice? (ex. 12 - 15) ')
    unitRange = [x.strip() for x in unitRange.split('-')]
    random = input('Would you like to shuffle the words? (y/n)')
    wordBank = wordBank(unitRange[0], unitRange[1])
    numQues = int(input('How many questions do you want? (ex. 15)'))
    countScores(numQues, wordBank.getDict(), shuffle = (random == 'y'))