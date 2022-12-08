def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map(int, input_().split())
    dict_n = {}
    list_ = []

    for _ in range(n):
        dict_n[input_().rstrip()] = 1
    for _ in range(m):
        data = input_().rstrip()
        if data in dict_n:
            list_.append(data)

    list_.sort()

    print(len(list_))
    for x in list_:
        print(x)


if __name__ == "__main__":
    solution()