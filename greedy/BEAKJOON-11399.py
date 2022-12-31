def solution():
    import sys

    input_ = sys.stdin.readline
    n = int(input_())
    list_ = list(map(int,input_().split()))

    dict_ = {}
    sum = 0
    for i in range(n):
        dict_[i] = list_[i]

    sorted_dict=sorted(dict_.items(),key=lambda x: x[1])

    for i, x in enumerate(sorted_dict):
        sum += x[1]*(n-i)

    print(sum)

if __name__ == "__main__":
    solution()