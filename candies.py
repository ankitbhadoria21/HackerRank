#!/usr/bin

def solve(arr):
	mem=[1 for x in range(len(arr))]
	for i in range(len(arr)-1):
		if arr[i+1]>arr[i]:	
			mem[i+1]=mem[i]+1;
	for i in range(len(arr)-1,0,-1):
		if arr[i-1]>arr[i] and mem[i]+1>mem[i-1]:
			mem[i-1]=mem[i]+1;
	return sum(mem)

n=int(input())
arr=[]
for i in range(n):
	n=int(input())
	arr.append(n)
print(solve(arr))
