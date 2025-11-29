strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

dict={}
for i in range(len(strs)):
    current_word=strs[i]
    sorted_word=''.join(sorted(current_word))
    if sorted_word in dict:
        dict[sorted_word].append(current_word)
    else:
        dict[sorted_word]=[current_word]
print(dict)
        
    
