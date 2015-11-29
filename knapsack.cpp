#include<iostream>

using namespace std;
int max_e=0;
void solve(int arr[],int sum,int i,int k,int n)
{
if(i>=n)
return  ;
if(max_e<sum && sum<=k)
max_e=sum;
if(sum+arr[i]>k)
solve(arr,sum,i+1,k,n);
else solve(arr,sum+arr[i],i,k,n);

}

int main()
{
int t,n,k,arr[2000];
cin>>t;
while(t--){
max_e=0;
cin>>n>>k;
for(int i=0;i<n;++i)
cin>>arr[i];
solve(arr,0,0,k,n);
cout<<max_e<<endl;
}
return 0;
}
