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

    input_list = range(1,123456*2)
    prime_list = []

    for x in input_list:
        if is_prime(x):
            prime_list.append(x)

    while 1:
        count = 0

        input = int(sys.stdin.readline())

        if input == 0:
            break
        
        for x in prime_list:
            if input < x <= input*2:
                count += 1
            
        print(count)
        



if __name__ == "__main__":
    solution()