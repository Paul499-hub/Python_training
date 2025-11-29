s = "loveleetcode"

r_table={}
for i in range(len(s)):
    if s[i] in r_table:
        r_table[s[i]]+=1
    else:
        r_table[s[i]]=0
print(f'r_table:{r_table}')

found=False
for i in range(len(s)):
    if r_table[s[i]]==0:
        print(f'First non repeating:{s[i]} index:{i}')
        found=True
        break

if found==False:
    print(f'Every character repeats at least once. index: -1')



   
    
    




