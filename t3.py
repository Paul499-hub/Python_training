'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

# EVERY NUMBER MUST HAVE DIFERENT VALUE

# IF SAME INDEXES USED DISCARD 

# ADDS UP TO ZERO\

nums = [-1,0,1,2,-1,-4]


def merge_sort(glist):
    
    # BASE CASE
    if len(glist)<2:
        return glist
    
    # SPLIT TO L R
    mid= len(glist)//2
    l=glist[:mid]
    r=glist[mid:]

    #RECURSIVE
    l=merge_sort(l)
    r=merge_sort(r)

    return merge(l,r)

def merge(l,r):
    
    l_p=0
    r_p=0
    out=[]
    for _ in range(len(l) + len(r)):
        
        if l_p>=len(l):
            out.extend(r[r_p:])
            return out

        if r_p>=len(r):
            out.extend(l[l_p:])
            return out

        if l[l_p]<r[r_p]:
            out.append(l[l_p])
            l_p+=1
        elif l[l_p]>r[r_p]:
            out.append(r[r_p])
            r_p+=1
        elif l[l_p]==r[r_p]:
            out.append(l[l_p])
            l_p+=1
    return out


s_nums=merge_sort(nums)

def threeSum(nums):
    for i in range(len(nums)):
        pass


threeSum(s_nums)