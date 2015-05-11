#D&D 5 Weapon Compare
#import random
#import os
# TO DO
# - clear screen based on OS

class Manger(object):
    def __init__(self):
        self.allweapons = []
        self.menu()

    def buildweapon(self, wpnobj, details):
        wpnobj = weapon(*details)
        self.allweapons.append(wpnobj)
        return(wpnobj)

    def menu(self):
        try:
            nwpns = int(input("How many weapons do you want to compare?\n"))
            print('Will test {} weapons.\n'.format(nwpns))
            self.wlist = []
            for x in range(1,nwpns+1):
                wpn = "wpn"+ str(x)
                self.wlist.append(wpn)
            for y in self.wlist:
                details = input("Give a name, hit bonus, damage bonus, and dice (as #d#.) \n")
                self.buildweapon(y, details.split(','))
        except:
            ValueError
            print("You've entered and invalid value.")


class weapon(object):
    def __init__(self, wtype, hit, dam, dice):
        self.wtype = wtype
        self.hit = int(hit)
        self.dam = int(dam)
        self.dice = dice

    def attack(target):
        #Return hit roll
        pass
    def damage():
        #Return damage
        #print(wpnobj.dice.split('d', 1))
        pass

def combatsimulator(weaponlist, rounds, maxac):
    for w2test in weaponlist:
        print(w2test)
        for x in range(10, maxac + 1):
            if x <= w2test.hit:
                print('hit')
            else:
                print('miss')
        #for x in range(0,rounds):
            #print(x)
    pass

if __name__ == '__main__':
    manger = Manger()
    combatsimulator(manger.allweapons, 5, 30)
# Concept Test
# weapon1 = weapon('Great Club',7,5,1,8)

# target = 15
# times = 100000
# dcount = 0
# numhits = 0
# misscount = 0

# for n in range(1,times):
#     roll = random.randrange(1, 21) + weapon1.hit
#     if roll >= target:
#         damage = (weapon1.numdice * random.randrange(1, weapon1.sides)) + weapon1.dam
#         dcount = dcount + damage
#         numhits += 1
#     else:
#         misscount += 1

# avgdam = round((dcount / numhits), 3)
# avgmis = round((misscount / times), 3)* 100
# print("Against an AC of {}".format(target))
# print("The {} did an average of {} points of damage.".format(weapon1.wtype, avgdam))
# print("The {} missed {} percent of the time.".format(weapon1.wtype, avgmis))
# print("")
