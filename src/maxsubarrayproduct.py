# Maximum Product Subarray
# Given an integer array, the task is to find the maximum product of any subarray.
#
# Examples:
#
# Input: arr[] = {-2, 6, -3, -10, 0, 2}
# Output: 180
# Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180
#
# Input: arr[] = {-1, -3, -10, 0, 60}
# Output: 60
# Explanation: The subarray with maximum product is {60}.

#bruteforce
def productsubarray(arr):
    max_product=-float('inf')
    print(max_product)
    for i in range(len(arr)):
        curr_prod=arr[i]
        for j in range(i+1,len(arr)):
            curr_prod=curr_prod*arr[j]
            max_product= max(max_product,curr_prod)
    return max_product

if __name__=="__main__":
    arr=[-2, 6, -3, -10, 0, 2]
    print(productsubarray(arr))

#optimised approach

# maxsubarrayproduct.py

def max_product_subarray(arr):
    min_prd=arr[0]
    max_prd=arr[0]
    res=arr[0]
    for i in range(1,len(arr)):
        if arr[i] < 0:
            max_prd,min_prd=min_prd,max_prd
        max_prd= max(arr[i],arr[i]*max_prd)
        min_prd= min(arr[i],arr[i]*min_prd)
        res=max(res,max_prd)
    return res
if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print(max_product_subarray(arr))  # Output: 180

