def solution():
    import sys

    input_ = sys.stdin.readline

    list_ = list(input_().rstrip().split("-"))    

    splited_list = []

    for x in list_:
        splited_list.append(sum(map(int,x.split("+"))))

    result = splited_list[0] 

    for i in range(1,len(splited_list)):
        result -= splited_list[i]

    print(result)


if __name__ == "__main__":
    solution()
