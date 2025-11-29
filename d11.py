'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

empty - all opening brackets allowed
( - all opening brackets allowed , + )      ] } not allowed 
'''



def ans():
    s="([])[]{}[]"
    
    opening_dict={'(':')', '[':']','{':'}'}
    expected=[] #<--- iterates from end
    for letter in s:
        current=letter
        print(f'\ncurrent  {current}')
        if current in opening_dict: #<-------------------- IF OPENING BRACKETS
            expected.append( opening_dict[current] )
            print(f'[O] OPENING BRACKET. expected list  {expected}')
        else:
            if len(expected)>0:
                if current==expected[len(expected)-1]: #<----- IF CLOSING BRACKED = LAST ADDED 
                    print(f'[C] Closing order good. expected  {expected[len(expected)-1]} ... Current:  {current}   Removing expected at last index.')
                    expected.pop()
                else:
                    print(f'[X] WRONG ORDER, expected  {expected[len(expected)-1]} but current:  {current}')
                    return False
            else:
                print(f'[X] WRONG ORDER, expected NO CLOSING BRACKET but current:  {current}')
                return False
                
    if len(expected)>0:
        print(f'UNCLOSED BRACKETS LEFT')
        return False
    else:
        print(f'VALID')
        return True



    


        



    

print(ans())
