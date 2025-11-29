'''
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

nums = [4, 4, 4, 4]
target = 8

required={}
for i in range(len(nums)):
    current_num=nums[i]
    required_num=target-current_num

    if current_num in required:
        print(f'{current_num} + {nums[required[current_num]]}={target}')
        print(f'indices:[{i}] + [{required[current_num]}]')
        break

    required[required_num]=i