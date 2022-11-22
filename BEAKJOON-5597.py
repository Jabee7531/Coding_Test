def solution():
    import sys
    check_list = list(range(1,31))

    for x in range(28):
        check = int(sys.stdin.readline())
        check_list.remove(check)

    for result in check_list:
        print(result)

if __name__ == "__main__":
    solution()