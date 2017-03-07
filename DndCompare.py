# D&D 5 Weapon Comparison
import random

# import os
# TO DO
# - clear screen based on OS


class Manger(object):
    def __init__(self):
        self.allweapons = []
        self.menu()

    def buildweapon(self, wpnobj, details):
        wpnobj = weapon(*details)
        self.allweapons.append(wpnobj)
        return (wpnobj)

    def menu(self):
        try:
            nwpns = int(input("How many weapons do you want to compare?\n"))
            print('Will test {} weapons.\n'.format(nwpns))
            self.wlist = []
            for x in range(1, nwpns + 1):
                wpn = "wpn" + str(x)
                self.wlist.append(wpn)
            for y in self.wlist:
                details = input(
                    "Give a name, hit bonus, damage bonus, and dice (as #d#.) \n"
                )
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

        self.results = []

    def damage(self):
        # Return damage
        # print(wpnobj.dice.split('d', 1))
        pass


def combatsimulator(weaponlist, rounds, maxac):
    for w2test in weaponlist:
        print(w2test.wtype)
        testhit = 0
        testmiss = 0
        testdam = 0
        for acs in range(10, maxac + 1):
            testhit = 0
            testmiss = 0
            testdam = 0
            for rnd in range(rounds):
                roll = random.randrange(1, 21) + w2test.hit
                if acs <= roll or roll == 20:
                    testhit = testhit + 1
                    start, end = w2test.dice.split('d', 1)
                    damage = random.randrange(int(start), int(end) +
                                              1) + w2test.dam
                    testdam = testdam + damage
                else:
                    testmiss = testmiss + 1
            try:
                print(
                    "For AC {}, Hits {}, Misses: {}, Total Dam: {}, Avg Dam: {:.2f}".
                    format(acs, testhit, testmiss, testdam,
                           round((testdam / testhit), 2)))
            except:
                print(
                    "For AC {}, Hits {}, Misses: {}, Total Dam: {}, Avg Dam: {:.2f}".
                    format(acs, testhit, testmiss, testdam, 0))
            try:
                w2test.results.append((acs, testhit, testmiss, round(
                    (testdam / testhit), 2)))
            except:
                w2test.results.append((acs, testhit, testmiss, 0))


if __name__ == '__main__':
    manger = Manger()
    combatsimulator(manger.allweapons, 50000, 30)
