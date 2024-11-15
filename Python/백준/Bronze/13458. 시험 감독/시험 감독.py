import math
N=int(input())
Ai=list(map(int,input().split()))
B,C=map(int,input().split())
G=0
for i in range(0,N):
    if(Ai[i]>=B):
        G+=math.ceil((Ai[i]-B)/C)+1
    else:
        G+=1        
print(int(G))