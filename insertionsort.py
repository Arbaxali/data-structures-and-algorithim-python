def sortedarr(arr):
    lem = len(arr)
    for i in range(1, lem):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j=j-1
    return arr        


arr = [5,4,3,2,1]
print(sortedarr(arr))
