wt,pok=input().split()
r12=abs(len(pok)-len(wt))
for k11 in range(len(wt)):
    if(len(pok)==1 and pok[k11] in wt):
        break
    if(wt[k11]!=pok[k11]):
        r12=r12+1
print(r12)
