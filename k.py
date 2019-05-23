N=list(map(int,input().split()))
n=N[0]
k=N[1]
s=0
ar=list(map(int,input().split()))
for i in range(k):
    s+=ar[i]
print(s)