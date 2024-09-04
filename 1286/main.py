def main():
    # try:
        n = int(input())
        if(n==0):
            quit()

        p = int(input())

        dist = []
        num_pizzas = []
        for i in range(n):
            d = input().split()
            dist.append(int(d[0]))
            num_pizzas.append(int(d[1]))

        total_roberto = 0
        total_time = 0
        
        while(True):
            min_pizza = min(num_pizzas)

            # if(len([x.index for x in num_pizzas if x==min_pizza]) > 1):
            #     ds = [int(x) for x in dists if x.index in [x.index for x in num_pizzas if x==min_pizza]]
            #     min_pizza = num_pizzas.index(dists.index(max(ds)))
            
            if(total_roberto + min_pizza > p):
                break

            total_time += dist[num_pizzas.index(min_pizza)]
            total_roberto += min_pizza

            dist.remove(dist[num_pizzas.index(min_pizza)])
            num_pizzas.remove(min_pizza)


        print(total_time, " min.")
    # except:
    #     quit()

while(True):
    main()