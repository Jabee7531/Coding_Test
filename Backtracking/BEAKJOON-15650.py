def solution():
    import sys

    input_ = sys.stdin.readline

    n, m = map(int, input_().split())

    s = []

    def dfs(x):
        if len(s) == m:
            print(" ".join(map(str, s)))
            return

        for i in range(x, n + 1):
            if i not in s:
                s.append(i)
                dfs(i+1)
                s.pop()

    dfs(1)


if __name__ == "__main__":
    solution()
