def recursion(s, l, r):
    if l >= r: 
        return f'1 {l + 1}'
    elif s[l] != s[r]: 
        return f'0 {l + 1}'
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def solution():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        text = input().rstrip()
        print(isPalindrome(text))


if __name__ == "__main__":
    solution()