with open('input.txt', 'r') as input_file:
    n = int(input_file.readline().strip())
    profit = list(map(int, input_file.readline().split()))
    clicks = list(map(int, input_file.readline().split()))

profit.sort(reverse=True)
clicks.sort(reverse=True)

max_profit = str(sum([profit[i] * clicks[i] for i in range(n)]))


with open('output.txt', 'w') as output_file:
    output_file.write(max_profit)