def solution():
    import sys

    x,y = map(int, sys.stdin.readline().split())

    a = []
    b = []

    for _ in range(x):
        data = list(map(int, sys.stdin.readline().split()))
        a.append(data)

    for _ in range(x):
        data = list(map(int, sys.stdin.readline().split()))
        b.append(data)

    for i in range(x):
        for j in range(y):
            print( a[i][j] + b[i][j] , end=' ')
        print()

if __name__ == "__main__":
    solution()