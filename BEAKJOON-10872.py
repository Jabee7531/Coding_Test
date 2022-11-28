def factorial(n: int) -> int :
    if n > 1:
        return factorial(n-1)*n
    else :
        return 1

def solution():
    import sys

    input = sys.stdin.readline

    n = int(input())
    
    print(factorial(n))


if __name__ == "__main__":
    solution()