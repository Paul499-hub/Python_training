n=4



def cs(n,data='', FIRST_DONE=False):
    #print(f'data on enter:{data}')
    if n<1:
        return data

    # TRANSFORM THE STRING
    temp=[]
    count=1
    last=''
    for i in range(0,len(data)):
        current=data[i]
        #print(f'c:{current} previous:{last}')
        if current==last:
            count+=1
            #print(f'currnent and next is same. add to count +1')
            if i==len(data)-1:
                temp.append(str(count))
                temp.append(str(current))
                #print(f'exit loop temp:{temp}')
        elif last=='':
            last=current
            if i==len(data)-1:
                temp.append(str(count))
                temp.append(str(current))
                #print(f'exit loop temp:{temp}')
        elif current!=last:
            temp.append(str(count))
            temp.append(str(last))
            count=1
            last=current
            #print(f'current and next NOT same. reset count. new temp:{temp}')
            if i==len(data)-1:
                temp.append(str(count))
                temp.append(str(current))
                #print(f'exit loop temp:{temp}')

    data = ''.join(temp) if len(temp)>0 else data
    n-=1
   
    if FIRST_DONE==False: # GENERATE 1
        #print(f'FIRST_DONE')
        FIRST_DONE=True
        data='1'
    return cs(n,data,FIRST_DONE)


print(cs(6))

