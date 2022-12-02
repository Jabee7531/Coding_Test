def solution():
    import sys

    input_ = sys.stdin.readline

    n = int(input_())
    list_ = []
    ranks = []

    for _ in range(n):
        x,y = map(int,input_().split())
        list_.append([x,y])
    
    for x in range(n):
        rank = 1
        for y in range(n):
            if list_[x][0] < list_[y][0] and list_[x][1] < list_[y][1] :
                rank += 1

        ranks.append(rank)

    for x in ranks:
        print(x,end = " ")


if __name__ == "__main__":
    solution()