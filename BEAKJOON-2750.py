def bubble_sort(li: list) -> list:
    n = len(li)

    for x in range(n-1):
        for y in range(n-x-1):
            if li[y] > li[y+1]:
                li[y],li[y+1] =li[y+1],li[y]
    
    return li


def selection_sort(li:list) -> list:
    n = len(li)

    for x in range(n-1):
        min_index = x
        for y in range(n-x-1):
            if li[min_index] > li[y+x+1]:
                min_index = y+x+1
        li[x], li[min_index] = li[min_index], li[x]

    return li

def solution():
    import sys
    
    n = int(sys.stdin.readline())

    li = []

    for _ in range(n):
        li.append(int(sys.stdin.readline()))    
    
    # result = sorted(li)
    # result = bubble_sort(li)
    result = selection_sort(li)

    for x in result:
        print(x)

if __name__ == "__main__":
    solution()