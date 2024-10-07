def minimum_coins_required(coins, target_amount):
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0

    for i in range(1, target_amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target_amount] if dp[target_amount] != float('inf') else -1

input_file = open('Lab8/input3.txt', 'r')
output_file = open('Lab8/output3.txt', 'w')

n, target_amount = map(int, input_file.readline().strip().split())

coin_values = list(map(int, input_file.readline().strip().split()))

print(minimum_coins_required(coin_values, target_amount), file=output_file)
