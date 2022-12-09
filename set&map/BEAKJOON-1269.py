def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map(int, input_().split())

    set_n = set(list(map(int, input_().split())))
    set_m = set(list(map(int, input_().split())))

    print(len(set_m^set_n))


if __name__ == "__main__":
    solution()