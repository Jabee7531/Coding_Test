def factorial(n: int) -> int:
    if n > 1:
        return factorial(n - 1) * n
    else:
        return 1


def solution():
    import sys

    input_ = sys.stdin.readline

    n, k = map(int, input_().split())

    print(factorial(n) // (factorial(k) * factorial(n - k)))


if __name__ == "__main__":
    solution()
