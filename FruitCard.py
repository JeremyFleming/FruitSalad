class FruitCard:
    def __init__(self, id, fruitType):
        self.id = id
        self.fruitType = fruitType
    
    def getFruit(self):
        return self.fruitType
    
    def __str__(self):
        return str(self.id) + " " + self.fruitType