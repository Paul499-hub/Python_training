# 1 2 3 4 5 6  7  8  9  10 = n
# 1 1 2 3 5 8 13 21 34

n_times_function_ran = 0

def fib_slow(n): #TIME COMPLEXITY = O(2**n)  SPACE COMPLEXITY O(2) 
    if n <3:
        return 1
    global n_times_function_ran
    n_times_function_ran = n_times_function_ran + 1 
    return fib_slow(n-1) + fib_slow(n-2)


def fib_faster(n , d1={"fib(1)":1, "fib(2)":1}):
    if f"fib({n})" in d1:
        return d1[ f"fib({n})" ]
    else:
        d1[f"fib({n})"] = fib_faster(n-1)+ fib_faster(n-2)
        return d1[f"fib({n})"]


def fib_fast(n , already_know={"fib(1)":1,"fib(2)":1} ): #TIME COMPLEXITY = O()  SPACE COMPLEXITY O() 
    if n <3:
        return 1
    else:
        if len(already_know)>=(n-1):
            # WE KNOW THE VALUE AND DONT NEED TO COMPUTE AGAIN
            left = already_know[  f"fib({n-1})"]
            print(f' we have already computed fib({n-1}) it is : { left } ')
        else:
            print(f' we dont know value of fib({n-1})')
            left = fib_fast(n-1)

        if len(already_know)>=(n-2):
            right = already_know[ f"fib({n-2})" ]
            print(f' we have already computed fib({n-2}) it is : {right} ')
        else:
            print(f' we dont know value of fib({n-2})')
            right = fib_fast(n-2)
        already_know[ f'fib({n})' ] = right + left
        return right + left



def fib(n): # < TIME COMPLEXITY = O(n)  SPACE COMPLEXITY O(2) 
    out = 1
    prev1 = 1
    prev2 = 1
    prev3 = 1
    print(f'BEGIN ------------------- ')
    for i in range(1,n+1):
        global n_times_function_ran
        n_times_function_ran = n_times_function_ran + 1 
        print(f'i = {i}')
        if i>2:
            out = prev1 + prev2 # 2(p1) + 3(p2) = 5(out)   
            print(f'out: {out}         p1: {prev1}            p2: {prev2}            p3: {prev3}')
            # STORE VALUES 
            if i>3:
                prev3= prev1
            prev1 = prev2 # 2(p1) --> 3(p1) 
            prev2 = out # 3(p2) --> 5(p2) 
            
            

        else:
            out=1
    return out



print( " fib answer: " , fib(9) )

#print(f' already know list: {already_know}')