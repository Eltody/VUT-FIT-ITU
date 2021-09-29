import random


# Pravidla hry Uno: https://www.navod-k-obsluze.cz/upload/karetni-hra-uno-navod-k-obsluze.pdf

def Main():
    cards_in_stack = ['redZero', 'redOne', 'redTwo', 'redThree', 'redFour', 'redFive', 'redSix', 'redSeven', 'redEight', 'redNine', 'second_redOne', 'second_redTwo', 'second_redThree', 'second_redFour', 'second_redFive', 'second_redSix', 'second_redSeven', 'second_redEight', 'second_redNine', 'redSkipCard', 'second_redSkipCard', 'redReverseCard', 'second_redReverseCard', 'redDraw2Card', 'second_redDraw2Card',
                        'yellowZero', 'yellowOne', 'yellowTwo', 'yellowThree', 'yellowFour', 'yellowFive', 'yellowSix', 'yellowSeven', 'yellowEight', 'yellowNine', 'second_yellowOne', 'second_yellowTwo', 'second_yellowThree', 'second_yellowFour', 'second_yellowFive', 'second_yellowSix', 'second_yellowSeven', 'second_yellowEight', 'second_yellowNine', 'yellowSkipCard', 'second_yellowSkipCard', 'yellowReverseCard', 'second_redReverseCard', 'redDraw2Card', 'second_redDraw2Card',
                        'greenZero', 'greenOne', 'greenTwo', 'greenThree', 'greenFour', 'greenFive', 'greenSix', 'greenSeven', 'greenEight', 'greenNine', 'second_greenOne', 'second_greenTwo', 'second_greenThree', 'second_greenFour', 'second_greenFive', 'second_greenSix', 'second_greenSeven', 'second_greenEight', 'second_greenNine', 'greenSkipCard', 'second_greenSkipCard', 'greenReverseCard', 'second_greenReverseCard', 'greenDraw2Card', 'second_greenDraw2Card',
                        'blueZero', 'blueOne', 'blueTwo', 'blueThree', 'blueFour', 'blueFive', 'blueSix', 'blueSeven', 'blueEight', 'blueNine', 'second_blueOne', 'second_blueTwo', 'second_blueThree', 'second_blueFour', 'second_blueFive', 'second_blueSix', 'second_blueSeven', 'second_blueEight', 'second_blueNine', 'blueSkipCard', 'second_blueSkipCard', 'blueReverseCard', 'second_blueReverseCard', 'blueDraw2Card', 'second_blueDraw2Card',
                        'wildCard', 'second_wildCard', 'third_wildCard', 'fourth_wildCard', 'wildDraw4Card', 'second_wildDraw4Card', 'third_wildDraw4Card', 'fourth_wildDraw4Card']
    # zamiesanie kariet na zaciatku hry
    random.shuffle(cards_in_stack)
    playerCards = []
    botCards = []
    second_botCards = []
    # Game mode: one player, one pc bot
    numberOfPlayers = 2
    # Game mode: one player, two pc bots
    # numberOfPlayers = 3

    # rozdanie 7 kariet hracovi a botovi, pripadne druhemu botovi a odstranenie kariet z balicku
    if numberOfPlayers == 2 or numberOfPlayers == 3:
        print('cards_in_stack:', len(cards_in_stack))
        for i in range(7):
            cardToRemoveFromStack = random.choice(cards_in_stack)
            playerCards.append(cardToRemoveFromStack)
            cards_in_stack.remove(cardToRemoveFromStack)
        print('playerCards:', playerCards)
        print('cards_in_stack:', len(cards_in_stack))

        for i in range(7):
            cardToRemoveFromStack = random.choice(cards_in_stack)
            botCards.append(cardToRemoveFromStack)
            cards_in_stack.remove(cardToRemoveFromStack)
        print('botCards:', botCards)
        print('cards_in_stack:', len(cards_in_stack))
        if numberOfPlayers == 3:
            for i in range(7):
                cardToRemoveFromStack = random.choice(cards_in_stack)
                second_botCards.append(cardToRemoveFromStack)
                cards_in_stack.remove(cardToRemoveFromStack)
            print('second_botCards:', second_botCards)
            print('cards_in_stack:', len(cards_in_stack))

    # Otocenie vrchnej karty z balicku licem nahoru a polozenie na stol ako zaklad odhadzovacej hromadky, na kt. budu hraci odhadzovat svoje karty
    thrownAwayCards = cards_in_stack[-1]
    cardToRemoveFromStack = cards_in_stack[-1]
    cards_in_stack.remove(cardToRemoveFromStack)
    print('Vrchna karta na odhadzovacej hromadke:', thrownAwayCards)
    print('cards_in_stack:', len(cards_in_stack))

    # volanie funkcii na tah hraca a bota
    cards_in_stack, thrownAwayCards, playerCards = playerMove(cards_in_stack, thrownAwayCards, playerCards)
    cards_in_stack, thrownAwayCards, botCards = botMove(cards_in_stack, thrownAwayCards, botCards)
    exit(0) # uspesne ukoncenie programu

