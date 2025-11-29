'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string 
is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range.
Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
'''

s = "  +  413"


def myAtoi(s):
        IsPositive=True
        out = 0
        temp=''
        FNZ=False
        SignDetected=False
        for i in range(len(s)):
            # print(s[i])
            current=s[i]

            if current==' ': # SPACE
                # print(f'space detected')
                if len(temp)>0 or FNZ==True or SignDetected==True:
                    break
                continue
            elif current =='+' or current=='-':# + OR - , STORE IN IsPositive
                if len(temp)>0 or FNZ==True or SignDetected==True:
                    # print(f'sign encounter AFTER a number')
                    break
                if current=='+':
                    # print(f'+ detected')
                    IsPositive=True
                    SignDetected=True
                    continue
                elif current=='-':
                    # print(f'- detected')
                    IsPositive=False
                    SignDetected=True
                    continue
            elif current.isdigit():
                
                if len(temp)==0 and int(current)==0:
                    # print(f'first number zero')
                    FNZ=True
                    continue
                else:
                    temp+=current
            else:
                # print(f'non-digit detected')
                break
            # print(f'temp after this iteration:{temp}')

        if not temp.isdigit():
            # print(f'returning 0')
            return 0
        if int(temp)>= 2**31:
            if IsPositive==True:
                temp=2**31 - 1
            else:
               temp=2**31 

        out = int(temp) * -1 if IsPositive==False else int(temp)
        
        # print(f'temp:{temp}, ispositive:{IsPositive}, out:{out}')
        return out

            




print(myAtoi(s))