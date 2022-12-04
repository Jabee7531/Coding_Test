def solution1():
    import sys

    input_ = sys.stdin.readline

    list_ = [0 for _ in range(-10000000, 10000001)]

    n = int(input_())
    list_n = list(map(int, input_().split()))

    for x in range(n):
        list_[list_n[x]-1] = 1

    m = int(input_())
    list_m = list(map(int, input_().split()))

    for x in range(m):
        print(list_[list_m[x]-1], end=" ")

def solution2():
    import sys

    input_ = sys.stdin.readline

    dict_ = {}

    n = int(input_())
    list_n = list(map(int, input_().split()))
    
    m = int(input_())
    list_m = list(map(int, input_().split()))

    for x in list_n:
        dict_[x] = 1

    for x in range(m):
        if list_m[x] in dict_:
            print("1", end=" ")
        else:
            print("0", end=" ")

if __name__ == "__main__":
    solution2()