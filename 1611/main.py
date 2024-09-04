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
    try:
        T = int(input())
        while T>0:
            T-=1
            
            ncm = [int(x) for x in input().split()]
            n = int(ncm[0])
            c = int(ncm[1])
            m = int(ncm[2])
            
            list_andares = [int(x) for x in input().split()]
            list_andares_sorted = quick_sort(list_andares)

            res = 0
            i = 0
            while i < m:
                c_andares = list_andares_sorted[i:i+c]
                res += 2*max(c_andares)
                i+=c
                
            print(res)
    except:
        quit()

while(True):
    main()