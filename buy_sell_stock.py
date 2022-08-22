'''
Best Time to Buy and Sell Stock.
You are given an array prices
You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0
'''
def maxProfit(prices):    
    if len(prices) == 1:
        return 0
    pro =[]
    mini = prices[0]
    for i in range (1, len(prices)):
        if prices[i] < mini:
            mini =prices[i]
        if prices[i] > mini :
            diff = prices[i] - mini
            pro.append(diff)
    if len(pro) == 0:
        return 0
    return max(pro)

prices = list(map(int, input().split()))
result = maxProfit(prices)
print(result)