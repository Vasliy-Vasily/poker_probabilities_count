import matplotlib.pyplot as plt
import numpy as np

from generation import generate_opponent_hands
from getting_data import get_data


def convergence(
    number_of_players,
    hand,
    table_cards,
    simulation_counts=(100, 500, 1000, 5000, 10000, 100000),
    log_scale=True,
): #Shows the convergence of results through count of simulations
    results = {}
    for n in simulation_counts:
        victory, draw, lose = generate_opponent_hands(
            number_of_players, hand, table_cards, simulations=n
        )
        results[n] = (victory * 100, draw * 100, lose * 100)
    ns = list(results.keys())
    victories = [results[n][0] for n in ns]
    draws     = [results[n][1] for n in ns]
    loses     = [results[n][2] for n in ns]
    if log_scale:
        x_pos = np.log10(ns)
    else:
        x_pos = np.array(ns, dtype=float)
    if len(x_pos) > 1:
        min_gap = np.min(np.diff(np.sort(x_pos)))
    else:
        min_gap = 1.0
    width = min_gap * 0.25
    fig, ax = plt.subplots(figsize=(10, 6))
    bars_v = ax.bar(x_pos - width, victories, width, label='Победа',    color='#2e7d32')
    bars_d = ax.bar(x_pos,          draws,     width, label='Ничья',     color='#9e9e9e')
    bars_l = ax.bar(x_pos + width,  loses,     width, label='Поражение', color='#c62828')

    for bars in (bars_v, bars_d, bars_l):
        for bar in bars:
            h = bar.get_height()
            if h >= 1:
                ax.annotate(
                    f'{h:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, h),
                    xytext=(0, 3),
                    textcoords='offset points',
                    ha='center', va='bottom',
                    fontsize=8,
                )

    ax.set_xticks(x_pos)
    ax.set_xticklabels([str(n) for n in ns])
    ax.set_xlabel('Количество симуляций')
    ax.set_ylabel('Доля, %')
    ax.set_title('Оценка вероятности исходов в зависимости от числа симуляций')
    ax.set_ylim(0, 110)
    ax.legend(loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    margin = (x_pos.max() - x_pos.min()) * 0.05
    ax.set_xlim(x_pos.min() - margin, x_pos.max() + margin)
    plt.tight_layout()
    plt.show()
    return results

def two_aces(
    number_of_players,
    hand,
    table_cards,
    simulations
): #Shows how the winning chances are changing with changing of players count
    player_counts = list(range(2, number_of_players + 1))
    results = {}
    for n in player_counts:
        victory, draw, lose = generate_opponent_hands(
            n, hand, table_cards, simulations=simulations
        )
        results[n] = (victory * 100, draw * 100, lose * 100)
    ns = list(results.keys())
    victories = [results[n][0] for n in ns]
    draws     = [results[n][1] for n in ns]
    loses     = [results[n][2] for n in ns]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ns, victories, marker='o', linewidth=2, color='#2e7d32', label='Победа')
    ax.plot(ns, draws,     marker='s', linewidth=2, color='#9e9e9e', label='Ничья')
    ax.plot(ns, loses,     marker='^', linewidth=2, color='#c62828', label='Поражение')
    for values, color in ((victories, '#2e7d32'),
                          (draws,     '#9e9e9e'),
                          (loses,     '#c62828')):
        for x_val, y_val in zip(ns, values):
            ax.annotate(
                f'{y_val:.1f}',
                xy=(x_val, y_val),
                xytext=(0, 7),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=8, color=color,
            )

    ax.set_xticks(ns)
    ax.set_xticklabels([str(n) for n in ns])
    ax.set_xlabel('Количество игроков (включая вас)')
    ax.set_ylabel('Доля, %')
    ax.set_title(
        f'Вероятности исходов для руки {" ".join(hand)}'
        + (f' при столе {" ".join(table_cards)}' if table_cards else ' (префлоп)')
    )
    ax.set_ylim(0, 110)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='center right')
    plt.tight_layout()
    plt.show()

    return results


def call():
    number_of_players, hand, table_card_number, table_cards = get_data()
    convergence(
        number_of_players, hand, table_cards,
        simulation_counts=[100, 500, 1000, 5000, 10000, 100000],
        log_scale=True,
    )
    two_aces(8, hand, table_cards, 10000)


call()
