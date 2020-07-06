"""
    Finding number of coins (of certain denominations) that add up to a given amount of money. 
    @wikipedia
"""

def coin_change(amount: int, denominations: list):
    """
        greedy approach to solve coin change problem 

        Note: although, greedy approach is easy to implement; it does not provide optimal solution

        Parameters
        ----------
        amount: given amount of money to find minimum number of coins
        denominations: list of coins it can be
    """
    # sort the denomations in increasing order
    denominations.sort()
    
    # find the highest coin that can be used
    number_of_coins = 0
    
    # keep track if the required coin is found or not
    not_found = True

    # results
    result = {}
    while amount != 0:
        not_found = True
        # looping through the denominations to find the largest coin that be used
        for i in range(len(denominations)-1, -1, -1):
            if amount - denominations[i] >= 0:
                number_of_coins += 1
                amount -= denominations[i]
                # adding to results
                if denominations[i] not in result.keys():
                    result[denominations[i]] = 1
                else:
                    result[denominations[i]] += 1
                not_found = False
                break
        if not_found:
            return result
    return result

if __name__ == "__main__":
    print(f'Minimum coins required to change 30: {coin_change(20, [5, 1, 2])}')
    print(f'Minimum coins required to change 23: {coin_change(23, [5, 1, 2])}')
    print(f'Minimum coins required to change 6: {coin_change(6, [5, 1, 2])}')
