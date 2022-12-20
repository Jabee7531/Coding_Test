def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution():
    import sys

    input_ = sys.stdin.readline

    n = int(input_())

    list_ = list(map(int, input_().split()))

    for i in range(1, len(list_)):
        gcd_val = gcd(list_[0], list_[i])
        print(list_[0] // gcd_val, "/", list_[i] // gcd_val, sep="")


if __name__ == "__main__":
    solution()
