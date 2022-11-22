def solution(list, target):
    
    return list.count(target)

if __name__ == "__main__":
    import sys

    count = int(sys.stdin.readline())
    list = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    result = solution(list,target)
    
    print(result)