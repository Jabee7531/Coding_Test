def solution():
    import sys

    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    
    sorted_li = sorted(list(set(arr)))
    
    dic = { sorted_li[i] : i for i in range(len(sorted_li)) }
    
    for x in range(n):
        print(dic[arr[x]], end = ' ')

if __name__ == "__main__":
    solution()