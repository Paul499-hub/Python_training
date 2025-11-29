
list0 = [1,3,4,5,6,5,7,6,6,11,16,20]

target_sum = 20

# SUM ALL POSSIBLE NUMBERS .
#  if target sum == BASE CASE . 

# FILTER DUPLICATE VALUES 
'''for n in range(0,len(list0)):
    print(f' n ==== {list0[n]}')
    for n2 in range(1+n, len(list0)):
        print(f'n2 = {list0[n2]}')
        if (n+list0[n2])==target_sum:
            print(f"YES : {n}+{list0[n2]} = {target_sum}")
            exit()'''


def rec( list0, target_sum, catche={} ):
    # MEMOIZATION
    if f"rec({target_sum})" in catche:
        print("skip")
        return catche[f"rec({target_sum})"]

    # BASE CASES
    if target_sum ==0:
        return True
    if target_sum <0: 
        return False

    # RECURSION 
    for i in list0:
        rem = target_sum-i
        if(rec(list0, rem, catche=catche )):
            catche[f"rec({rem})"]= True
            return True

    return False
    
        

#print(rec( list0, target_sum))
print(rec( [2,4], 7))
print(rec( [2,3,5], 8))
print(rec( [2,4], 777))