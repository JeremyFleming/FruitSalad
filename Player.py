class Player:
    def __init__(self, name):
        self.name = name
        self.pointCards = []
        self.fruitCards = []
        self.score = 0
    
    def printPlayer(self):
        print(self.name)
        for card in self.pointCards:
            print(card, end = "   ")
        print("")
        for i in range(len(self.fruitCards)):
            print(self.fruitCards[i], end = "   ")
        print("\n")
    
    def convertFCtoDict(self):
        # print(self.fruitCards)
        fruitCardsDict = {"Banana":0, 
                        "Mango":0,
                        "Strawberry":0,
                        "Blueberry":0,
                        "Grape":0,
                        "Pear":0}
        for fruitCard in self.fruitCards:
            if fruitCard != None:
                fruitCardsDict[fruitCard.getFruit()] += 1
        return fruitCardsDict

    def scorePoints(self, otherPlayerCards):
        fruitDict = self.convertFCtoDict()
        for card in self.pointCards:
            self.score += card.scoring(fruitDict, otherPlayerCards)
        return self.score

    def getPointCards(self):
        return self.pointCards

    def removePointCard(self, index):
        del self.pointCards[index]

    def addPointCard(self, pointCard):
        self.pointCards.append(pointCard)

    def addFruitCard(self, fruitCard):
        self.fruitCards.append(fruitCard)
    
    def getName(self):
        return self.name