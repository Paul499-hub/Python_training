'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''




# FIND HALF NUMBER 

#CHECK IF TARGET HIGHER OR LOWER THAN HALF NUMBER

# IF HIGHER, TAKE HIGHER HALF OF LIST AND FIND HALF NUMBER OF IT

# IF LOWER, TAKE LOWER HALF OF LIST AND FIND HALF NUMBER OF IT 


# def sol_old(glist, saved=None):
#     #BASE CASE
#     if len(glist)<2:
#         print(f'BASE CASE returning glist:{glist}')
#         return glist
        
#     # SPLIT l , r 
#     mid_idx = len(glist)//2
#     mid_num = glist[mid_idx]

#     if saved==None:
#         saved={}
#         saved['idx_list']=range(len(glist))

#     print(f'mid_idx:{mid_idx}')
#     if target>mid_num:
#         half=glist[mid_idx:]
#         saved['idx_list']=saved['idx_list'][mid_idx:]
#         print(f'target higher than mid... target: {target} mid:{mid_num} ... Split list: {half} , SAVED:{saved["idx_list"]}')
#     elif target==mid_num:
#         half=[glist[mid_idx]]
#         saved['idx_list']=saved['idx_list'][mid_idx]
#         print(f'target EQUAL mid... target: {target} mid:{mid_num} ... Split list: {half}, SAVED:{saved["idx_list"]}')
#     else:
#         half=glist[:mid_idx]
#         saved['idx_list']=saved['idx_list'][:mid_idx]
#         print(f'target lower than mid... target: {target} mid:{mid_num} ... Split list: {half}, SAVED:{saved["idx_list"]}')

#     half=sol(half, saved)
#     return half


# nums = list(range(1, 10000))
# target=5000

# def searchInsert(nums, saved=None):

#     #EDGE CASE
#     if not nums:
#         return []

#     if target<nums[0]:
#         return 0
#     elif target>nums[len(nums)-1]:
#         return len(nums)

#     if saved==None:
#         saved={}
#         saved['idx']=range(len(nums))

#     #BASE CASE
#     if len(nums)==2:
#         if target<=nums[0]:
#             return saved['idx'][0]
#         else:
#             return saved['idx'][1]
    
#     m=len(nums)//2

#     if nums[m]<target:
#         nums=nums[m:]
#         saved['idx']=saved['idx'][m:]
#         print(f'<  nums: {nums} saved: {saved}')
#     elif nums[m]>target:
#         nums=nums[:m+1]
#         saved['idx']=saved['idx'][:m+1]
#         print(f'>  nums: {nums} saved: {saved}')
#     elif nums[m]==target:
#         return saved['idx'][m]
    
#     return searchInsert(nums,saved)
        
# print(searchInsert(nums))


nums= [0,1,2,4,5,6]
target=3

def sol():
    pass

    l=0
    r=len(nums)-1
    
    while l<=r:
        middle=(l+r)//2

        if nums[middle]>target:
            r=middle-1
        elif nums[middle]<target:
            l=middle+1
        elif nums[middle]==target:
            return middle
    return l
        
print(sol())






        