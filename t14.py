def idx(iter,idx):
    return iter[idx] if abs(idx)<len(iter) else None


nums=[1,3,7,2,2,5,4,11,13,4,2,6,7,3,15,2,5]

def merge_sort(nums):

    # BASE CASE
    if len(nums)<2:
        return nums

    # DIVIDE
    mid=len(nums)//2
    l=nums[:mid]
    r=nums[mid:]

    #RECURSE
    l=merge_sort(l)
    r=merge_sort(r)  

    #COMBINE
    return recombine(l,r)

def recombine(a,b):
    res=[]
    p_a=0
    p_b=0
    for _ in range(len(a)+len(b)):
        n_a=idx(a,p_a)
        n_b=idx(b,p_b)

        try:
            if n_a<n_b:
                res.append(n_a) 
                p_a+=1
            else:
                res.append(n_b) 
                p_b+=1
        except:
            if not n_a:
                res.append(n_b)
                p_b+=1
            elif not n_b:
                res.append(n_a)
                p_a+=1


    return res

print(merge_sort(nums))
    



