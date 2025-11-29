s='aabbbccddee'

p='aa?b?c*'

# def tree_iterate(idx):
#     if idx < len(s):
#         print(f'[TREE TRAVERSE]: {s[idx]}')
#         tree_iterate(idx+1)
# tree_iterate(0)


#TWO POINTERS, * checks next symbol in the pattern list and matches everything UNTIL that, or if last mathces everything

def outside():

    p_p=0
    iterate_until=''

    def solve():

        for i in range(len(s)):
            if p_p>=len(p):
                if iterate_until:
                    return False
                break

            s_member= s[i]
            p_member= p[p_p]
            print(f's_member={s_member} p_member={p_member}')

            if iterate_until:
                if iterate_until==s_member:
                    print('[iterate until found]')
                    iterate_until=''
                else:p_p+=1
            
            if s_member==p_member or p_member=='?':
                print(f'--[SINGLE MATCH]--  {s_member} ,  {p_member}')
                p_p+=1
                continue

            if p_member=='*':
                if p_p>=len(p)-1:
                    print(f'--[MULTI MATCH LAST]-- EVERYTHING MATCHES')
                    break
                else:
                    iterate_until=p[p_p+1]
    solve()




    


    


