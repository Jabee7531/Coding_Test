def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map (int,input_().split())
    list_ = []
    ans1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    ans2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    min = 65

    for _ in range(n):
        list_.append(input_().rstrip())

    for i in range(n-7):
        for j in range(m-7):
            count = 0
            for x in range(8):
                for y in range(8):
                    # print(ans1[x][y], list_[x+i][y+j])
                    if ans1[x][y] != list_[x+i][y+j]:
                        count+=1
            if min > count:
                min = count

    for i in range(n-7):
        for j in range(m-7):
            count = 0
            for x in range(8):
                for y in range(8):
                    # print(ans1[x][y], list_[x+i][y+j])
                    if ans2[x][y] != list_[x+i][y+j]:
                        count+=1
            if min > count:
                min = count

    print(min)


if __name__ == "__main__":
    solution()