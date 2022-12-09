def solution():
    import sys

    input_ = sys.stdin.readline
    
    s = input_().rstrip()
    set_  =  set()

    for x in range(1, len(s)+1):
         for y in range(len(s)-x+1):
            set_.add(s[y:y+x])
    
    print(len(set_))

    
if __name__ == "__main__":
    solution()