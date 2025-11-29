

candidates = [10,1,2,7,6,1,5]
target = 8



def outside():
        final_result=set()
        memory=set()

        def deep_search(idx,res,sum):
            #print(f'--[ON ENTER]-- idx={idx}, res={res}, sum={sum} ----- CURRENT NUMBER : {candidates[idx]}')

            #CALCULATE
            sum=sum+candidates[idx]
            #print(f'sum={sum}')

            #SPAWN
            if sum < target and (idx+1)<len(candidates):
                res = res[:] + [candidates[idx]]
                tsr=tuple(sorted(res))
                if tsr not in memory:
                    #print(f' idx+1 ({idx+1}) IS LESS THAN len(candidates) ({len(candidates)}), SPAWN')
                    memory.add(tsr)
                    for i in range(idx+1,len(candidates)):
                        deep_search(i,res,sum)
            elif sum == target:
                res = res[:] + [candidates[idx]]
                tsr=tuple(sorted(res))
                memory.add(tsr)
                key=tuple( sorted(res))
                final_result.add(key)
                #print(f'******* ANSWER FOUND ***** : {final_result}')
                return res
            elif sum > target:
                #print(f'XXXXX SUM IS GREATER THAN TARGET, DON"T SPAWN sum={sum}, target={target}')
                pass 
            else:pass
            
        for i in range(len(candidates)):
            deep_search(i,[],0)

        final_result= [ list(t) for t in final_result]
        return final_result

print(outside())

