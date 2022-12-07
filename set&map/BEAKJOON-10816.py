def solution():
    import sys

    input_ = sys.stdin.readline

    n = int(input_())
    list_n = list(map(int,input_().split()))
    m = int(input_())
    list_m = list(map(int,input_().split()))

    dict_ = {}

    for x in list_n:
        if x in dict_:
            dict_[x] += 1
        else:
            dict_[x] = 1
    
    for x in list_m:
        print(dict_.get(x,0), end=" ")


if __name__ == "__main__":
    solution()