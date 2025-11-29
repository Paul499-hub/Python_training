lone = [0,5,300,40,55,159,44,133,12,16,15,111,1888,20,15]



l=[2,3,7]
r=[3,4,8,9]
#result= [2,3,3,4,7,8,9]

def merge(l,r):
    
    out=[]
    i=0
    j=0
    for _ in range(len(l)+len(r)):

        if i>=len(l):
            out.append(r[j])
            j+=1
            continue

        if j>=len(r):
            out.append(l[i])
            i+=1
            continue

        if l[i] == r[j]:
            out.append(l[i])
            i+=1
            continue
        if l[i]<r[j]:
            out.append(l[i])
            i+=1
            continue
        if r[j]<l[i]:
            out.append(r[j])
            j+=1

    return out

def merge_sort(glist):
    #BASE CASE
    if len(glist)<2:
        return glist      #<----------------- RETURNS THIS 
    
    #SPLIT
    mid=len(glist)//2
    r=glist[mid:]
    l=glist[:mid]

    #RECURSION
    r=merge_sort(r)        #<----------------- HERE
    l=merge_sort(l)

    #FINAL RETURN
    return merge(l,r)



print(merge_sort(lone))