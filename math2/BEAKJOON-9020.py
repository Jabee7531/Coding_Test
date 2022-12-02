def is_prime(target):
    if target == 1:
        return False
    else:
        for x in range(2,int(target**0.5)+1):
            if target % x == 0:
                return False

        return True

def solution():
    import sys

    n = int(sys.stdin.readline())

    for _ in range(n):
        input = int(sys.stdin.readline())

        a,b = input//2 , input//2

        while 1:
            if is_prime(a) and is_prime(b):
                print(a,b)
                break
            else:
                a-=1
                b+=1

if __name__ == "__main__":
    solution()