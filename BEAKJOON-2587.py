def solution():
    import sys

    li = []

    for _ in range(5):
        li.append(int(sys.stdin.readline()))

    li.sort()

    print(sum(li)//5)
    print(li[2])


if __name__ == "__main__":
    solution()