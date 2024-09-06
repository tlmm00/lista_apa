# import numpy as np

def main():
    # try:
        n = int(input()) # qtt pizzas
        if(n==0):
            quit()

        p = int(input()) # Roberto max

        list_entregas = []
        for _ in range(n):
            l = [int(x) for x in input().split()]
            list_entregas.append(l)
        
        # map_final = np.zeros((n,p))
        map_final = [[0 for _ in range(p+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, p+1):
                vi = list_entregas[i-1][0]
                wi = list_entregas[i-1][1]
                if wi > j:
                    map_final[i][j] = map_final[i-1][j]
                else:
                    if map_final[i-1][j-wi] + vi > map_final[i-1][j]:
                        map_final[i][j] = map_final[i-1][j-wi] + vi
                    else:
                        map_final[i][j] = map_final[i-1][j]
        
        print(map_final[n][p], "min.")


while(True):
    main()