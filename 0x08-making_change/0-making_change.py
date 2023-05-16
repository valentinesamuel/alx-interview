#!/usr/bin/python3
'''Making a change
'''


def makeChange(coins, total):
    '''given a total amount, determine the least amound if coins needed
    '''
    if total_amount <= 0:
        return 0
    coins = 0
    coins_index = 0
    sort_coins = sorted(coins, reverse=True)
    cons_length = len(coins)
    while total_amount > 0:
        if coins_index >= cons_length:
            return -1
        if total_amount - sort_coins[coins_index] >= 0:
            total_amount -= sort_coins[coins_index]
            coins += 1
        else:
            coins_index += 1
    return coins