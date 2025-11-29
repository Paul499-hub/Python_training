s = "abc ac"

def sol():
    c=''
    counter=0
    word_started=False

    for i in range(len(s)):
        c = s[len(s)-1-i]

        if (c==' ') and word_started==True:
            return counter

        if c==' ':
            word_started=False
            counter=0
        else:
            word_started=True
            counter+=1
            if i==len(s)-1:
                return counter
    return counter

        

        

print(sol())