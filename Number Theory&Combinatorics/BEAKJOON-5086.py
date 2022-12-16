def solution():
    import sys

    input_ = sys.stdin.readline

    while 1:
        a, b = map(int, input_().split())

        if not a:
            break

        if b % a == 0:
            print("factor")
        elif a % b == 0:
            print("multiple")
        else:
            print("neither")

if __name__ == "__main__":
    solution()