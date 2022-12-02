def solution():
    import sys

    input_ = sys.stdin.readline
    n = int(input_())
    result = 0

    for x in range(1, n+1):
        sum = 0
        for y in str(x):
            sum += int(y)
        if sum+x == n:
            result = x
            break       

    print(result)
if __name__ == "__main__":
    solution()