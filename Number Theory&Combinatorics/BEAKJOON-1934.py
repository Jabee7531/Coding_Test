def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution():
    import sys

    input_ = sys.stdin.readline

    t = int(input_())

    for _ in range(t):
        a, b = map(int, input_().split())

        print(a * b // gcd(a, b))


if __name__ == "__main__":
    solution()
