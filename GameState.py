class GameState:
    def __init__(self, roomID, players, pointCards, fruitCards, gameProgress, turn):
        self.roomID = roomID
        self.players = players
        self.pointCards = pointCards
        self.fruitCards = fruitCards
        self.gameProgress = gameProgress
        self.turn = turn
    
    def printGameState(self):
        for card in self.pointCards:
            print(card, end = "   ")
        print("\n")
        for i in range(len(self.fruitCards)):
            print(self.fruitCards[i], end = "   ")
            if i == 2:
                print("")
        print("\n")

        for player in self.players:
            player.printPlayer()
    
    def getProgress(self):
        return self.gameProgress
    
    def setProgress(self, gameProgress):
        self.gameProgress = gameProgress

    def getPointCards(self):
        return self.pointCards
    
    def getFruitCards(self):
        return self.fruitCards
    
    def setPointCards(self, pointCards):
        self.pointCards = pointCards
    
    def setFruitCards(self, fruitCards):
        self.fruitCards = fruitCards
    
    def getCurrentPlayer(self):
        return self.players[self.turn]
    
    def nextTurn(self):
        self.turn = (self.turn + 1) % len(self.players)
    
    def printScore(self):
        for player in self.players:
            FCdicts = []
            print(player.getName())
            for otherPlayer in self.players:
                if player != otherPlayer:
                    FCdicts.append(otherPlayer.convertFCtoDict())
            print(str(player.scorePoints(FCdicts)) + "\n")