def playerMove(cards_in_stack, thrownAwayCards, playerCards):
    # na tahu je hrac, na odhadzovaciu hromadku moze odhodit len kartu z ruky, ktora ma rovnaku farbu alebo ciselnu hodnotu ako vrchna karta na odhadzovacej hromadke
    # TODO urobit to aj pre rovnaky symbol
    if playerCards != 0:
        allowedPlayerCardsToThrowAway = []      # karty, ktore moze hrac odhodit na odhadzovaciu hromadku

        # zistenie farby karty na odhadzovacej hromadke
        if 'red' in thrownAwayCards:
            colorOfThrownAwayCard = 'red'
        elif 'yellow' in thrownAwayCards:
            colorOfThrownAwayCard = 'yellow'
        elif 'green' in thrownAwayCards:
            colorOfThrownAwayCard = 'green'
        elif 'blue' in thrownAwayCards:
            colorOfThrownAwayCard = 'blue'
        else:
            print('[color] ThrownAwayCard is a wild card, code is not ready for this yet.') # TODO implement wild cards, reverse cards, draw cards, skip cards
            colorOfThrownAwayCard = 'wild card'
        print(colorOfThrownAwayCard)

        # vyberie vsetky hracove karty, ktore maju rovnaku farbu ako farba karty na hromadke
        sameColorPlayerCardsToThrowAway = [i for i in playerCards if colorOfThrownAwayCard in i]

        # zistenie cisla karty na odhadzovacej hromadke
        if 'Zero' in thrownAwayCards:
            numberOfThrownAwayCard = 'Zero'
        elif 'One' in thrownAwayCards:
            numberOfThrownAwayCard = 'One'
        elif 'Two' in thrownAwayCards:
            numberOfThrownAwayCard = 'Two'
        elif 'Three' in thrownAwayCards:
            numberOfThrownAwayCard = 'Three'
        elif 'Four' in thrownAwayCards:
            numberOfThrownAwayCard = 'Four'
        elif 'Five' in thrownAwayCards:
            numberOfThrownAwayCard = 'Five'
        elif 'Six' in thrownAwayCards:
            numberOfThrownAwayCard = 'Six'
        elif 'Seven' in thrownAwayCards:
            numberOfThrownAwayCard = 'Seven'
        elif 'Eight' in thrownAwayCards:
            numberOfThrownAwayCard = 'Eight'
        elif 'Nine' in thrownAwayCards:
            numberOfThrownAwayCard = 'Nine'
        else:
            print('[number] ThrownAwayCard is a wild card, code is not ready for this yet.') # TODO implement wild cards, reverse cards, draw cards, skip cards
            numberOfThrownAwayCard = 'wild card'
        print(numberOfThrownAwayCard)

        # vyberie vsetky hracove karty, ktore maju rovnake cislo ako cislo karty na hromadke
        sameNumberPlayerCardsToThrowAway = [i for i in playerCards if numberOfThrownAwayCard in i]

        # spojenie farbenych a ciselnych kariet, ktore moze hrac odhodit na hromadku
        allowedPlayerCardsToThrowAway = sameColorPlayerCardsToThrowAway + sameNumberPlayerCardsToThrowAway
        print('allowedPlayerCardsToThrowAway:', allowedPlayerCardsToThrowAway)

        # TODO v tomto bode mam v BE zistene, ktore karty moze hrac odhodit na hromadku. Ale ako zistim, ktoru kartu sa hrac rozhodne odhodit? To musi prist asi z FE ako premenna playerCardToThrowAway.

        # # kontrola, ci hrac zvolil kartu, ktoru zahrat moze a nasledne priradenie vybranej karty na vrch hromadky
        # if playerCardToThrowAway in allowedPlayerCardsToThrowAway:
        #     thrownAwayCards = playerCardToThrowAway
        # elif playerCardToThrowAway == 'Hrac uz nechce odhodit dalsiu kartu s rovnakym cislom alebo farbou, aj ked ich v ruke ma':
        #     # TODO tah by sa mal presunut na tah bota
        # elif playerCardToThrowAway == 'Hrac si chce potiahnut kartu z balicku':
        #     cardToRemoveFromStack = random.choice(cards_in_stack)   # random vyber karty z balicku
        #     playerCards.append(cardToRemoveFromStack)               # priradenie vybranej karty do kariet hraca
        #     cards_in_stack.remove(cardToRemoveFromStack)            # odstranenie vybranej karty z balicku
        #     # TODO pokial tato vybrana karta z balicku dovoluje hracovi odhodit tuto novu kartu, moze tak urobit, inak sa tah presunie na tah bota

        return (cards_in_stack, thrownAwayCards, playerCards)

