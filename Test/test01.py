gameList = []
gaming = True
previousWord = ''

class words:
    def __init__(self) -> None:
        pass
    def next(self, word):
        global gaming,gameList,previousWord
        gaming = True
        self.word = word
        if(previousWord != ''):
            gaming = True if(self.word[0:2].lower() == previousWord[-2:].lower()) else False
        for i in gameList:
            if(self.word == i):
                gaming = False
        if(gaming):
            gameList.append(self.word)
            print("'", self.word,"'", ' -> ', gameList, sep="")  
        else:
            print("'", self.word,"'", ' -> ', 'game over', sep="")
        previousWord = self.word
        pass
    def reset(self):
        global gaming,gameList,previousWord
        gaming = True
        gameList.clear()
        print('game restarted')
        pass
    def end(self, list1, temp):
        global gaming,gameList,previousWord
        gaming = False
        self.list1 = list1
        self.temp = temp
        if(self.list1[0] != 'X'):
            print("'", self.temp,"'", ' is Invalid Input !!!', sep="")
        pass


print('*** TorKham HanSaa ***')
wordZ = words()
s = input('Enter Input : ').split(',')
for i in range(0,len(s)):
    temp = s[i]
    s[i] = s[i].split(' ')
    if(gaming):
        if(s[i][0] == 'P'):
            wordZ.next(s[i][1])
        elif(s[i][0] == 'R'):
            wordZ.reset()
        else:
            wordZ.end(s[i], temp)