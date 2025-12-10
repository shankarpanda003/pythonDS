# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
#
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
#
# Output: [1]
#
# Example 3:
#
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#
# Output: [1,2]

def topkfrequentelement(arr,k):
    freq_map={}
    for i in range(len(arr)):
        if arr[i] in freq_map:
            freq_map[arr[i]]+=1
        else:
            freq_map[arr[i]]=1
    sorted_arr=sorted(freq_map.items(), key=lambda x:x[1], reverse=True)
    print([key for key,value in sorted_arr[:k]])

if __name__=="__main__":
    arr = [1,1,1,2,2,3]
    k = 2
    print(topkfrequentelement(arr,k))