

def sol():


    n=2

    res=[]
    def dfs(openP, closeP, s):
        
        #BASE CASE, IS PARENTHESIES ARE EQUAL AND NEED TO ADD NO MORE
        if openP == closeP and openP + closeP == n*2:
            res.append(s)
            return
        
        # RECURSIVELY INCREASE OPEN P IF WE CAN
        if openP < n:
            dfs( openP + 1, closeP, s + '(' )
        # RECURSIVELY INCREASE OPEN P IF WE CAN
        if closeP < openP:
            dfs( openP, closeP + 1, s + ')' )

    dfs(0,0,'')

    return res