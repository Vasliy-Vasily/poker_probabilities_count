import math
#In this function we find errors for 95% confidence interval
def err(victory_rate, draw_rate, lose_rate, simulations=100000):
    se_victory_rate = math.sqrt(victory_rate * (1 - victory_rate)/simulations)
    victory_error = round(se_victory_rate * 1.96, 5)
    se_draw_rate = math.sqrt(draw_rate * (1 - draw_rate) / simulations)
    draw_error = round(se_draw_rate * 1.96, 5)
    se_lose_rate = math.sqrt(lose_rate * (1 - lose_rate) / simulations)
    lose_error = round(se_lose_rate * 1.96, 5)
    return victory_error, draw_error, lose_error
