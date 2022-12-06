def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map(int,input_().split())

    dict_ = {}

    for i in range(1, n+1):
        data = input_().rstrip()
        dict_[data] = i
        dict_[i] = data


    for _ in range(m):
        ask = input_().rstrip()

        if ask.isnumeric():
            print(dict_[int(ask)])
        else:
            print(dict_[ask])

if __name__ == "__main__":
    solution()