def solution():
    import sys

    input_ = sys.stdin.readline

    x, y, w, h = map(int, input_().split())

    print(min(w-x, h-y,x,y))
    
if __name__ == "__main__":
    solution()