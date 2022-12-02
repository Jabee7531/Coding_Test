def solution():
    import sys

    m = 0
    x_index,y_index = 1,1

    for i in range(9):
        li = list(map(int, sys.stdin.readline().split()))
        if m < max(li):
            m = max(li)
            x_index = i + 1
            y_index = li.index(m) + 1

    print(m)
    print(x_index,y_index)


if __name__ == "__main__":
    solution()