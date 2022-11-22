def solution(input):
    arr = [1,1,2,2,2,8]


    return [b-a for a,b in zip(input, arr)]

if __name__ == "__main__":
    input  = map( int, input().split() )
    
    result = solution(input)

    for x in result:
        print(x, end=' ')