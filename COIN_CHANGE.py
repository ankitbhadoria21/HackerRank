#!/usr/bin

def solve(arr,n):
	mem=[[0 for y in range(len(arr))] for x in range(n+1)];
	for i in range(len(arr)):
		mem[0][i]=1
	for i in range(1,n+1):
		for j in range(len(arr)):
			p=int(arr[j])
			x=mem[i-p][j] if i-p>=0 else 0 
			y=mem[i][j-1] if j>=1 else 0
			mem[i][j]=x+y
	return mem[n][len(arr)-1]
str=input()
n,m=str.split()
str=input()
lst=str.split()
print(solve(lst,int(n)))
