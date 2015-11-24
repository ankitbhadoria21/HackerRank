#!/usr/bin

def solve(a,b,n):
	prev=a
	curr=b;
	for i in range(2,n):
		next=curr*curr+prev
		prev=curr
		curr=next
	return curr

s=input()
a,b,n=s.split(" ")
print(solve(int(a),int(b),int(n)))
