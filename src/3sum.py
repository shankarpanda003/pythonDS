# 3 Sum - Find All Triplets with Zero Sum
# Given an array arr[], the task is to find all possible indices
# {i, j, k} of triplet {arr[i], arr[j], arr[k]} such that their sum is equal to zero and
# all indices in a triplet should be distinct (i != j, j != k, k != i).
# We need to return indices of a triplet in sorted order, i.e., i < j < k.
#
# Examples :
#
# Input: arr[] = {0, -1, 2, -3, 1}
# Output: {{0, 1, 4}, {2, 3, 4}}
# Explanation:  Two triplets with sum 0 are:
#     arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
# arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0
#
# Input: arr[] = {1, -2, 1, 0, 5}
# Output: {{0, 1, 2}}
# Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0
#
# Input: arr[] = {2, 3, 1, 0, 5}
# Output: {{}}
# Explanation: There is no triplet with sum 0

#bruteforce
def threesum_bruteforce(arr,target):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] ==  target:
                    res.append((i,j,k))
    return res

if __name__ == "__main__":
    arr=[0, -1, 2, -3, 1]
    target=0
    print(threesum_bruteforce(arr,target))


def threepointersum(arr,target):
    orig_arr=arr
    arr=sorted(arr)
    char_index=[]
    print(arr)
    for i in range(len(arr)-2):
        lookforsum=target-arr[i]
        print('lookforsum',lookforsum)
        left=i+1
        right=len(arr)-1
        print(left,right)
        while left<right:
            print(arr[left],arr[right])
            if arr[left]+arr[right] ==  lookforsum:
                char_index.append([orig_arr.index(arr[i]),orig_arr.index(arr[left]),orig_arr.index(arr[right])])
                break
            elif arr[left]+arr[right] > lookforsum:
                right = right-1
            else:
                left= left+1
    return char_index

if __name__ == "__main__":
    arr=[2, 3, 1, 0, 5]
    target=0
    print(threepointersum(arr,target))


def threepointersum(arr, target):
    res = set()
    n = len(arr)
    val_to_indices = {}
    for idx, val in enumerate(arr):
        val_to_indices.setdefault(val, []).append(idx)
    arr_sorted = sorted(arr)
    for i in range(n - 2):
        if i > 0 and arr_sorted[i] == arr_sorted[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = arr_sorted[i] + arr_sorted[left] + arr_sorted[right]
            if s == target:
                vals = [arr_sorted[i], arr_sorted[left], arr_sorted[right]]
                indices = []
                used = set()
                for v in vals:
                    for idx in val_to_indices[v]:
                        if idx not in used:
                            indices.append(idx)
                            used.add(idx)
                            break
                indices.sort()
                res.add(tuple(indices))
                left_val, right_val = arr_sorted[left], arr_sorted[right]
                while left < right and arr_sorted[left] == left_val:
                    left += 1
                while left < right and arr_sorted[right] == right_val:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return list(res)

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = 0
    print(threepointersum(arr, target))  # Output: [(0, 1, 4), (2, 3, 4)]
