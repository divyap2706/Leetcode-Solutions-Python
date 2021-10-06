def reverse_arr(arr):
    sum=0
    rev_arr=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        while(arr[i]>0):
            rev_arr[i]=rev_arr[i]*10+arr[i]%10
            arr[i]=arr[i]//10
        sum+=rev_arr[i]
    return sum
        
