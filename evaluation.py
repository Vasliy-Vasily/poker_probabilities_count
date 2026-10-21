#This function evaluates hands and returns a tuple (rank, kickers) that 
    # can be used to compare two hands: a larger tuple indicates a stronger combination 
def evaluate_7(cards): 
    counter = {}
    for c in cards:
        counter[c[0]] = counter.get(c[0], 0) + 1

    by_freq = sorted(counter.items(), key=lambda x: (-x[1], -x[0]))
    counts = [f for _, f in by_freq]
    values_sorted = [v for v, _ in by_freq]

    suit_counter = {}
    for c in cards:
        suit_counter[c[1]] = suit_counter.get(c[1], 0) + 1
    flush_suit = None
    for s, f in suit_counter.items():
        if f >= 5:
            flush_suit = s
            break

    unique_ranks = sorted(set(counter.keys()))
    if 14 in unique_ranks:
        unique_ranks_low = [1] + unique_ranks
    else:
        unique_ranks_low = unique_ranks
    straight_high = 0
    c = 1
    for i in range(1, len(unique_ranks_low)):
        if unique_ranks_low[i] == unique_ranks_low[i - 1] + 1:
            c += 1
        else:
            c = 1
        if c >= 5:
            straight_high = unique_ranks_low[i]

    if flush_suit is not None:
        flush_ranks = sorted(set(card[0] for card in cards if card[1] == flush_suit))
        if 14 in flush_ranks:
            flush_ranks_low = [1] + flush_ranks
        else:
            flush_ranks_low = flush_ranks
        c2 = 1
        sf_high = 0
        for i in range(1, len(flush_ranks_low)):
            if flush_ranks_low[i] == flush_ranks_low[i - 1] + 1:
                c2 += 1
            else:
                c2 = 1
            if c2 >= 5:
                sf_high = flush_ranks_low[i]
        if sf_high > 0:
            return (9, [sf_high])

    if counts[0] == 4:
        quad = values_sorted[0]
        kicker = max(v for v in values_sorted[1:])
        return (8, [quad, kicker])
    if counts[0] == 3 and counts[1] == 2:
        return (7, [values_sorted[0], values_sorted[1]])
    if flush_suit is not None:
        flush_vals = sorted([card[0] for card in cards if card[1] == flush_suit], reverse=True)
        return (6, flush_vals[:5])
    if straight_high > 0:
        return (5, [straight_high])
    if counts[0] == 3:
        trips = values_sorted[0]
        kickers = sorted(values_sorted[1:], reverse=True)[:2]
        return (4, [trips] + kickers)
    if counts[0] == 2 and counts[1] == 2:
        pair1, pair2 = values_sorted[0], values_sorted[1]
        kicker = max(values_sorted[2:])
        return (3, [pair1, pair2, kicker])
    if counts[0] == 2:
        pair = values_sorted[0]
        kickers = sorted(values_sorted[1:], reverse=True)[:3]
        return (2, [pair] + kickers)
    return (1, sorted([card[0] for card in cards], reverse=True)[:5])
