
grid=[]

def make_grid(n, m):
    global grid
    for grid_row in range(0,n):
        grid.append( ['*']*m )

def print_grid():
    global grid
    #grid[8][5] = 'x' # LAST INDEX 
    for row in grid:
        print(row)

#2,3 -> 1,2 =2
#make_grid(3,3) # possible moves down 8, possible moves right 5 . 40
#print_grid()

def cal_p(n,m, catche={}):

    if f'p({n},{m})' in catche:
        print(f'skip calculation p({n},{m})')
        return catche[f'p({n},{m})']

    if f'p({m},{n})' in catche: # CHECK IF FLIPPED  
        print(f'skip calculation p({n},{m})')
        return catche[f'p({m},{n})'] 

    if n==0:
        catche[f'p({n},{m})']=0
        return catche[f'p({n},{m})']
    if m==0:
        catche[f'p({n},{m})']=0
        return catche[f'p({n},{m})']
    if n==1 and m==1:
        catche[f'p({n},{m})']=1
        return catche[f'p({n},{m})']

    catche[f'p({n},{m})']=cal_p(n-1,m,catche=catche)+ cal_p(n,m-1,catche=catche)
    return catche[f'p({n},{m})']

print(cal_p(18,18))




