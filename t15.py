nums = [-1,0,1,2,-1,-4]

#RESULT: [[-1,-1,2],[-1,0,1]] . TRIPLETS MUST ADD TO ZERO. ALL NUMBERS MUST BE DIFFERENT. SAME FREQUENCY TRIPLETS REMOVED(DUPLICATES)
nums=[-1,0,1,2,-1,-4]

# HELPER
def idx(iter,idx):
    return iter[idx] if abs(idx)<len(iter) else None

if False:

    def outside(nums):
            fin=[]
            memory = set()
            nums=sorted(nums)

            # HELPER
            def idx(iter,idx):
                return iter[idx] if abs(idx)<len(iter) else None

            def tree(idx0, idx1, idx2,nums):

                #PRUNING
                if idx0 < idx1 < idx2:
                    pass
                else:
                    return

                n1=idx(nums,idx0)
                n2=idx(nums,idx1)
                n3=idx(nums,idx2)

                fm = frozenset([idx0,idx1,idx2])
                if fm in memory:
                    return
                memory.add(fm)
        
                if n1>0: # IF n0 ABOVE 0 ALL NUMBERS WILL ADD UP TO ABOVE ZERO
                    return 
                        
                try:
                    if n1+n2+n3 == 0 and idx0!=idx1 and idx0!=idx2 and idx1!=idx2:
                        fin.append([n1,n2,n3])
                except:
                    return

                #SPAWN
                # FIND NEXT INDEX THAT ISN'T SAME NUMBER 
                tree(idx0,idx1,idx2+1,nums)
                tree(idx0,idx1+1,idx2,nums)
                tree(idx0+1,idx1,idx2,nums)

            tree(0,1,2,nums)

            clear=set()
            for el in fin:
                clear.add(tuple(sorted(el)))
            
            fin=[]
            for el in clear:
                fin.append(list(el))
            return fin

    print(outside(nums))


nums=sorted(nums)





    









