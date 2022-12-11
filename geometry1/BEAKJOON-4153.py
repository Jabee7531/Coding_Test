def solution():
    import sys

    input_ = sys.stdin.readline
    list_ = []

    k = int(input_())

    for _ in range(6):
        list_.append(list(map(int,input_().split())))
    
    max_x_index = list_.index(max(list_, key = lambda x: x[1]))

    x_before_index = max_x_index-1
    x_next_index = max_x_index+1 if max_x_index < 5 else 0

    max_y_index = list_.index(max(list_[x_before_index], list_[x_next_index], key = lambda x: x[1]))

    y_before_index = max_y_index-1
    y_next_index = max_y_index+1 if max_y_index < 5 else 0

    max_box = list_[max_x_index][1] * list_[max_y_index][1]
    min_box = abs(list_[x_before_index][1]-list_[x_next_index][1])*abs(list_[y_before_index][1]-list_[y_next_index][1])
    
    print((max_box-min_box)*k)

if __name__ == "__main__":
    solution()