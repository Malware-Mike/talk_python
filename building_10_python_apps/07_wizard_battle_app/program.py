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

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
        cmd = cmd.lower()
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print("OK, exiting game... bye!")
            break

if __name__ == '__main__':
    main()