def greedy_knapsack(p,w,m,n):
    total_profit = 0
    fraction = [0] * n

    pi_wi = [p / w for p, w in zip(p, w)]
    indices = sorted(range(len(pi_wi)), key=lambda i: pi_wi[i], reverse=True)

    rc = m

    for i in indices:
        if w[i] <= rc:
            fraction[i] = 1
            total_profit += p[i]
            rc -= weights[i]
        else:
            fraction[i] = rc / w[i]
            total_profit += p[i] * fraction[i]
            break
    print(f"Fractions Are {fraction}")
    return total_profit


profits = [100,20,60,40]
weights = [3,2,4,1]
capacity = 5

total_profit = greedy_knapsack(profits, weights, capacity, len(profits))
print("Total profit:", total_profit)