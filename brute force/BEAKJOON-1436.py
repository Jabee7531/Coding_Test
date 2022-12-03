def check(name: int) -> bool:
    str_name = str(name)

    for x in range(len(str_name)-2):
        if str_name[x] == '6' and str_name[x+1] == '6' and str_name[x+2] == '6':
            return True
        
    return False

def solution():
    import sys

    input_ = sys.stdin.readline
    n = int(input_())

    name = 666

    for _ in range(n-1):
        while 1:
            name +=1
            if check(name):
                break
    print(name)

if __name__ == "__main__":
    solution()