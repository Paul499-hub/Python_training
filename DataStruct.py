#LIST 
if False:
    my_list = [1, 2, 3, "hello", True]
    my_list.extend([5,5,5])
    my_list.insert(0,'wot')
    print(my_list)

#TUPLE
if False:
    t=(1,5,'huh',1,1)
    ans=t.count(1) #<--- COUNTS HOW MANY INSTANCES OF GIVEN OBJECT IN TUPLE
    ans=t.index('huh') #<------ RETURN THE FIRST INDEX OF GIVEN VALUE
    print(ans)

#DICT
if True:
    d={'key1':0,'key2':12}
    ans=d.keys()
    d.update([('key1',5), ('key5',6)]) #<--- merges/updates OVERLAPPING VALUES with DICT
    print(d.pop('key9','Key not found')) #<--------- remove from DICT, IF VALUE NOT FOUND RETURN 'key not found'
    print(f'pop:{d.popitem()}')# <------------------- DELETES LAST INSERTED ITEM IN DICT
    print(f'first dict key:{next(iter(d))}')
    d['key3']= 13
    d['key4'] = 15
    print(d)

    #-------------------------------- ITERATING DICT's
    print(f'ordinary dict iteration')
    for key,value in d.items():
        print(key)
        print(value)

    print(f'dict iteration using next:')
    dict_iterator= iter(d)
    try:
        while True:
            next_key=next(dict_iterator)
            print(f'key:{next_key} value:{d[next_key]}')
    except StopIteration: #<------------------------------ EXCEPTION RAISED AFTER ITERATOR HAS NO MORE ITEMS TO RETURN
        print('Iteration over')
    


#SET 
if False:
    s=set()
    s={0,1}
    s.add('huh')
    s.remove('huh')
    out = s.union({1,2}) #<----- MERGES BOTH ITERABLES
    out = s.intersection({1,2}) #<----- ITEMS IN BOTH SETS
    out = s.difference({1,2})#<-------- ELEMENTS IN FIRST SET, BUT NOT IN SECOND
    s.discard(1)#<-------------------- SAFE DELETE, DOESNT RAISE KEY ERROR
    print(s)


#STRING
if False:
    txt='baBcbeaeba'
    txt=txt.upper()
    txt=txt.lower()
    txt=txt.strip('ba') #<-------- REMOVES THESE CHARS FROM START AND END UNTIL one of the char's not found
    txt=txt.replace('a','|')
    out=txt.find('|')
    words=['dog','cat','treee']
    joined='%'.join(words)
    print(joined)


#ARRAY - LIST BUT CAN STORE ONLY ON TYPE OF ELEMENT. MORE MEMORRY EFFICIENT

