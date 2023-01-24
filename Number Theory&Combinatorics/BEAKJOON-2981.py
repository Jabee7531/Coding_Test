def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution():
    import sys

    input_ = sys.stdin.readline

    ans = []
    
    n = int(input_())
    list_ = list(int(input_()) for _ in range(n))

    list_.sort()

    prev_ = list_[1] - list_[0]
    for i in range(1, n-1):
        prev_ = gcd(prev_, list_[i+1]- list_[i])

    for i in range(2,int(prev_** 0.5)+1):
        if prev_ % i ==0:
            ans.append(i)
            ans.append(prev_//i)
    ans.append(prev_)

    ans = list(set(ans))
    ans.sort()
    print(*ans)

if __name__ == "__main__":
    solution()