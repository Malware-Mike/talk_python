import random
import time

from actors import Wizard, Creatures


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------')
    print('    WIZARD GAME APP    ')
    print('---------------------')
    print()


def game_loop():

    creatures = [
        Creatures('Toad', 1),
        Creatures('Tiger', 12),
        Creatures('Bat', 3),
        Creatures('Dragon', 50),
        Creatures('Evil Wizard', 1000)
    ]

    hero = Wizard('Mike', 1000)




    while True:

        active_creature = random.choice(creatures)
        print("A {}  of level {} has appeared from a dark and foggy forest....".format(active_creature.name, active_creature.level))

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
        cmd = cmd.lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover....")
                time.sleep(5)
                print("The Wizard returns healthy!")

        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees: '.format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(
                    c.name, c.level
                ))
        else:
            print("OK, exiting game... bye!")
            break


if __name__ == '__main__':
    main()