def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map(int,input_().split())
    arr = list(map(int, input_().split()))

    max_ = 0

    for x in range(len(arr)-2):
        for y in range(len(arr)-x-2):
            for z in range(len(arr)-x-y-2):
                sum = arr[x]+arr[x+y+1]+arr[x+y+z+2]
                if sum <= m and sum > max_:
                    max_ = sum

    print(max_)

if __name__ == "__main__":
    solution()