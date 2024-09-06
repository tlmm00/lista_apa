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
        
        while(len(num_pizzas) > 0):
            l = []
            for i in range(len(num_pizzas)):
                l.append(dist[i]/num_pizzas[i])
            
            id_max = l.index(max(l))

            max_dist = dist[id_max]
            min_pizza = num_pizzas[id_max]

            if(total_roberto + min_pizza > p):
                break

            total_time += max_dist
            total_roberto += min_pizza
            
            dist.pop(id_max)
            num_pizzas.pop(id_max)
            

        print(total_time, " min.")

while(True):
    main()