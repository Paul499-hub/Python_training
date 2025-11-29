'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed), in ascending order.

You may assume that each input would have exactly one solution and you may not use the same element twice.
'''

numbers = [2, 7, 11, 15]
target = 9
left=0
right=len(numbers)-1

while left<right:
    lr_sum=numbers[left]+numbers[right]

    if lr_sum==target:
        print(f'Answer found: {numbers[left]}+{numbers[right]}={target}')
        print(f'indexes:[{left+1}] + [{right+1}]')
        break

    if lr_sum>target:
        right-=1
        continue
    if lr_sum<target:
        left+=1
        continue
    
    