import itertools
import sys

def main(): 
    try:
        nm = [int(x) for x in input().split()]
        n = nm[0]
        m = nm[1]

        c_list = [int(x) for x in input().split()]
    
    except:
        exit()

    possible_combinations = list(itertools.product(range(1, m+1), repeat=n))

    # print(possible_combinations)
    possible_results = []
    for combination in possible_combinations:
        res = 0
        for i in range(n):
            res += c_list[i] * combination[i]
        
        
        if(res in possible_results):
            print("Try again later, Denis...")
            return
        else:
            possible_results.append(res)

    print("Lucky Denis!")

while(True):
    main()