def botMove(cards_in_stack, thrownAwayCards, botCards):
    if botCards != 0:
        allowedBotCardsToThrowAway = []  # karty, ktore moze bot odhodit na odhadzovaciu hromadku

        # zistenie farby karty na odhadzovacej hromadke
        if 'red' in thrownAwayCards:
            colorOfThrownAwayCard = 'red'
        elif 'yellow' in thrownAwayCards:
            colorOfThrownAwayCard = 'yellow'
        elif 'green' in thrownAwayCards:
            colorOfThrownAwayCard = 'green'
        elif 'blue' in thrownAwayCards:
            colorOfThrownAwayCard = 'blue'
        else:
            print('[color] ThrownAwayCard is a wild card, code is not ready for this yet.')  # TODO implement wild cards, reverse cards, draw cards, skip cards
            colorOfThrownAwayCard = 'wild card'

        # vyberie vsetky botove karty, ktore maju rovnaku farbu ako farba karty na hromadke
        sameColorBotCardsToThrowAway = [i for i in botCards if colorOfThrownAwayCard in i]

        # zistenie cisla karty na odhadzovacej hromadke
        if 'Zero' in thrownAwayCards:
            numberOfThrownAwayCard = 'Zero'
        elif 'One' in thrownAwayCards:
            numberOfThrownAwayCard = 'One'
        elif 'Two' in thrownAwayCards:
            numberOfThrownAwayCard = 'Two'
        elif 'Three' in thrownAwayCards:
            numberOfThrownAwayCard = 'Three'
        elif 'Four' in thrownAwayCards:
            numberOfThrownAwayCard = 'Four'
        elif 'Five' in thrownAwayCards:
            numberOfThrownAwayCard = 'Five'
        elif 'Six' in thrownAwayCards:
            numberOfThrownAwayCard = 'Six'
        elif 'Seven' in thrownAwayCards:
            numberOfThrownAwayCard = 'Seven'
        elif 'Eight' in thrownAwayCards:
            numberOfThrownAwayCard = 'Eight'
        elif 'Nine' in thrownAwayCards:
            numberOfThrownAwayCard = 'Nine'
        else:
            print('[number] ThrownAwayCard is a wild card, code is not ready for this yet.')  # TODO implement wild cards, reverse cards, draw cards, skip cards
            numberOfThrownAwayCard = 'wild card'

        # vyberie vsetky hracove karty, ktore maju rovnake cislo ako cislo karty na hromadke
        sameNumberBotCardsToThrowAway = [i for i in botCards if numberOfThrownAwayCard in i]

        # spojenie farbenych a ciselnych kariet, ktore moze hrac odhodit na hromadku
        allowedBotCardsToThrowAway = sameColorBotCardsToThrowAway + sameNumberBotCardsToThrowAway
        print('allowedBotCardsToThrowAway:', allowedBotCardsToThrowAway)

        # bot zvoli kartu (pripadne viacero kariet), ktore zahrat moze a nasledne priradenie vybranej karty na vrch hromadky
        # pokial ma bot viac (prípadne rovnako) kariet s rovnakou farbou, ako je na vrchu hromadky, tak na nu vylozi vsetky tieto karty
        if allowedBotCardsToThrowAway:
            if len(sameColorBotCardsToThrowAway) >= len(sameNumberBotCardsToThrowAway):
                thrownAwayCards = sameColorBotCardsToThrowAway[-1]
                # odstranenie vsetkych vyhodenych kariet z kariet bota na odhadzovaniu hromadku
                for item in sameColorBotCardsToThrowAway:
                    if item in botCards:
                        botCards.remove(item)
            # pokial ma bot viac kariet s rovnakym cislom, ako je na vrchu hromadky, tak na nu vylozi vsetky tieto karty
            elif len(sameColorBotCardsToThrowAway) < len(sameNumberBotCardsToThrowAway):
                thrownAwayCards = sameNumberBotCardsToThrowAway[-1]
                # odstranenie vsetkych vyhodenych kariet z kariet bota na odhadzovaniu hromadku
                for item in sameNumberBotCardsToThrowAway:
                    if item in botCards:
                        botCards.remove(item)
            print('Vrchna karta na odhadzovacej hromadke:', thrownAwayCards)
            print('botCards:', botCards)
        else:
            print('bot have to draw a card')
            cardToRemoveFromStack = random.choice(cards_in_stack)  # random vyber karty z balicku
            botCards.append(cardToRemoveFromStack)                 # priradenie vybranej karty do kariet bota
            print(len(cards_in_stack))
            print(len(botCards))
            # TODO pokial tato vybrana karta z balicku dovoluje botovi odhodit tuto novu kartu, urobi tak, inak sa tah presunie na tah hraca

            cards_in_stack.remove(cardToRemoveFromStack)  # odstranenie vybranej karty z balicku
        print('-----')
        return (cards_in_stack, thrownAwayCards, botCards)
# Zavolanie fce Main
Main()
