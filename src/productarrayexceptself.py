# Given an array arr[] of n integers, construct a product array res[] (of the same size) such
# that res[i] is equal to the product of all the elements of arr[] except arr[i].
#
# Example:
#
# Input: arr[] = [10, 3, 5, 6, 2]
# Output: [180, 600, 360, 300, 900]
# Explanation:
#
# For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
# For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
# For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
# For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
# For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
# Input: arr[] = [12, 0]
# Output: [0, 12]
# Explanation:
#
# For i = 0, res[i] = 0.
# For i = 1, res[i] = 12.

#bruteforce
def productarray(arr):
    n=len(arr)

    res=[1]*n

    #[1,1,1,1,1]
    for i in range(n):
        for j in range(n):
            if i!=j:
                res[i]= res[i]*arr[j]

    return res

if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    print(productarray(arr))

#little optimised approach using prefix and postfix
def productsubarray(arr):
    n=len(arr)
    prefix_arr=[1]*n
    posix_arr=[1]*n
    prefix=1
    postfix=1
    final_array=[]
    for i in range(n):
        prefix=prefix*arr[i]
        prefix_arr[i]=prefix
        postfix=postfix*arr[n-1-i]
        posix_arr[n-1-i]=postfix
    for i in range(n):
        if i==0:
            final_array.append(1*posix_arr[i+1])
        elif i==n-1:
            final_array.append(prefix_arr[i-1]*1)
        else:
            final_array.append(prefix_arr[i-1]*posix_arr[i+1])
    return final_array


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    print(productsubarray(arr))



