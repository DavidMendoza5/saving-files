import random

class Bcolors:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]
    
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    
    def generate_spell_damage(self, i):
        mgl = self.magic[i]["Dmg"] - 5
        mgh = self.magic[i]["Dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, Dmg):
        self.hp -= Dmg
        if(self.hp < 0):
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["Name"]

    def get_spell_cost(self, i):
        return self.magic[i]["Cost"]

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["Name"], "(Cost:", str(spell["Cost"]) + ")")
            i += 1
        