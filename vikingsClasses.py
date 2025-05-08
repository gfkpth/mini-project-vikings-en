import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength 

    def receiveDamage(self, damage):
        if self.health > damage:
            self.health -= damage
        
        else:
            self.health = 0


        
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name

    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        if self.health>damage:
            self.health -= damage
            return f'{self.name} has received {damage} points of damage'
        else:
            self.health = 0
            return f'{self.name} has died in act of combat'

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        pass
        

    def receiveDamage(self, damage):
        # your code here
        pass

# Davicente

class War():
    def __init__(self):
        # your code here
        pass

    def addViking(self, viking):
        # your code here
        pass
    
    def addSaxon(self, saxon):
        # your code here
        pass
    
    def vikingAttack(self):
        # your code here
        pass
    
    def saxonAttack(self):
        # your code here
        pass

    def showStatus(self):
        # your code here
        pass


