__author__ = "Zatko Tomas"
__login__ = "xzatko02"

import random


# Pravidla hry Uno: https://www.navod-k-obsluze.cz/upload/karetni-hra-uno-navod-k-obsluze.pdf

def Main():
    # zamiesanie kariet na zaciatku hry
    cards_in_stack = shuffle_new_cards()
    # inicializacia premennych - zoznamov
    playerCards = []
    botCards = []
    second_botCards = []
    draw2Card_give = False
    draw2Card_get = False
    skipCard = False
    reverseCard = False
    # Game mode: one player, one pc bot
    numberOfPlayers = 2  # TODO VYMAZAT, GAME MODE SI BUDE VOLIT SAM HRAC
    # Game mode: one player, two pc bots
    ## numberOfPlayers = 3  # TODO VYMAZAT, GAME MODE SI BUDE VOLIT SAM HRAC

    # rozdanie 7 kariet hracovi a botovi, pripadne druhemu botovi a odstranenie kariet z balicku
    numberOfPlayers, cards_in_stack, playerCards, botCards, second_botCards = deal_the_cards(numberOfPlayers,
                                                                                             cards_in_stack,
                                                                                             playerCards, botCards,
                                                                                             second_botCards)

    # Otocenie vrchnej karty z balicku licem nahoru a polozenie na stol ako zaklad odhadzovacej hromadky, na kt. budu hraci odhadzovat svoje karty
    thrownAwayCards = cards_in_stack[-1]
    cardToRemoveFromStack = cards_in_stack[-1]
    cards_in_stack.remove(cardToRemoveFromStack)
    print('Vrchna karta na odhadzovacej hromadke:', thrownAwayCards)
    print('cards_in_stack:', len(cards_in_stack))

    # volanie funkcii na tah hraca a bota
    while (1):
        cards_in_stack, thrownAwayCards, playerCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get = playerMove(cards_in_stack, thrownAwayCards, playerCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get)
        if skipCard or reverseCard:
            cards_in_stack, thrownAwayCards, playerCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get = playerMove(cards_in_stack, thrownAwayCards, playerCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get)
        cards_in_stack, thrownAwayCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get = botMove(cards_in_stack, thrownAwayCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get)
        if skipCard or reverseCard:
            cards_in_stack, thrownAwayCards, botCards, skipCard, reverseCard, draw2Card_give,draw2Card_get = botMove(cards_in_stack, thrownAwayCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get)


def playerMove(cards_in_stack, thrownAwayCards, playerCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get):
    # na tahu je hrac, na odhadzovaciu hromadku moze odhodit len kartu z ruky, ktora ma rovnaku farbu alebo ciselnu hodnotu ako vrchna karta na odhadzovacej hromadke
    # TODO urobit to aj pre rovnaky symbol
    if len(playerCards) != 0:
        draw2Card_give = False
        skipCard = False
        reverseCard = False
        allowedPlayerCardsToThrowAway = []  # karty, ktore moze hrac odhodit na odhadzovaciu hromadku

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
            print(
                '[color] ThrownAwayCard is a wild card, code is not ready for this yet.')  # TODO implement wild cards, reverse cards, draw cards, skip cards
            colorOfThrownAwayCard = 'wild card'
        print(colorOfThrownAwayCard)

        # vyberie vsetky hracove karty, ktore maju rovnaku farbu ako farba karty na hromadke
        sameColorPlayerCardsToThrowAway = [i for i in playerCards if colorOfThrownAwayCard in i]

        # zistujem, ci ma bot skipCard a ak ano, zistim si jej index vo farebnych kartach, ktore moze odhodit
        indexOfDraw2Card_give = -1
        indexOfSkipCard = -1
        indexOfReverseCard = -1
        for item in sameColorPlayerCardsToThrowAway:
            indexOfDraw2Card_give += 1
            indexOfSkipCard += 1
            indexOfReverseCard += 1
            if 'Draw2' in item:
                draw2Card_give = True
                break
            if 'Skip' in item:
                skipCard = True
                break
            if 'Reverse' in item:
                reverseCard = True
                break

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
            print(
                '[number] ThrownAwayCard is a wild card, code is not ready for this yet.')  # TODO implement wild cards, reverse cards, draw cards, skip cards
            numberOfThrownAwayCard = 'wild card'
        print(numberOfThrownAwayCard)

        # vyberie vsetky hracove karty, ktore maju rovnake cislo ako cislo karty na hromadke
        sameNumberPlayerCardsToThrowAway = [i for i in playerCards if numberOfThrownAwayCard in i]

        # spojenie farbenych a ciselnych kariet, ktore moze hrac odhodit na hromadku
        # TODO vyriesit duplikaty, ked sa spoja farba a cislo
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

        ################ VYMAZAT TENTO BLOK, SLUZI LEN NA OTESTOVANIE FUNGOVANIA HRY DVOCH BOTOV
        if allowedPlayerCardsToThrowAway and draw2Card_get != True:
            if skipCard != True and reverseCard != True and draw2Card_give != True and draw2Card_get != True:
                if len(sameColorPlayerCardsToThrowAway) >= len(sameNumberPlayerCardsToThrowAway):
                    thrownAwayCards = sameColorPlayerCardsToThrowAway[-1]
                    playerCards.remove(
                        sameColorPlayerCardsToThrowAway[-1])  # odstranenie poslednej karty - tej, kt. mozem odhodit

                # pokial ma bot viac kariet s rovnakym cislom, ako je na vrchu hromadky, tak na nu vylozi vsetky tieto karty
                elif len(sameColorPlayerCardsToThrowAway) < len(sameNumberPlayerCardsToThrowAway):
                    thrownAwayCards = sameNumberPlayerCardsToThrowAway[-1]
                    playerCards.remove(
                        sameNumberPlayerCardsToThrowAway[-1])  # odstranenie poslednej karty - tej, kt. mozem odhodit

                print('Vrchna karta na odhadzovacej hromadke:', thrownAwayCards)
                print('playerCards:', playerCards)
                if len(playerCards) == 0:
                    print('Player has won the game.')
                    print(botCards)
                    # zistenie hodnoty jednotlivych botovych kariet, kt. ma na ruke po hracovom vitazstve
                    coinsToEarn = 0
                    for item in botCards:
                        if 'Zero' in item:
                            coinsToEarn += 0
                        elif 'One' in item:
                            coinsToEarn += 1
                        elif 'Two' in item:
                            coinsToEarn += 2
                        elif 'Three' in item:
                            coinsToEarn += 3
                        elif 'Four' in item:
                            coinsToEarn += 4
                        elif 'Five' in item:
                            coinsToEarn += 5
                        elif 'Six' in item:
                            coinsToEarn += 6
                        elif 'Seven' in item:
                            coinsToEarn += 7
                        elif 'Eight' in item:
                            coinsToEarn += 8
                        elif 'Nine' in item:
                            coinsToEarn += 9
                    ## return coinsToEarn  # vratim do FE informaciu o pocte hracovych zarobenych coinov z danej hry
                    print('coinsToEarn:', coinsToEarn)
                    exit(0)
            # pokial ma skipCard alebo reverseCard, pouzije ju a odstrani sa mu z ruk a pokracuje hned dalsim tahom
            elif skipCard == True or reverseCard == True or draw2Card_give == True:
                if skipCard == True:
                    thrownAwayCards = sameColorPlayerCardsToThrowAway[indexOfSkipCard]
                    print('indexOfSkipCard:', indexOfSkipCard)
                    playerCards.remove(sameColorPlayerCardsToThrowAway[indexOfSkipCard])
                elif reverseCard == True:
                    thrownAwayCards = sameColorPlayerCardsToThrowAway[indexOfReverseCard]
                    print('indexOfReverseCard:', indexOfReverseCard)
                    playerCards.remove(sameColorPlayerCardsToThrowAway[indexOfReverseCard])
                elif draw2Card_give == True:
                    thrownAwayCards = sameColorPlayerCardsToThrowAway[indexOfDraw2Card_give]
                    print('indexOfDraw2Card_give', indexOfDraw2Card_give)
                    playerCards.remove(sameColorPlayerCardsToThrowAway[indexOfDraw2Card_give])
                    draw2Card_get = True    # priznak pre bota, ze si ma zobrat dve karty na svojom tahu


        # Nutnost potiahnutia karty z balicku
        elif not allowedPlayerCardsToThrowAway or draw2Card_get == True:
            print('player have to draw a card or two cards bcs bot played draw2Card')
            # nove vygenerovanie balicku kariet, pokial uz je balicek prazdny
            if len(cards_in_stack) == 0:
                cards_in_stack = shuffle_new_cards()
            cardToRemoveFromStack = random.choice(cards_in_stack)  # random vyber karty z balicku
            playerCards.append(cardToRemoveFromStack)  # priradenie vybranej karty do kariet bota
            cards_in_stack.remove(cardToRemoveFromStack)  # odstranenie vybranej karty z balicku
            if draw2Card_get == True:
                if len(cards_in_stack) == 0:
                    cards_in_stack = shuffle_new_cards()
                cardToRemoveFromStack = random.choice(cards_in_stack)  # random vyber karty z balicku
                playerCards.append(cardToRemoveFromStack)  # priradenie vybranej karty do kariet bota
                cards_in_stack.remove(cardToRemoveFromStack)  # odstranenie vybranej karty z balicku
                draw2Card_get = False
            print(len(cards_in_stack))
            print(playerCards)
            print(len(playerCards))
            # TODO pokial tato vybrana karta z balicku dovoluje botovi odhodit tuto novu kartu, urobi tak, inak sa tah presunie na tah hraca


        print('-----')
        ################ AZ POTIALTO VYMAZAT BLOK KODU, KT. SLUZI NA OTESTOVANIE

        return (cards_in_stack, thrownAwayCards, playerCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get)
    else:
        print('Player has won the game.')
        exit(0)


def botMove(cards_in_stack, thrownAwayCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get):
    if len(botCards) != 0:
        draw2Card_give = False
        skipCard = False
        reverseCard = False
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
            print(
                '[color] ThrownAwayCard is a wild card, code is not ready for this yet.')  # TODO implement wild cards, reverse cards, draw cards, skip cards
            colorOfThrownAwayCard = 'wild card'

        # vyberie vsetky botove karty, ktore maju rovnaku farbu ako farba karty na hromadke
        sameColorBotCardsToThrowAway = [i for i in botCards if colorOfThrownAwayCard in i]

        # zistujem, ci ma bot skipCard a ak ano, zistim si jej index vo farebnych kartach, ktore moze odhodit
        indexOfDraw2Card_give = -1
        indexOfSkipCard = -1
        indexOfReverseCard = -1
        for item in sameColorBotCardsToThrowAway:
            indexOfDraw2Card_give += 1
            indexOfSkipCard += 1
            indexOfReverseCard += 1
            if 'Draw2' in item:
                draw2Card_give = True
                break
            if 'Skip' in item:
                skipCard = True
                break
            if 'Reverse' in item:
                reverseCard = True
                break

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
            print(
                '[number] ThrownAwayCard is a wild card, code is not ready for this yet.')  # TODO implement wild cards, reverse cards, draw cards, skip cards
            numberOfThrownAwayCard = 'wild card'

        # vyberie vsetky hracove karty, ktore maju rovnake cislo ako cislo karty na hromadke
        sameNumberBotCardsToThrowAway = [i for i in botCards if numberOfThrownAwayCard in i]

        # spojenie farbenych a ciselnych kariet, ktore moze hrac odhodit na hromadku
        allowedBotCardsToThrowAway = sameColorBotCardsToThrowAway + sameNumberBotCardsToThrowAway
        print('allowedBotCardsToThrowAway:', allowedBotCardsToThrowAway)

        # bot zvoli kartu (pripadne viacero kariet), ktore zahrat moze a nasledne priradenie vybranej karty na vrch hromadky
        # pokial ma bot viac (prípadne rovnako) kariet s rovnakou farbou, ako je na vrchu hromadky, tak na nu vylozi vsetky tieto karty
        if allowedBotCardsToThrowAway and draw2Card_get != True:
            if skipCard != True and reverseCard != True and draw2Card_give != True and draw2Card_get != True:
                if len(sameColorBotCardsToThrowAway) >= len(sameNumberBotCardsToThrowAway):
                    thrownAwayCards = sameColorBotCardsToThrowAway[-1]  # odstranenie poslednej karty - tej, kt. mozem odhodit
                    botCards.remove(sameColorBotCardsToThrowAway[-1])

                # pokial ma bot viac kariet s rovnakym cislom, ako je na vrchu hromadky, tak na nu vylozi vsetky tieto karty
                elif len(sameColorBotCardsToThrowAway) < len(sameNumberBotCardsToThrowAway):
                    thrownAwayCards = sameNumberBotCardsToThrowAway[
                        -1]  # odstranenie poslednej karty - tej, kt. mozem odhodit
                    botCards.remove(sameNumberBotCardsToThrowAway[-1])

                print('Vrchna karta na odhadzovacej hromadke:', thrownAwayCards)
                print('botCards:', botCards)
                if len(botCards) == 0:
                    print('Bot has won the game.')
                    exit(0)
            # pokial ma skipCard alebo reverseCard, pouzije ju a odstrani sa mu z ruk a pokracuje hned dalsim tahom
            elif skipCard == True or reverseCard == True or draw2Card_give == True:
                if skipCard == True:
                    thrownAwayCards = sameColorBotCardsToThrowAway[indexOfSkipCard]
                    print('indexOfSkipCard:', indexOfSkipCard)
                    botCards.remove(sameColorBotCardsToThrowAway[indexOfSkipCard])
                elif reverseCard == True:
                    thrownAwayCards = sameColorBotCardsToThrowAway[indexOfReverseCard]
                    print('indexOfReverseCard:', indexOfReverseCard)
                    botCards.remove(sameColorBotCardsToThrowAway[indexOfReverseCard])
                elif draw2Card_give == True:
                    thrownAwayCards = sameColorBotCardsToThrowAway[indexOfDraw2Card_give]
                    print('indexOfDraw2Card_give', indexOfDraw2Card_give)
                    botCards.remove(sameColorBotCardsToThrowAway[indexOfDraw2Card_give])
                    draw2Card_get = True    # priznak pre bota, ze si ma zobrat dve karty na svojom tahu

        # Nutnost potiahnutia karty z balicku
        elif not allowedBotCardsToThrowAway or draw2Card_get == True:
            print('bot have to draw a card or two card bcs another player played draw2Card')
            # nove vygenerovanie balicku kariet, pokial uz je balicek prazdny
            if len(cards_in_stack) == 0:
                cards_in_stack = shuffle_new_cards()
            cardToRemoveFromStack = random.choice(cards_in_stack)  # random vyber karty z balicku
            botCards.append(cardToRemoveFromStack)  # priradenie vybranej karty do kariet bota
            cards_in_stack.remove(cardToRemoveFromStack)  # odstranenie vybranej karty z balicku
            if draw2Card_get == True:
                if len(cards_in_stack) == 0:
                    cards_in_stack = shuffle_new_cards()
                cardToRemoveFromStack = random.choice(cards_in_stack)  # random vyber karty z balicku
                botCards.append(cardToRemoveFromStack)  # priradenie vybranej karty do kariet bota
                cards_in_stack.remove(cardToRemoveFromStack)  # odstranenie vybranej karty z balicku
                draw2Card_get = False

            print(len(cards_in_stack))
            print(botCards)
            print(len(botCards))
            # TODO pokial tato nova vybrana karta z balicku dovoluje botovi odhodit tuto novu kartu, urobi tak, inak sa tah presunie na tah hraca

        print('-----')

        return (cards_in_stack, thrownAwayCards, botCards, skipCard, reverseCard, draw2Card_give, draw2Card_get)
    else:
        print('Bot has won the game.')
        exit(0)


# inicializacia a zamiesanie kariet
def shuffle_new_cards():
    new_cards = ['redZero', 'redOne', 'redTwo', 'redThree', 'redFour', 'redFive', 'redSix', 'redSeven', 'redEight',
                 'redNine', 'second_redOne', 'second_redTwo', 'second_redThree', 'second_redFour', 'second_redFive',
                 'second_redSix', 'second_redSeven', 'second_redEight', 'second_redNine', 'redSkipCard', 'second_redSkipCard', 'redReverseCard', 'second_redReverseCard', 'redDraw2Card', 'second_redDraw2Card',
                 'yellowZero', 'yellowOne', 'yellowTwo', 'yellowThree', 'yellowFour', 'yellowFive', 'yellowSix',
                 'yellowSeven', 'yellowEight', 'yellowNine', 'second_yellowOne', 'second_yellowTwo',
                 'second_yellowThree', 'second_yellowFour', 'second_yellowFive', 'second_yellowSix',
                 'second_yellowSeven', 'second_yellowEight', 'second_yellowNine', 'yellowSkipCard', 'second_yellowSkipCard', 'yellowReverseCard', 'second_yellowReverseCard', 'yellowDraw2Card', 'second_yellowDraw2Card',
                 'greenZero', 'greenOne', 'greenTwo', 'greenThree', 'greenFour', 'greenFive', 'greenSix', 'greenSeven',
                 'greenEight', 'greenNine', 'second_greenOne', 'second_greenTwo', 'second_greenThree',
                 'second_greenFour', 'second_greenFive', 'second_greenSix', 'second_greenSeven', 'second_greenEight',
                 'second_greenNine', 'greenSkipCard', 'second_greenSkipCard', 'greenReverseCard', 'second_greenReverseCard', 'greenDraw2Card', 'second_greenDraw2Card',
                 'blueZero', 'blueOne', 'blueTwo', 'blueThree', 'blueFour', 'blueFive', 'blueSix', 'blueSeven',
                 'blueEight', 'blueNine', 'second_blueOne', 'second_blueTwo', 'second_blueThree', 'second_blueFour',
                 'second_blueFive', 'second_blueSix', 'second_blueSeven', 'second_blueEight', 'second_blueNine',
                 'blueSkipCard', 'second_blueSkipCard', 'blueReverseCard', 'second_blueReverseCard', 'blueDraw2Card', 'second_blueDraw2Card']

    # TODO PODPOROVAT WILD CARDS
    # ,'wildCard', 'second_wildCard', 'third_wildCard', 'fourth_wildCard', 'wildDraw4Card',
    # 'second_wildDraw4Card', 'third_wildDraw4Card', 'fourth_wildDraw4Card', redSkipCard,... ] A MNOHO DALSIIIIIIIIIIIIICH
    # zamiesanie balicku kariet
    random.shuffle(new_cards)
    return new_cards


