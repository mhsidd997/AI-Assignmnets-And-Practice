import random
arr=[]
print("Random Numbers:")
for i in range(100):
    arr.append(random.randint(1,1000))
print(arr)
minarr=0
minarr=arr[0]
for i in range(100):
    if arr[0] > arr[i]:
        indmin=i+1
        arr[0]=arr[i]
        arr[i]=minarr
print("\nSmallest Number in Randoms:",arr[0],"at:",indmin)
maxarr=0
maxarr=arr[0]
for i in range(100):
    if arr[0] < arr[i]:
        indmax=i+1
        arr[0]=arr[i]
        arr[i]=maxarr
print("\nLargest Number in Randoms:",arr[0],"at:",indmax)
sumarr=0
for i in range(100):
    sumarr+=arr[i]
print("\nTotal Sum:",sumarr)
meanarr=sumarr/len(arr)
print("Mean:",meanarr)