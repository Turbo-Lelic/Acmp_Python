arr = list(map(int, input().split()))
costs = arr[:3]
bars = arr[3:]
costs.sort()
bars.sort()

print(costs[0] * bars[0] + costs[1] * bars[1] + costs[2] * bars[2])