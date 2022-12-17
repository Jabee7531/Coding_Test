def solution():
    import sys

    input_ = sys.stdin.readline

    n = int(input_())
    list_ = list(map(int, input_().split()))

    print(min(list_)*max(list_))

def solution():
    import sys

    input_ = sys.stdin.readline

    n = int(input_())
    list_ = list(map(int, input_().split()))

    list_.sort()

    print(list_[0] * list_[-1])

if __name__ == "__main__":
    solution()