digits = [1,7,9]


def sol():
    
    carry=False
    for i in range(len(digits)):
        
        if digits[ len(digits)-1 -i ]>=9: #<----- CURRENT NUM 9 OR MORE
            digits[ len(digits)-1 -i ]=0  #<----- SET CURRENT TO 0
            if (len(digits)-1 -i -1) < 0: #<----- PREVIOUS INDEX DOES NOT EXIST, CREATE 1
                digits.insert(0,1)
                print('IV')
                return digits
            else: #<----- PREVIOUS INDEX DOES EXIST, INCREMENT IT BY ONE
                digits[ len(digits)-1 -i -1 ] = digits[ len(digits)-1 -i -1]+1
                if digits[ len(digits)-1 -i -1 ]<10:
                    return digits
                print('I')
                
        elif carry==False and digits[ len(digits)-1 -i ]<10: #<----- CURRENT LESS THAN 9
            digits[ len(digits)-1 -i ]=digits[ len(digits)-1 -i ]+1
            print('II')
            return digits
    return digits
        

def plusOne():

    for i in range(len(digits)-1,-1,-1):
        if digits[i] + 1 < 10:
            digits[i] += 1
            return digits 
        digits[i]=0
        if i==0:
            return [1] + digits

print(plusOne())
