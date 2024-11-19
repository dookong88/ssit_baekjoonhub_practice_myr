N,M=map(int,sorted(input().split()))
chocolate=0
for i in range(0,M):
    for j in range(0,N):
        chocolate+=1
print(chocolate-1)