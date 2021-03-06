from array import *
def a2(m,n):
    if((m=="[")and(n=="]")):
        return 0
    elif((m=="(")and(n==")")):
        return 0
    elif((m=="{")and(n=="}")):
        return 0
    return 1
a=input()
l=[]
v=0
for i in range(0,len(a)):
    if((a[i]=="(")or(a[i]=="{")or(a[i]=="[")):
        l.append(a[i])
    elif((a[i]==")")or(a[i]=="}")or(a[i]=="]")):
        if(a2(l[len(l)-1],a[i])):
            v=1
            break
        else:
            l.pop()
if(v==1):
    print("fail")
else:
    print("pass")




