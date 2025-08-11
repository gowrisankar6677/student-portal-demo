def binary_search(arr,target):
 left,right=0,len(arr)-1
while left<=right:
 mid=left+(right-left)//2
if mid[arr]==target:
 return mid
elif mid[arr]>target:
 right=mid-1
else:
 left=mid+1
return-1
arr=[1,3,5,7,9,13,15,18]
target=7
result=binary_search(arr,target)
if result!=-1:

 print("successfully found.....search element found",result)
else:
 print("unsuccess")
