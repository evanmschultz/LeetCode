"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a 
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
    profit, return 0.
"""


# def maxProfit(prices):
#     """
#         failed as time complexity is O(n^2)
#     """
#     max_profit = 0

#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             if prices[j] - prices[i] > max_profit:
#                 max_profit = prices[j] - prices[i]

#     return max_profit


# print(maxProfit([7, 6, 4, 3, 1]))
# print(maxProfit([1, 2]))


def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        if price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))

# use min and max built in functions


def maxProfit2(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
