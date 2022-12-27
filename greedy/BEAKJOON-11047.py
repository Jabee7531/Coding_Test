def solution():
    import sys

    input_ = sys.stdin.readline

    n, k = map(int, input_().split())
    coins = []
    count = 0

    for i in range(n):
        coins.append(int(input_()))

    for i in range(1, n + 1):
        while coins[-i] <= k:
            count += k // coins[-i]
            k = k % coins[-i]
        if k == 0:
            break

    print(count)


if __name__ == "__main__":
    solution()
