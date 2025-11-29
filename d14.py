'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''


def sol():
    haystack = "leetcode"
    needle = "leeto"
        
    search_index= len(needle)-1
    for _ in range(1+len(haystack)-len(needle) ):
        if haystack[search_index+1 - len(needle): search_index+1 ] == needle:
            return search_index+1 - len(needle)
        search_index+=1
    return -1

print(sol())
      