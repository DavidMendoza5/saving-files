import random
from Classes.enemy import Enemy


enemy = Enemy(200, 60)
print("HP: ", enemy.get_hp())

'''
class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

    def getHp(self):
        print("HP is", self.hp)

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(70, 80)
enemy2.getAtk()
enemy2.getHp()
'''

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if(playerhp <= 0):
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Currente HP is", playerhp)

    if(playerhp == 30):
        print("You have low health, you've been teleported to the nearest inn.")
        break
'''
