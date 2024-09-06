def bubbleSort(arr):
    n = len(arr)
    swaps = 0
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if (swapped == False):
            return swaps


def main():
    n = int(input())

    while(n):
        n-=1
        l = int(input())

        init_order = [int(x) for x in input().split()]
        swaps = bubbleSort(init_order)
        print("Optimal train swapping takes", swaps, "swaps.")
        

    return


main()