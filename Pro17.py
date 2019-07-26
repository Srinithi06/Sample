ccom,ddom=map(int,input().split())
l=list(map(int,input().split()))
b=0
for i in range(0,ccom):
    for j in range(1,ccom):
        if l[i]+[j]==ddom and i!=j:
            b=1
            break
 print("yes" if b else "no")
