from GameState import *
from PointCard import *
from Player import *
from FruitCard import *
import random

# Carrot, Lettuce, Tomato, Cabbage, Pepper, Onion
fruitTypes = ["Banana", "Mango", "Strawberry", "Grape", "Blueberry", "Pear"]

def drawCard(deck):
    if len(deck) == 0:
        return None
    card = deck[0]
    del deck[0]
    return card


def makeDeck(players): 
    deck = []
    for i in range(len(fruitTypes)):
        deck.append(LinearPointCard((i*18 + 0), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6]], [2]))
        deck.append(LinearPointCard((i*18 + 1), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+4)%6], fruitTypes[(i+5)%6]], [4, -2, -2]))
        deck.append(LinearPointCard((i*18 + 2), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+1)%6], fruitTypes[i]], [3, -1, -1]))
        deck.append(LinearPointCard((i*18 + 3), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+1)%6], fruitTypes[i]], [2, 1, -2]))
        deck.append(LinearPointCard((i*18 + 4), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+4)%6]], [1, 1]))
        deck.append(LinearPointCard((i*18 + 5), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+2)%6], fruitTypes[(i+1)%6]], [2, 2, -4]))
        deck.append(LinearPointCard((i*18 + 6), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+2)%6]], [3, -2]))
        deck.append(LinearPointCard((i*18 + 7), fruitTypes[i], "LINEAR", [fruitTypes[(i+3)%6], fruitTypes[(i+1)%6]], [1, 1]))
        deck.append(SameSetPointCard((i*18 + 8), fruitTypes[i], "SAME_SET", [fruitTypes[(i+3)%6], fruitTypes[(i+3)%6]], [5]))
        deck.append(SameSetPointCard((i*18 + 9), fruitTypes[i], "SAME_SET", [fruitTypes[(i+3)%6], fruitTypes[(i+3)%6], fruitTypes[(i+3)%6]], [8]))
        if i == 2 or i == 4 or i == 5:
            deck.append(DiffSetPointCard((i*18 + 10), fruitTypes[i], "DIFF_SET", [fruitTypes[(i+5)%6], fruitTypes[(i+4)%6]], [5]))
            deck.append(DiffSetPointCard((i*18 + 11), fruitTypes[i], "DIFF_SET", [fruitTypes[(i+2)%6], fruitTypes[(i+1)%6]], [5]))
        else:
            deck.append(DiffSetPointCard((i*18 + 10), fruitTypes[i], "DIFF_SET", [fruitTypes[(i+4)%6], fruitTypes[(i+2)%6]], [5]))
            deck.append(DiffSetPointCard((i*18 + 11), fruitTypes[i], "DIFF_SET", [fruitTypes[(i+5)%6], fruitTypes[(i+1)%6]], [5]))
        deck.append(DiffSetPointCard((i*18 + 12), fruitTypes[i], "DIFF_SET", [fruitTypes[(i)%6], fruitTypes[(i+3)%6], fruitTypes[(i+5)%6]], [8]))
        deck.append(DiffSetPointCard((i*18 + 13), fruitTypes[i], "DIFF_SET", [fruitTypes[(i+4)%6], fruitTypes[(i+3)%6], fruitTypes[(i+2)%6]], [8]))
        deck.append(EvenOddPointCard((i*18 + 14), fruitTypes[i], "EVEN_ODD", [fruitTypes[(i+3)%6]], [7, 3]))
        deck.append(MostOfTypePointCard((i*18 + 15), fruitTypes[i], "MOST_OF_TYPE", [fruitTypes[(i+3)%6]], [10]))
        deck.append(FewestOfTypePointCard((i*18 + 16), fruitTypes[i], "FEWEST_OF_TYPE", [fruitTypes[(i+3)%6]], [7]))
    deck.insert(17, AtLeastThreePointCard(17, fruitTypes[0], "AT_LEAST_THREE", fruitTypes, [5]))
    deck.insert(35, FewestFruitPointCard(35, fruitTypes[1], "FEWEST_FRUIT", fruitTypes, [7]))
    deck.insert(53, FruitSaladPointCard(53, fruitTypes[2], "FRUIT_SALAD", fruitTypes, [12]))
    deck.insert(71, MissingTypePointCard(71, fruitTypes[3], "MISSING_TYPE", fruitTypes, [5]))
    deck.insert(89, FewestFruitPointCard(89, fruitTypes[4], "MOST_FRUIT", fruitTypes, [10]))
    deck.insert(107, AtLeastThreePointCard(107, fruitTypes[5], "AT_LEAST_TWO", fruitTypes, [3]))
    if players == 6:
        random.shuffle(deck)
        return deck
    finalDeck = []
    for i in range(len(fruitTypes)):
        finalDeck += random.sample(deck[i*18:((i+1)*18-1)], k=players*3)
    random.shuffle(finalDeck)
    return finalDeck

