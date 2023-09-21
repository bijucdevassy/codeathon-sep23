def find_best_days_to_buy_and_sell_stocks(stock_prices):
  """Finds the best days to buy and sell stocks to maximize profit.

  Args:
    stock_prices: A list of stock prices.

  Returns:
    The maximum profit that can be made, or -1 if no profit can be made.
  """

  current_profit = 0
  max_profit = 0
  for i in range(1, len(stock_prices)):
    if stock_prices[i] < stock_prices[i - 1]:
      current_profit = 0
    current_profit += stock_prices[i] - stock_prices[i - 1]
    max_profit = max(max_profit, current_profit)

  if max_profit == 0:
    return -1
  else:
    return max_profit

Use code with caution. Learn more
Here are some test cases for the program:

Python
# Test case 1:
stock_prices = [100, 180, 260, 310, 40, 535, 695]

expected_profit = 865

actual_profit = find_best_days_to_buy_and_sell_stocks(stock_prices)

assert actual_profit == expected_profit

# Test case 2:
stock_prices = [100, 90, 80, 70, 60]

expected_profit = -1

actual_profit = find_best_days_to_buy_and_sell_stocks(stock_prices)

assert actual_profit == expected_profit

# Test case 3:
stock_prices = [100]

expected_profit = -1

actual_profit = find_best_days_to_buy_and_sell_stocks(stock_prices)

assert actual_profit == expected_profit
