import random

# this is a test message
# this is a new message   
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return f"{self.strength} of the soldier's strength"

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
    return f"There is no damage to the soldier"
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name

    def battleCry(self):
        return 'Odin Owns You All!!'

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

    def receiveDamage(self, damage):
        # your code here

# Davicente

class War():
    def __init__(self):
        # your code here

    def addViking(self, viking):
        # your code here
    
    def addSaxon(self, saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass


