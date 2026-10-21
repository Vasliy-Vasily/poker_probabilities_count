def get_data(): #Here user should enter the table and hand data
    print('Welcome to the Poker counter! Looks like someone wants to win some money')
    number_of_players = int(input('Tell me, how many players are in the game including you?\n'))
    print('Nice, now tell me the values of your cards, where jack - 11, queen - 12, king - 13, ace - 14')
    print('Also tell me the suits (hearts, diamonds, spades, clubs)')
    print('Example: 9 hearts 12 spades')
    right = False
    while right == False:
        hand = input().split()
        if len(hand) != 4:
            print('Wrong input. Try again')
        elif int(hand[0]) > 14 or int(hand[0]) < 2 or int(hand[2]) > 14 or int(hand[2]) < 1:
            print('Wrong cards value. Try again')
        elif hand[1] not in ['hearts', 'diamonds', 'spades', 'clubs'] or hand[3] not in ['hearts', 'diamonds', 'spades', 'clubs']:
            print('Wrong suits. Try again')
        elif hand[0] == hand[2] and hand[1] == hand[3]:
            print('You cannot have two identical cards. Try again')
        else:
            right = True
    print('Now, how many cards are on table now?')
    right = False
    while right == False:
        table_card_number = int(input())
        if table_card_number < 0 or table_card_number > 5:
            print('Wrong input. Try again')
        else:
            right = True
    right = False
    if table_card_number != 0:
        print('Last step: tell me, what cards are on the table?')
        print('Write it in the same format as you did with your hand')
        while right == False:
            table_cards = input().split()
            if len(table_cards) != table_card_number * 2:
                print('Wrong input. Try again')
                continue
            correct = True
            for i in range(0, len(table_cards), 2):
                if int(table_cards[i]) > 14 or int(table_cards[i]) < 2:
                    print('Wrong cards value. Try again')
                    correct = False
                    break
                if table_cards[i + 1] not in ['hearts', 'diamonds', 'spades', 'clubs']:
                    print('Wrong suits. Try again')
                    correct = False
                    break
            if correct:
                table_pairs_check = [(table_cards[i], table_cards[i + 1])
                                     for i in range(0, len(table_cards), 2)]
                if len(set(table_pairs_check)) != len(table_pairs_check):
                    print('You cannot have two identical cards on the table. Try again')
                    correct = False
            if correct:
                hand_pairs = [(hand[i], hand[i + 1]) for i in range(0, len(hand), 2)]
                table_pairs = [(table_cards[i], table_cards[i + 1]) for i in range(0, len(table_cards), 2)]
                if any(card in table_pairs for card in hand_pairs):
                    print('Your hand cards cannot be on the table. Try again')
                    correct = False
            if correct:
                right = True
    else:
        table_cards = []
    return number_of_players, hand, table_card_number, table_cards
