'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

s = "egg"
t = "ggo"

def is_anagram(s,t):
    if sorted(s)==sorted(t):
        return True
    return False

o=is_anagram(s,t)
print(o)