def solution():
    import sys

    input_ = sys.stdin.readline

    count = 0
    n, m = map(int,input_().split())

    list_n = []
    list_m = []

    for _ in range(n):
        list_n.append(input_().rstrip())

    for _ in range(m):
        list_m.append(input_().rstrip())

    for x in list_m:
        if x in list_n:
            count += 1

    print(count)

if __name__ == "__main__":
    solution()