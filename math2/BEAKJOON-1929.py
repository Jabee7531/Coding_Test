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

    min, max = map(int, sys.stdin.readline().split())

    for target in range(min,max+1):
        if is_prime(target):
            print(target)
        


if __name__ == "__main__":
    solution()