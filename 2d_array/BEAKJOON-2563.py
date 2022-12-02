def solution():
    import sys

    n = int(sys.stdin.readline())
    result = 0

    li = [[0 for _ in range(100)] for _ in range(100)]

    for _ in range(n):
        x,y = map(int,sys.stdin.readline().split())
        for i in range(10):
            for j in range(10):
                if li[x+i][y+j] == 0:
                    li[x+i][y+j] = 1
                    result += 1

    print(result)

if __name__ == "__main__":
    solution()