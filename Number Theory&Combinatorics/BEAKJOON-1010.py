# https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients


def fectorial(x):
    ans = 1
    for i in range(2, x + 1):
        ans *= i
    return ans


def solution():
    import sys

    input_ = sys.stdin.readline

    t = int(input_())

    for _ in range(t):
        n, m = map(int, input_().split())

        print(fectorial(m) // (fectorial(n) * fectorial(m - n)))


if __name__ == "__main__":
    solution()
