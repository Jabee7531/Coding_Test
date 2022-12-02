def solution():
    import sys

    n = int(sys.stdin.readline())
    li = []

    for _ in range(n):
        li.append(list(sys.stdin.readline().split()))

    li.sort(key=lambda x: int(x[0]))

    for x in li:
        print(x[0],x[1])

if __name__ == "__main__":
    solution()