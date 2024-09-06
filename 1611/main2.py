def minTime(n, k, a) :
     
    # Sort in descending order 
    a.sort(reverse = True); 
     
    minTime = 0; 
 
    # Iterate through the groups 
    for i in range(0, n, k) :
 
        # Update the time taken for 
        # each group 
        minTime += (2 * a[i]); 
 
    # Return the total time taken 
    return minTime; 
 
# Driver code 
if __name__ == "__main__" :
     
    k = 2
    arr = [ 2, 3, 4 ] 
    n = len(arr)
    print(minTime(n, k, arr)) 