with open('input.txt', 'r') as f:
    n = int(f.readline().strip())


def max_pairwise_sum(n):
    k = 1
    while k * (k + 1) <= 2 * n:
        k += 1
    k -= 1

    result = []
    for i in range(1, k):
        result.append(i)
        n -= i
    result.append(n)

    return k, result


with open('output.txt', 'w') as f:
    k, result = max_pairwise_sum(n)
    f.write(str(k) + '\n')
    f.write(' '.join(map(str, result)))
