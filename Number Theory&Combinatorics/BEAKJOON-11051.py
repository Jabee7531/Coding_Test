def factorial(n: int) -> int:
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def solution():
    import sys

    input_ = sys.stdin.readline

    n, k = map(int, input_().split())

    result = factorial(n) // (factorial(k) * factorial(n - k))

    print(result % 10007)


if __name__ == "__main__":
    solution()