# rozdanie 7 kariet hracovi a botovi, pripadne druhemu botovi a odstranenie kariet z balicku
def deal_the_cards(numberOfPlayers, cards_in_stack, playerCards, botCards, second_botCards):
    if numberOfPlayers == 2 or numberOfPlayers == 3:
        print('cards_in_stack:', len(cards_in_stack))
        # rozdanie 7 kariet hracovi
        for i in range(7):
            cardToRemoveFromStack = random.choice(cards_in_stack)
            playerCards.append(cardToRemoveFromStack)
            cards_in_stack.remove(cardToRemoveFromStack)
        print('playerCards:', playerCards)
        print('cards_in_stack:', len(cards_in_stack))
        # rozdanie 7 kariet botovi
        for i in range(7):
            cardToRemoveFromStack = random.choice(cards_in_stack)
            botCards.append(cardToRemoveFromStack)
            cards_in_stack.remove(cardToRemoveFromStack)
        print('botCards:', botCards)
        print('cards_in_stack:', len(cards_in_stack))
        # rozdanie 7 kariet druhemu botovi
        if numberOfPlayers == 3:
            for i in range(7):
                cardToRemoveFromStack = random.choice(cards_in_stack)
                second_botCards.append(cardToRemoveFromStack)
                cards_in_stack.remove(cardToRemoveFromStack)
            print('second_botCards:', second_botCards)
            print('cards_in_stack:', len(cards_in_stack))
    return (numberOfPlayers, cards_in_stack, playerCards, botCards, second_botCards)


# Zavolanie fce Main
Main()
