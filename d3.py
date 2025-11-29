strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def is_anagram(w1,w2):
    if len(w1)!=len(w2):
        return False
    w1dict={}
    for i in range(len(w1)):
        w1dict[w1[i]]=i

    for i in range(len(w2)):
        if w2[i] not in w1dict:
            return False 
    return True

out=[]
added=False
for i in range(len(strs)):
    if i==0:
        out.append([strs[i]])
    if i>0:
        for category in range(len(out)):
            added=False
            if is_anagram(out[category][0], strs[i]):
                out[category].append(strs[i])
                added=True
                break
        if added==False:
            out.append([strs[i]])
            
print(out)

       
    