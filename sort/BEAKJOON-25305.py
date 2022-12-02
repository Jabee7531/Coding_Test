def solution():
    import sys

    n, k = map(int,sys.stdin.readline().split())
    li = list(map(int,sys.stdin.readline().split()))

    li.sort()

    print(li[n-k])

if __name__ == "__main__":
    solution()