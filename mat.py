import math
n,m=map(int,input().split())

cen=math.ceil(n/2)
t=1
for i in range(cen):
    if(i== cen-1):
        print("WELCOME".center(m,'-'))
    else: 
           
        print((t*".|.").center(m,'-'))
        t+=2
for i in range(cen-1):
    
    t-=2
    print((t*".|.").center(m,'-'))
