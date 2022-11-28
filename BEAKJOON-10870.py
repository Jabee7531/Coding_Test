def fibonacci(n: int) -> int:
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return n


def solution():
    import sys

    input = sys.stdin.readline

    n = int(input())

    print(fibonacci(n))


if __name__ == "__main__":
    solution()