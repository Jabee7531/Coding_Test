def solution():
    import sys

    n = int(sys.stdin.readline())
    li = {}

    for _ in range(n):
        li[sys.stdin.readline().rstrip()] =1

    li =list(li.keys())
    li.sort(key=str)
    li.sort(key=len)

    print("\n".join(li))


if __name__ == "__main__":
    solution()