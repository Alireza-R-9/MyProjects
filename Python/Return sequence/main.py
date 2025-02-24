def precompute(max_n):
    memo = {1: 2}
    for i in range(2, max_n + 1):
        prev = memo[i - 1]
        if i % 2 == 0:
            result = (prev // 2) * ((prev + 1) // 2)
        else:
            result = prev - 4
        memo[i] = result
    return memo


def main():
    t = int(input())
    queries = [int(input()) for _ in range(t)]
    max_n = max(queries)
    memo = precompute(max_n)

    results = [str(memo[n]) for n in queries]
    print("\n".join(results))


if __name__ == "__main__":
    main()