'''
Given an integer x, return true if x is a 
palindrome (reads same forward and back '121' )
, and false otherwise.
'''

input=-12356877865321


def is_palindrome(x):
    s=str(x)
    mid=len(s)//2

    l=s[:mid]
    print(f'l:{l}')
    if len(s)%2==0:
        r=s[mid:]
    else:
        r=s[mid+1:]
    r=r[::-1]
    print(f'r:{r}')
    if r==l:
        return True
    else:
        return False
    
print(is_palindrome(input))

    
    