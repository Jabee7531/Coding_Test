def solution(input):

    return 0

if __name__ == "__main__":
    total = int(input())
    numb = int(input())
    for x in range(numb):
        price, count  = list(map( int, input().split() ))
        total -= price*count
    
    if total == 0:
        print("Yes")
    else:
        print("No")
