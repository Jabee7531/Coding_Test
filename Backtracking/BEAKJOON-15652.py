def solution():
    import sys

    input_ = sys.stdin.readline

    n,m  = map (int, input_().split())
    s = []
    def dfs(start):
        if len(s)==m:
            print(" ".join(map(str,s)))
            return
        
        for i in range(start, n+1):
            s.append(i)
            dfs(i)
            s.pop()

    dfs(1)
    


if __name__ == "__main__":
    solution()
