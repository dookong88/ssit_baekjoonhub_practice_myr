A,B=map(int,sorted(input().split()))
if(A!=0 and B!=0):
    m=1
else:
    m=0
for i in range(A,0,-1):
    if(A%i==0 and B%i==0):
        A//=i
        B//=i
        m=m*i     
print(m)
print(m*A*B)
