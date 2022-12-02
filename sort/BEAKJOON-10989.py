def solution():
    import sys

    n = int(sys.stdin.readline())
    li = [0 for _ in range(10001)]

    for _ in range(n):
        li[int(sys.stdin.readline())] += 1


    for x in range(1,10001):
        if li[x] != 0:
            for _ in range(li[x]):
                print(x)


if __name__ == "__main__":
    solution()