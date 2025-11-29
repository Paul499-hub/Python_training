'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

'''
nums=[0,0,1,2,3,3,3,3,4,5,6,6,7,8,8,8,8,8]

def sol(nums):
        
        if not nums:
            return 
        idx_changer=0
        idx_max=0
        max=nums[0]
        while idx_max<len(nums):
            if nums[idx_max]>max: # IF BIGGER NUMBER FOUND, change max
                max=nums[idx_max]
                idx_changer+=1
                nums[idx_changer]=max
            idx_max+=1
        return idx_changer+1
        
k=sol(nums)
print(f'k:{k}, nums:{nums}')

