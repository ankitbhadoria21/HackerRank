#!/usr/bin

def solve(arr,i,j,n,m,k):

	if i<0 or j<0 or i>n-1 or j>m-1 or k<0 or (k==0 and arr[i][j]!='*'):
		return 100000
	if arr[i][j]=='*':
		return 0
	if mem[i][j][k]!=-1:
		return mem[i][j][k]
	min_val=100000
	x=solve(arr,i,j+1,n,m,k-1)
	if x!=100000:
		x=x+(0 if arr[i][j]=='R' else 1)
	min_val=min(min_val,x)
	x=solve(arr,i,j-1,n,m,k-1)
	if x!=100000:
		x=x+(0 if arr[i][j]=='L' else 1)
	min_val=min(min_val,x)
	x=solve(arr,i-1,j,n,m,k-1)
	if x!=100000:
		x=x+(0 if arr[i][j]=='U' else 1)
	min_val=min(min_val,x)
	x=solve(arr,i+1,j,n,m,k-1)
	if x!=100000:
		x=x+(0 if arr[i][j]=='D' else 1)
	min_val=min(min_val,x)

	mem[i][j][k]=min_val
	return min_val

n,m,k=input().split()
n=int(n)
m=int(m)
k=int(k)
arr=[[' ' for j in range(m)] for i in range(n)]
for i in range(n):
	str=input()
	arr[i]=list(str)
mem=[[[-1 for i in range(100)] for j in range(100)] for l in range(1010)]
x=solve(arr,0,0,n,m,k)
print(x if x!=100000 else -1)
