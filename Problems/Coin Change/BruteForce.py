"""
    Finding number of coins (of certain denominations) that add up to a given amount of money. 
    @wikipedia
"""
import sys

d = [1, 2, 5]
def coin_change(amount):
    if amount == 0:
        return 0
    res = sys.maxsize
    for i in d:
        if amount >= i:
            res = min(res, coin_change(amount - i) + 1)
    return res

print(coin_change(23));