from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    first_buy_sell_profits = [0.0] * len(prices)
    second_buy_sell_profits = [0.0] * len(prices)
    min_price = 0
    for i in range(len(prices)):
        profit = prices[i] - min_price
        first_buy_sell_profits[i] = max(profit, 0)
        if prices[i] < min_price:
            min_price = prices[i]
    max_price = prices[-1]
    for i in reversed(range(len(prices))):
        profit = max_price - prices[i]
        second_buy_sell_profits[i] = max(profit, 0)
        if prices[i] > max_price:
            max_price = prices[i]
    max_profit = 0
    max_profits = []
    for i in range(len(prices)-1):
        profit = first_buy_sell_profits[i] + second_buy_sell_profits[i+1]
        max_profits.append(profit)
        if profit > max_profit:
            max_profit = profit
    print(max_profits)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
