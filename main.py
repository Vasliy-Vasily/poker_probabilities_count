from getting_data import get_data
from generation import generate_opponent_hands


def main():
    number_of_players, hand, table_card_number, table_cards = get_data()
    if table_card_number != 0:
        print('So you have', ' '.join(hand), 'and', ' '.join(table_cards), 'on the table')
    else:
        print('So you have', ' '.join(hand))
    print('Now the program will now generate 10,000 random distributions of cards '
          'among your opponents hands and calculate the probability that you currently hold the best hand.')

    victory_rate, draws_rate, loses_rate = generate_opponent_hands(
        number_of_players, hand, table_cards, simulations=10000
    )

    print(' ')
    print(f'In 10000 simulations you have won in {victory_rate} % of games, '
          f'you got draw in {draws_rate} % of games and lost in {loses_rate} % of games')


if __name__ == '__main__':
    main()
