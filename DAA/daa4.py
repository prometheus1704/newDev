# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ------------- MAIN PROGRAM -------------
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    values.append(int(input(f"Enter value of item {i+1}: ")))
    weights.append(int(input(f"Enter weight of item {i+1}: ")))

capacity = int(input("Enter knapsack capacity: "))

max_value = knapsack(values, weights, capacity)
print(f"\nMaximum total value in knapsack = {max_value}")
