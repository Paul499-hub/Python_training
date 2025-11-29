



def outside():
        candidates = [2,3,6,7]
        target = 7
        maxIdx=len(candidates)-1
        final_res=set()
        #i=0

        def deep_search(idx, res, sum):
            #nonlocal i
            #i=i+1
            #print(f'\n------------[ENTER |{i}]--- entered loop with: idx={idx}, res={res}, sum={sum} , current_num={candidates[idx]}')

            # CALCULATE SUM <--- LATER THIS DECIDES IF FUNCTION SHOULD SPAWN CHILDREN OR NOT
            asum=sum+candidates[idx]
            #print(f'asum={asum}')

            #RECURSIVE / BASE
            if asum<target: #<--- SPAWN 
                res.append(candidates[idx])
                for idx in range(idx,len(candidates)): #<--- DO NOT SEARCH TO THE LEFT OF IDX, ALREADY TRAVERSED...
                    deep_search(idx,res,asum)
                if res:res.pop()
            elif asum>target:
                #print(f'--[BASE]-- DONT SPAWN CHILDREN, SUM IS ALREADY HIGHER THAN TARGET!')
                pass
            elif asum==target:
                res.append(candidates[idx])
                key = tuple(sorted(res))
                final_res.add(key)
                res.pop()
                #print(f'$$$$ VALID RESULT RETURNED... Appending to fin... final_res={final_res}') 
            
        for idx in range(len(candidates)):
            deep_search(idx,[],0) #<--- DEEP SEARCHES ROOT NUMBER AND ALL IT's COMBINATIONS.

        #print(f'final res:{final_res}')
        return list( [list(t) for t in final_res] )

print(outside())


    
    


    



    

            

