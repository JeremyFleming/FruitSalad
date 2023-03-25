from FruitCard import FruitCard

class PointCard:
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        self.id = id
        self.reverseType = reverseType
        self.pointType = pointType
        self.fruitTypes = fruitTypes
        self.pointValues = pointValues

    # fruitCards is a dictionary with key value pairs of {"fruitName" : # of fruit card}
    # otherPlayerCards is an array of fruitCard dictionaries 
    def scoring(fruitCards, otherPlayerCards):
        pass

    def __str__(self):
        return str(self.id) + " " + self.pointType + " " + self.reverseType + " " + str(self.fruitTypes) + " " + str(self.pointValues)

    def flip(self):
        return FruitCard(self.id, self.reverseType)

class LinearPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)

    def scoring(self, fruitCards, otherPlayerCards):
        score = 0
        for i in range(len(self.fruitTypes)):
            score += self.pointValues[i] * fruitCards[self.fruitTypes[i]]
        return score
    
class DiffSetPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)

    def scoring(self, fruitCards, otherPlayerCards):
        limFactor = 100
        for i in range(len(self.fruitTypes)):
            if fruitCards[self.fruitTypes[i]] < limFactor:
                limFactor = fruitCards[self.fruitTypes[i]] 
        return limFactor * self.pointValues[0]

class SameSetPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)

    def scoring(self, fruitCards, otherPlayerCards):
        return (fruitCards[self.fruitTypes[0]] // len(self.fruitTypes)) * self.pointValues[0]

class MostOfTypePointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [10]

    def scoring(self, fruitCards, otherPlayerCards):
        for i in range(len(otherPlayerCards)):
            if otherPlayerCards[i][self.fruitTypes[0]] > fruitCards[self.fruitTypes[0]]:
                return 0
        return self.pointValues[0]

class FewestOfTypePointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [7]

    def scoring(self, fruitCards, otherPlayerCards):
        for i in range(len(otherPlayerCards)):
            if otherPlayerCards[i][self.fruitTypes[0]] < fruitCards[self.fruitTypes[0]]:
                return 0
        return self.pointValues[0]

class MostFruitPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [10]

    def scoring(self, fruitCards, otherPlayerCards):
        numCards = sum(fruitCards.values())
        for i in range(len(otherPlayerCards)):
            if sum(otherPlayerCards[i].values()) > numCards:
                return 0
        return self.pointValues[0]

class FewestFruitPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [7]

    def scoring(self, fruitCards, otherPlayerCards):
        numCards = sum(fruitCards.values())
        for i in range(len(otherPlayerCards)):
            if sum(otherPlayerCards[i].values()) < numCards:
                return 0
        return self.pointValues[0]

class EvenOddPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [7, 3]

    def scoring(self, fruitCards, otherPlayerCards):
        if (fruitCards[self.fruitTypes[0]] % 2 == 0):
            return self.pointValues[0]
        return self.pointValues[1]


class FruitSaladPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [12]

    def scoring(self, fruitCards, otherPlayerCards):
        limFactor = 100
        for i in range(len(self.fruitTypes)):
            if fruitCards[self.fruitTypes[i]] < limFactor:
                limFactor = fruitCards[self.fruitTypes[i]] 
        return limFactor * self.pointValues[0]


# fruitTypes should be all 6 fruit Types
class MissingTypePointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [5]

    def scoring(self, fruitCards, otherPlayerCards):
        score = 0
        for i in range(len(self.fruitTypes)):
            if fruitCards[self.fruitTypes[i]] == 0:
                score += self.pointValues[0]
        return score

# fruitTypes should be all 6 fruit Types
class AtLeastTwoPointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [3]

    def scoring(self, fruitCards, otherPlayerCards):
        score = 0
        for i in range(len(self.fruitTypes)):
            if fruitCards[self.fruitTypes[i]] >= 2:
                score += self.pointValues[0]
        return score

# fruitTypes should be all 6 fruit Types
class AtLeastThreePointCard(PointCard):
    def __init__(self, id, reverseType, pointType, fruitTypes, pointValues):
        super().__init__(id, reverseType, pointType, fruitTypes, pointValues)
        self.pointValues = [5]

    def scoring(self, fruitCards, otherPlayerCards):
        score = 0
        for i in range(len(self.fruitTypes)):
            if fruitCards[self.fruitTypes[i]] >= 3:
                score += self.pointValues[0]
        return score