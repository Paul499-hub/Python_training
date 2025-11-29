'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

s = "egg"
t = "ggo"


def ans(s,t):

    if len(s)!=len(t) or len(set(s))!=len(set(t)):
        return False
    else:
        length_before=len(set(s))
        length_joined=len(set(s).union(set(t)))
        if length_joined==length_before:
            return True
        else:
            return False
   
print(ans(s,t))