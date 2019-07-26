a=int(input())
b=0
l=[]
for a in range(1,a+1):
    l.append(a)
for a in range(len(l)):
    for a in range(a+1,len(l)):
        b+=1
print(b)
