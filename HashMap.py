'''Problem Statement: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


nums = [2, 7, 11, 15,8,12,4,9,10,16,18,17,3]
target = 20

# INTERTE THROUGHT ALL NUMBERS

#PUT EVERY NUMBER's VALUE as KEY, and INDICE as VALUE inside DICTIONARY

#CALCULATE VALUE NEEDED FOR EACH current number , SEE IF IT IS IN DICTIONARY, IF IT IS, GET THE VALUE's INDICE and current number's indice


seen={} # Number_value(key) :Indice_in_list(value) 
for i in range(len(nums)):
    out=[]
    value_needed = target - nums[i]
    if value_needed in seen:
        out.append(i)
        out.append(seen[value_needed])
        break
    seen[nums[i]] = i 
        

print(out)