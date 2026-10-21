import random
from evaluation import evaluate_7

#This functions generates a lot of random decks of cards for further analysis
def generate_opponent_hands(number_of_players, hand, table_cards, simulations=100000):
    victories = draws = loses = 0

    def to_int_pair(value_str, suit_str):
        value_map = {'11': 11, '12': 12, '13': 13, '14': 14}
        rank = value_map.get(value_str, int(value_str))
        suit_map = {'hearts': 1, 'diamonds': 2, 'spades': 3, 'clubs': 4}
        return [rank, suit_map[suit_str]]

    known_pairs = []
    for i in range(0, len(hand), 2):
        known_pairs.append(to_int_pair(hand[i], hand[i + 1]))
    for i in range(0, len(table_cards), 2):
        known_pairs.append(to_int_pair(table_cards[i], table_cards[i + 1]))

    full_deck = [[r, s] for r in range(2, 15) for s in range(1, 5)]
    remaining = [c for c in full_deck if c not in known_pairs]
    num_opponents = number_of_players - 1
    cards_on_table = len(table_cards) // 2
    missing_table = 5 - cards_on_table
    total_needed = num_opponents * 2 + missing_table
    if total_needed > len(remaining):
        raise ValueError(
            f'Не хватает карт: нужно {total_needed}, доступно {len(remaining)}'
        )
    known_table_pairs = [to_int_pair(table_cards[i], table_cards[i + 1])
                         for i in range(0, len(table_cards), 2)]
    user_pair = [to_int_pair(hand[0], hand[1]), to_int_pair(hand[2], hand[3])]

    for _ in range(simulations):
        random.shuffle(remaining)
        idx = 0
        new_table_cards = remaining[idx: idx + missing_table]
        idx += missing_table
        full_table = known_table_pairs + new_table_cards
        opponent_hands = []
        best_rank = 0
        best_kickers = []
        best_hand = None
        best_opponent_index = -1

        for opp_i in range(num_opponents):
            opp_hand = [remaining[idx], remaining[idx + 1]]
            idx += 2
            opponent_hands.append(opp_hand)

            seven = full_table + opp_hand
            rank, kickers = evaluate_7(seven)

            if (rank, kickers) > (best_rank, best_kickers):
                best_rank = rank
                best_kickers = kickers
                best_hand = seven[:]
                best_opponent_index = opp_i

        user_seven = full_table + user_pair
        user_rank, user_kickers = evaluate_7(user_seven)

        if (user_rank, user_kickers) > (best_rank, best_kickers):
            victories += 1
        elif (user_rank, user_kickers) == (best_rank, best_kickers):
            draws += 1
        else:
            loses += 1

    victory_rate = round(victories / simulations, 5)
    draw_rate = round(draws / simulations, 5)
    lose_rate = round(loses / simulations, 5)
    return victory_rate, draw_rate, lose_rate

