def solution():
    import sys

    input_ = sys.stdin.readline

    t = int(input_())
    
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int,input_().split())

        distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

        min_r = min(r1, r2)
        max_r = max(r1, r2)

        if distance == 0 and r1 == r2:
            print(-1)
        elif distance + min_r < max_r:
            print(0)
        elif distance + min_r == max_r:
            print(1)
        elif min_r + max_r < distance:
            print(0)
        elif min_r + max_r == distance:
            print(1)
        elif min_r + max_r > distance:
            print(2)


if __name__ == "__main__":
    solution()