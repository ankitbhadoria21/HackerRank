#!/usr/bin
def find_ceil(mem,val,start,end):
	while end-start>1:
		mid=int(start+(end-start)/2)
		if mem[mid]>=val:
			end=mid
		else: start=mid
	return end
	
def solve(arr,n):
	if n==1:
		return 1;
	mem=[0 for x in range(n)]
	mem[0]=arr[0]
	len=1
	for i in range(1,n):
		if arr[i]<mem[0]:
			mem[0]=arr[i]
		elif arr[i]>mem[len-1]:
			mem[len]=arr[i]
			len=len+1
		else: 
			mem[find_ceil(mem,arr[i],-1,len-1)]=arr[i]
	return len

n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))

print(solve(arr,n))
