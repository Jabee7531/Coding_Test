def solution():
    import sys

    n = int(sys.stdin.readline())
    li = []

    for _ in range(n):
        li.append(list(map(int, sys.stdin.readline().split())))


    li.sort()

    for i in range(n):
        print(li[i][0],li[i][1])


if __name__ == "__main__":
    solution()