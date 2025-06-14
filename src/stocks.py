# Given an array prices[] of length N, representing the prices of the stocks on different days,
# the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.
# Here one transaction means 1 buy + 1 Sell.
#
# Note: Stock must be bought before being sold.
#
# Examples:
#
# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9.
#
# Input: prices[] = {7, 6, 4, 3, 1}
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.
#
# Input: prices[] = {1, 3, 6, 9, 11}
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]

#bruteforce
def max_profit(prices):
    diff=[-1]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            diff_value=prices[j] - prices [i]
            print(diff_value)#debugging
            if diff_value > 0 and diff_value > max(diff):
                diff.append(diff_value)
                print("buy for {} and sell for {} to gain profit of {}".format(prices [i],prices [j],diff_value))
                final_value= (prices [i],prices [j],diff_value)
    return final_value

if __name__ == "__main__":
    prices=[7, 10, 1, 3, 6, 9, 2]
    prceslen=len(prices)-1
    if prices[0]==max(prices):
        print("since array is sorted in descending order, there will always be loss")
    elif prices[prceslen] == max(prices) and prices[0]== min(prices):
        print("buy for {} and sell for {} to gain profit of {}".format(prices[0],prices[prceslen],prices[prceslen]-prices[0]))
    else:
        abc=max_profit(prices)
        print(abc)
# #Time Complexity: O(n²), for using two nested loops
# #Space Complexity: O(1), no extra space is used except for the input array
# Optimized approach
def optimised_stocks(prices):
    min_price=float("inf")
    max_profit=0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price=prices[i]
            max_profit=max(prices[i]-min_price,max_profit)
        else:
            max_profit=max(prices[i]-min_price,max_profit)
        print(prices[i],min_price,max_profit)
    return max_profit
if __name__ == "__main__":
    prices=[7, 10, 1, 3, 6, 9, 2]
    prceslen=len(prices)-1
    if prices[0]==max(prices):
        print("since array is sorted in descending order, there will always be loss")
    elif prices[prceslen] == max(prices) and prices[0]== min(prices):
        print("buy for {} and sell for {} to gain profit of {}".format(prices[0],prices[prceslen],prices[prceslen]-prices[0]))
    else:
        abc=optimised_stocks(prices)
        print(abc)
# Time Complexity: O(n), for using a single loop
# Space Complexity: O(1), no extra space is used except for the input array