def main():
    # createGame()
    # roomID = "placeholder"
    # pointCards = ["LINEAR_BANANA", "EVEN_ODD_MANGO", "SET_TRIPLE_MANGO"]
    # fruitCards = ["BANANA", "BANANA", "STRAWBERRY", "GRAPE", "PEAR", "BLUEBERRY"]
    # players = ["Jeremy", "Ben", "Christian", "David"]
    # gs = "IN_PROGRESS"
    # turn = 0
    # gameState = GameState(roomID, pointCards, fruitCards, players, gs, turn)

    # jeremysPointCards = [FruitSaladPointCard("", "Mango", "", fruitTypes, [5])]
    # jeremysFruitCards = [FruitCard("", "Mango"), FruitCard("", "Mango"), FruitCard("", "Mango"), FruitCard("", "Banana"), FruitCard("", "Blueberry"), FruitCard("", "Strawberry"), FruitCard("", "Pear"), FruitCard("", "Grape")]

    # otherFruitCards = [{"Banana":0, 
    #                     "Mango":5,
    #                     "Strawberry":0,
    #                     "Blueberry":0,
    #                     "Grape":0,
    #                     "Pear":-1}, 
    #                     {"Banana":0, 
    #                     "Mango":3,
    #                     "Strawberry":3,
    #                     "Blueberry":-2,
    #                     "Grape":0,
    #                     "Pear":0}]
    # jeremy = Player("Jeremy", jeremysPointCards, jeremysFruitCards)
    # print(jeremy.scorePoints(otherFruitCards))
    deck = makeDeck(4)
    pointCards = deck[0:3]
    del deck[0:3]
    fruitCards = []
    for i in range(6):
        fruitCards.append(deck[i].flip())
    del deck[0:6]
    # del deck [1:-1]
    p1 = Player("Jeremy")
    p2 = Player("Christian")
    p3 = Player("Ben")
    p4 = Player("David")
    gameState = GameState("", [p1, p2], pointCards, fruitCards, "IN_PROGRESS", 0)
    
    while (gameState.getProgress() == "IN_PROGRESS"):
        gameState.printGameState()
        curPlayer = gameState.getCurrentPlayer()

        choice = "F"
        allNone = True
        for card in gameState.getPointCards():
            if card != None:
                allNone = False
                break
        fruitCardNoneCount = 0
        for card in gameState.getFruitCards():
            if card == None:
                fruitCardNoneCount += 1

        if not allNone:
            choice = input("Would you like a [P]oint Card or 2 [F]ruit Cards? > ")
        if choice == "P":
            cardIndex = (int) (input("Choose your card! > ")) - 1
            curPlayer.addPointCard(pointCards[cardIndex])
            pointCards[cardIndex] = drawCard(deck)
        else:
            cardIndex1 = (int) (input("Choose your card! > ")) - 1
            curPlayer.addFruitCard(fruitCards[cardIndex1])
            if fruitCardNoneCount != 5:
                cardIndex2 = (int) (input("Choose another card! > ")) - 1
            curPlayer.addFruitCard(fruitCards[cardIndex2])
            if pointCards[cardIndex1 % 3] != None:
                fruitCards[cardIndex1] = pointCards[cardIndex1 % 3].flip()
            else:
                fruitCards[cardIndex1] = None
                for i in range(len(pointCards)):
                    if pointCards[i] != None:
                        fruitCards[cardIndex1] = pointCards[i].flip()
                        pointCards[i] = None
                        break
            pointCards[cardIndex1 % 3] = drawCard(deck)
            if fruitCardNoneCount != 5:
                if pointCards[cardIndex2 % 3] != None:
                    fruitCards[cardIndex2] = pointCards[cardIndex2 % 3].flip()
                else:
                    fruitCards[cardIndex2] = None
                    for i in range(len(pointCards)):
                        if pointCards[i] != None:
                            fruitCards[cardIndex2] = pointCards[i].flip()
                            pointCards[i] = None
                            break
        
        if fruitCardNoneCount >= 4:
            gameState.setProgress("GAME_OVER")

        gameState.setFruitCards(fruitCards)
        gameState.setPointCards(pointCards)
        
        if len(curPlayer.getPointCards()) != 0:
            choice = input("Would you like to flip a point card? [Y] or [N] > ")
            if choice == "Y":
                index = (int) (input("Choose your card! > ")) - 1
                curPlayer.addFruitCard(curPlayer.getPointCards()[index].flip())
                curPlayer.removePointCard(index)
        
        gameState.nextTurn()

    gameState.printGameState()
    gameState.printScore()

    # for card in deck:
    #     print(card)
    # print("")
    


if __name__ == '__main__':
    main()