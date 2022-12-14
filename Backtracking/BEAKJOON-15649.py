def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map(int, input_().split())

    s = []

    def dfs():
        if len(s) == m:
            print(" ".join(map(str, s)))
            return

        for i in range(1, n + 1):
            if i not in s:
                s.append(i)
                dfs()
                s.pop()

    dfs()


if __name__ == "__main__":
    solution()
