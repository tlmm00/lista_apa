def quick_sort(l):
    if(len(l) <= 1):
        return l
    else:
        pivot = l[len(l) // 2]
        left = [p for p in l if p < pivot]
        middle = [p for p in l if p == pivot]
        right = [p for p in l if p > pivot]

        return quick_sort(left) + middle + quick_sort(right)

def main():
    nc = int(input())
    while(nc):
        nc-=1

        n = int(input())
        height_list = [int(x) for x in input().split()]

        print(' '.join(str(e) for e in quick_sort(height_list)))

main()