def is_valid(n, A, B):
    heights = [0] * n
    heights[0] = A
    heights[-1] = B


    for i in range(1, n - 1):
        heights[i] = (heights[i - 1] + heights[i + 1]) / 2 - 1


    zero_count = sum(1 for h in heights if h <= 0)

    return zero_count <= 2

def find_min_b(n, A):
    left, right = 0, A + n
    best_b = right

    while right - left > 1e-7:
        mid = (left + right) / 2
        if is_valid(n, A, mid):
            best_b = mid
            right = mid
        else:
            left = mid

    return best_b


with open('input.txt') as f:
    n, A = map(float, f.readline().strip().split())
    n = int(n)


result = find_min_b(n, A)


with open('output.txt', 'w') as f:
    f.write(f"{result:.10f}\n")
