def sortf(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    result = sortf(arr)
    print(result)
