from getting_data import get_data
from generation import generate_opponent_hands
from error import err


def main():
    number_of_players, hand, table_card_number, table_cards = get_data()
    if table_card_number != 0:
        print('So you have', ' '.join(hand), 'and', ' '.join(table_cards), 'on the table')
    else:
        print('So you have', ' '.join(hand), 'and table is clear yet')
    print('Now the program will now generate 100000 random distributions of cards '
          'among your opponents hands and calculate the probability that you currently hold the best hand.')

    victory_rate, draw_rate, lose_rate = generate_opponent_hands(
        number_of_players, hand, table_cards, simulations=100000
    )

    victory_error, draw_error, lose_error = err(victory_rate, draw_rate, lose_rate, simulations=100000)

    print(' ')
    print(f'In random 100000 simulations you have won in {victory_rate * 100:.3f} % '
          f'± {victory_error * 100:.3f} % of games, '
          f'you got draw in {draw_rate * 100:.3f} % ± {draw_error * 100:.3f} % of games and '
          f'lost in {lose_rate * 100:.3f} % ± {lose_error * 100:.3f} % of games\n'
          f'(errors are counted for 95% confidence interval)')

    


if __name__ == '__main__':
    main()
