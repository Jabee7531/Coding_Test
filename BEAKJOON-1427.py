def solution():
    import sys

    li = list(sys.stdin.readline().rstrip())
    
    for x in sorted(li,reverse=True):
        print(x,end='')


if __name__ == "__main__":
    solution()