'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

strs = ['flog','flog','flot']

def Sol():
    prefix=''
    if len(strs)<1:
        return prefix
    
    for i in range(len(strs[0])):
        old_char=strs[0][i]
        for word in strs:
            if i<len(word):
                if old_char!=word[i]:
                    prefix=word[:i]
                    return prefix   
            else:
                prefix = word[:i]
                return prefix
        prefix=strs[0][:i+1]
    return prefix

print(Sol())
