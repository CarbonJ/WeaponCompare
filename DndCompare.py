#D&D 5 Weapon Compare
#import random

def menu():
    try:
        nwpns = int(input("How many weapons do you want to compare?\n"))
        print('Will test {} weapons.\n'.format(nwpns))
        wlist = []
        for x in range(1,nwpns+1):
            wpn = "wpn"+ str(x)
            print(wpn)
            wlist.append(wpn)
            print(wlist)
    except:
        ValueError
        print("You've entered and invalid value.")
        menu()



def weaponrolls():
    pass


class weapon():
    def __init__(self, wtype, hit, dam, numdice, sides):
        self.wtype = wtype
        self.hit = hit
        self.dam = dam
        self.numdice = numdice
        self.sides = sides

    def attack():
        #Return hit roll
        pass
    def damage():
        pass


menu()

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
