def solution():
    import sys

    input_ = sys.stdin.readline

    a, b = map(int, input_().split())

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    print(gcd(a, b))
    print(lcm(a, b))


if __name__ == "__main__":
    solution()