from itertools import permutations

Capacity = int(input())  # capacity of bag
BarsGold = list(map(int, input().split()))  # get list of weight bars of gold

Weight = 0
length = len(BarsGold)

for i in permutations(BarsGold, length):  # get combination of choice weight of gold
    currentWeight = 0
    for j in range(length):
        if Capacity >= currentWeight + i[j]:
            currentWeight += i[j]
        if currentWeight > Weight:
            Weight = currentWeight
print("Maximum weight of gold that fits into a knapsack with capacity of " +
      str(Capacity) + " - " + str(Weight))
