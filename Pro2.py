from itertools import combinations
a,b=map(int,input().split())
d=len(str(a))
lst=list(combinations(str(a),d-b))
lst=sorted(lst)
print(*lst[0],sep='')
