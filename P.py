nums=[1,5,9,7,6,1,2,5,6,4,3,2,1,5,7,8,9,11,15,16,17,19,20,20,22,2,3]

def m_sort(glist):

    #BASE CASE
    if len(glist)<2:
        return glist

    # SPLIT IN HALF LOGIC
    mid=len(glist)//2
    l=glist[:mid]
    r=glist[mid:]

    # RCURRENT CALLS 
    l=m_sort(l)
    r=m_sort(r)

    #BASE CASE 2- CONQUER
    return merge(l,r)

def merge(l,r):
    i=0 # FOR ITERATING FIRST LIST - until len(l)-1
    k=0 # FOR ITERATING FIRST LIST - until len(l)-1
    out=[]
    for _ in range(len(l)+len(r)):
        if i<len(l) and k<len(r):
            if l[i]<r[k]:
                out.append(l[i])
                i+=1
            else:
                out.append(r[k])
                k+=1
        else:
            if i>=len(l):
                out.extend(r[k:])
                return out
            elif k>=len(r):
                out.extend(l[i:])
                return out
    return out
            
print(m_sort(nums))
        

        