lone = [0,5,300,40,55,159,44,133,12,16,15,111,1888,20,15]

def merge_sort(glist):
    #BASE CASE
    if len(glist)<2:
        return glist
    #MAIN FUNCTION
    left = glist[:len(glist)//2]
    right = glist[len(glist)//2:]  
    print(f'l:{left} r:{right}')
    #RECURSION
    return merge( merge_sort(left), merge_sort(right) )

def merge(l,r):
    out=[]
    i=0
    j=0
    for _ in range(len(l)+len(r)):
        if i>=len(l): # ERROR CASE
            out.append(r[j])
            j+=1
            continue 

        if j>=len(r):  # ERROR CASE
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
            continue

        if r[j]==l[i]:
            out.append(r[j])
            j+=1
            continue

    return out

print(merge_sort(lone))

