N=int(input())
shell=0
shell_max=0
if(N==1):
    shell=1
else:
    while(N>(shell_max+1)):
        shell_max+=shell*6
        shell+=1
print(shell)