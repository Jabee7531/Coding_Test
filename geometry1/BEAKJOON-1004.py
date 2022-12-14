def solution():
    import sys

    input_ = sys.stdin.readline

    t = int(input_())

    for _ in range(t):
        count = 0
        
        x1, y1, x2, y2 = map(int,input_().split())
        n = int(input_())

        for _ in range(n):
            x, y, r = map(int,input_().split())
                    
            d1 = (((x1 - x) ** 2) + ((y1 - y) ** 2)) ** 0.5
            d2 = (((x2 - x) ** 2) + ((y2 - y) ** 2)) ** 0.5
            if (d1 < r and d2 > r) or (d1 > r and d2 < r):
                count += 1

        print(count)

if __name__ == "__main__":
    solution()