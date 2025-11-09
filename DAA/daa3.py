# Fractional Knapsack Problem using Greedy Strategy

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    # Calculate value/weight ratio and sort items in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  # total profit
    remaining_capacity = capacity

    for item in items:
        if item.weight <= remaining_capacity:
            # take the whole item
            total_value += item.value
            remaining_capacity -= item.weight
        else:
            # take fraction of the item
            fraction = remaining_capacity / item.weight
            total_value += item.value * fraction
            remaining_capacity = 0
            break  # bag is full

    return total_value

# ------------- MAIN PROGRAM -------------
n = int(input("Enter number of items: "))
items = []

for i in range(n):
    value = float(input(f"Enter value of item {i+1}: "))
    weight = float(input(f"Enter weight of item {i+1}: "))
    items.append(Item(value, weight))

capacity = float(input("Enter knapsack capacity: "))

max_value = fractional_knapsack(items, capacity)
print(f"\nMaximum total value in knapsack = {max_value:.2f}")
