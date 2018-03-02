def kSmallest(arr, k):
    arr.sort(reverse=False)
    for i in range(k):
        print (arr[i],end=" ") 
arr = [9,7,6,8,5,3,2,4,1]
k = int(input(""))
kSmallest(arr, k)
