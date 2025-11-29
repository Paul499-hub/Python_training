s="abcabcbbabcdefghfgadcrteqahfajfabcdefghijkloaoipoasdi"
#s = "abcbefg"
if False:
    substr=''
    dict={}
    i=0
    slowi=0
    max=0
    maxstr=''

    while i < len(s):
        letter=s[i]

        if letter in dict: # SUBSTRING OVER
            if len(substr)>max:
                longest=substr
                max=len(longest)
            dict={}
            substr=''
            slowi+=1
            i=slowi
            continue

        if i==len(s)-1: # LAST INDEX CASE
            if len(substr)>max:
                longest=substr
            dict[letter]=i

        dict[letter]=i
        substr+=letter
        i+=1

# --------------- V2 

s="abcabcbbabcdefghfgadcrteqahfajfabcdefghijkloaoipoasdi"
#s = "abcbefg"
i=0
w_start=0 # w_end=i
dict={}
max=0
saved_sub=''

while i<len(s)-1:
    letter = s[i]
    if letter in dict and dict[letter]>=w_start:
        if i-w_start>max:
            max=i-w_start
            saved_sub=s[w_start:i]
            print(f'longes saved:{saved_sub} length:{i-w_start}')
        w_start=dict[letter]+1
    dict[letter]=i
    i+=1
sub=s[w_start:len(s)]
if len(s)-w_start>max:
    saved_sub=s[w_start:len(s)]


print(f'saved:{saved_sub}')





