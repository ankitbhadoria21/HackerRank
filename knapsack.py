#!/usr/bin
mem=[0 for i in range(2001)]
def solve(arr,n,k):
	for i in range(1,k+1):
		for j in range(n):
			if int(arr[j])>i:continue
			mem[i]=max(mem[i],int(arr[j])+mem[i-int(arr[j])])			

t=int(input())
while t:
	n,k=input().split(" ")
	n=int(n)
	k=int(k)
	arr=input().split(" ")
	solve(arr,n,k)
	print(mem[k])
	mem=[0 for i in range(2001)]
	t-=1
