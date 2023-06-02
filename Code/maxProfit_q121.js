/*
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a 
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
    profit, return 0.
*/

function maxProfit(prices) {
    let min_price = prices[0]
    let max_profit = 0

    for (i = 0; i < prices.length; i++) {
        // do `else if` because these checks are mutually exclusive and `else if` makes that more obvious
        if (prices[i] < min_price) {
            min_price = prices[i]
        } else if (max_profit < prices[i] - min_price) {
            max_profit = prices[i] - min_price
        }
    }

    return max_profit
}
