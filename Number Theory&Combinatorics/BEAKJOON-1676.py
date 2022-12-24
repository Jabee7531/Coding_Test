def fectorial(x):
    ans = 1
    for i in range(2, x + 1):
        ans *= i
    return ans


def solution():
    import sys

    input_ = sys.stdin.readline

    n = int(input_())

    num = str(fectorial(n))

    count = 0

    for x in range(1, len(num)):
        if num[-x] != "0":
            break

        count += 1

    print(count)


if __name__ == "__main__":
    solution()
