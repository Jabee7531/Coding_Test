def solution():
    import sys
    
    input = sys.stdin.readline
    n = int(sys.stdin.readline())


    li = []

    for _ in range(n):
        li.append(int(input()))

    li.sort()

    counter = [ 0 for _ in range(-4000,4001)]
    count = 0

    for x in li:
        x += 4000

        counter[x] += 1

    max_count = max(counter)
    max_index = 0

    for idx, x in enumerate(counter):
        if max_count == x:
            count += 1
            max_index = idx
            if count == 2:
                print(round(sum(li)/n))
                print(li[n//2])
                print(idx - 4000)
                print(li[-1]-li[0])

                break

    if count == 1:
        print(round(sum(li)/n))
        print(li[n//2])
        print(max_index-4000)
        print(li[-1]-li[0])


if __name__ == "__main__":
    solution()