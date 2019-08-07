import random
def countScores(num, bank, shuffle = True, maxTries = 3):
    totalPoints = 0
    keys = list(bank.keys())
    if num > len(keys):
        num = len(keys)
    if shuffle:
        random.shuffle(keys)
    for index, key in enumerate(keys):
        if index < num:
            numTries = 0
            response = input('Chinese: {}, English: '.format(key)).strip()
            while response != bank[key]:
                numTries += 1
                response = input('please try again ({} tries left)'.format(maxTries - numTries)).strip()
                if numTries == 3:
                    print('you\'ve tried three times; the answer is {}'.format(bank[key]))
                    totalPoints -= 1
                    break
            totalPoints += 1
    print('Score = %.2f%%' % (totalPoints * 100/ num))