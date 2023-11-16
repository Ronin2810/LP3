def knapsack(weights,values,capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<w:
                dp[i][w] = max(dp[i-1][w],values[i-1]+ dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    selected_items=[]
    i,w = n,capacity

    while i>0 and w>0:
        if dp[i][w]!=dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i-=1
    
    return dp[n][capacity], selected_items[::-1]


def get_input():
    while True:
        try:
            weights = list(map(int, input("Enter weights separated by space: ").split()))
            values = list(map(int, input("Enter values separated by space: ").split()))
            capacity = int(input("Enter knapsack capacity: "))
            return weights, values, capacity
        except ValueError:
            print("Invalid input. Please enter integers only. Try again.")


if __name__ == "__main__":
    weights, values, capacity = get_input()
    max_value, selected_items = knapsack(weights, values, capacity)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)