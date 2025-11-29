s1 = "bcc" 
s2 = "bbca" 
s3 = "bbcbcac"
#Output: true

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

s1="aabcc"

s2="dbbca"

s3="aadbbcbcac"


# SPAWN CHILDREN IF char exists in s1 or s2
# sum it into single string

def outside():
        
        if len(s1)+len(s2)!=len(s3):
            return False
        
        FINAL=[False]
        memory=set()
        def tree(idxs3,idxs2,idxs1,prio=''):
            
            if (idxs3,idxs2,idxs1) in memory: # <--- ALREADY COMPUTED THIS ENTRY
                return 
            memory.add((idxs3,idxs2,idxs1))

            #print(f'\n----[ENTER]--- {idxs3} | {idxs2} | {idxs1} | {temp} | prio: {prio} |')

            if FINAL[0]==True: # EXIT TREE AFTER FINDING RESULT
                return

            if prio:
                c=s3[idxs3]

            if prio=='s2':
                if  idxs2<len(s2):
                    if s2[idxs2]==c:
                        #temp=temp[:]+s2[idxs2] #<--- TEMPORARY STRING WHERE WE SUM RESULT
                        #print(f'---[FOUND]--- {s3[idxs3]} exisits in s2... Updated temp:{temp}')
                        pass
                    else:
                        #print(f'-[X]- Priority is s2, but s2 doesnt have current letter. return')
                        return
                else:
                    #print(f'-[X]- s2 cannot be iterated anymore... idxs2 out of range: {idxs2}')
                    return

            if prio=='s1':
                if  idxs1<len(s1):
                    if s1[idxs1]==c:
                        #temp=temp[:]+s1[idxs1] #<--- TEMPORARY STRING WHERE WE SUM RESULT
                        #print(f'---[FOUND]--- {s3[idxs3]} exisits in s1... Updated temp:{temp}')
                        pass
                    else:
                        #print(f'-[X]- Priority is s1, but s1 doesnt have current letter. return')
                        return
                else:
                    #print(f'-[X]- s1 cannot be iterated anymore... idxs1 out of range: {idxs1}')
                    return

            if idxs3==len(s3)-1:
                #print(f'-----------[CORRECT]-------- TEMP IS s3: {temp}')
                FINAL[0]=True
                return True   
     
            #SPAWN LEAF NODES
            tree(idxs3+1,idxs2=idxs2+1,idxs1=idxs1, prio='s2')
            tree(idxs3+1,idxs2=idxs2,idxs1=idxs1+1, prio='s1')

        tree(-1,-1,-1)
        return FINAL[0]


print(outside())







