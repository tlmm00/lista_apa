def main():
    # try:
        n = int(input()) # qtt pizzas
        if(n==0):
            quit()

        p = int(input()) # Roberto max

        dist = [] # delivery time list
        num_pizzas = [] # delivery qtt list
        for i in range(n):
            d = input().split()
            dist.append(int(d[0]))
            num_pizzas.append(int(d[1]))

        total_roberto = 0
        total_time = 0
        
        while(True):
            min_pizza = min(num_pizzas)

            if(len([x for x in num_pizzas if x==min_pizza]) > 1):
                ds = []
                
                # ds = [dist[j] for j in range(len(dist)) if dist[j] in
                #  [num_pizzas[i] for i in range(len(num_pizzas)) if num_pizzas[i]==min_pizza]]
                print(ds)
                min_pizza = num_pizzas.index(dist.index(max(ds)))
            
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