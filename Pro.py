mo=int(input())
q1=[]
for i in range(0,mo):
    r1=input()
    q1.append(r1)
s1=[]
for i in zip(*q1):
    if(i.count(i[0])==len(i)):
        s1.append(i[0])
    else:
        break
print(''.join(s1))
        
