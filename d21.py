

def sol1(): # SLIDING WINDOW - FIND LONGEST SUBSTRING
    s='abcasd'


    left = max_length = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1

        char_set.add(s[right])
        max_length = max( max_length, right-left+1 )

    return max_length


def sol2():
    s='abcde'

    left = max_length = 0
    count={}

    for right, char in enumerate(s):
        count[char] = 1 + count.get(char,0) #<--- COUNTS HOW MANY KEYS WITHOUT KEY ERROR

        while count[char] > 1:
            count[s[left]] -=1 
            left+= 1

        max_length = max(max_length, right - left + 1)

    return max_length

        
def sol3(): # SLIDING WINDOW - FIND LONGEST SUBSTRING
    s='absvasb'

    left = max_length = 0
    last_seen = {}

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1 #<----- MOVE LEFT POINTER +1 PAST ALREADY ENCOUNTERED 
        
        max_length = max(max_length, right-left + 1)
        last_seen[char]= right
    
    return max_length


# c='hello'

# rev=''
# for i in range(len(c)-1,-1,-1):
#     rev+= c[i]

# OR 

#s[::-1]


example=[0,1,2,3,4,5,6,7,8]

# res=[]
# for i in range(len(example)):
#     if example[i]%2==0:
#         res.append(example[i]) 
# print(res)

#OR

#[num for num in example if num % 2 ==0]


# CHECK IF ADJACENT NUMBER ORDER SHOULD BE FLIPPED 

ex = [0,1,6,7,2,1,3,5,4,6,8,5]

def bubble(ex):

    # DEFINE 2 VARIABLES idx_len and sordet 
    idx_len= len(ex)-1
    sorted=False

    while not sorted: # LOOP while not sorted 
        sorted = True # assume will be sorted
        for i in range(idx_len): # Loop until idx_len
            if ex[i]>ex[i+1]: # 
                sorted=False
                ex[i], ex[i+1] = ex[i+1], ex[i]
        idx_len=idx_len-1 #<---------- SHOULD I ADD THIS HERE? 
    return ex

print(bubble(ex))




class Car:
    def __init__(self, brand, model):
        self.brand = brand

    def display_info(self):
        print(self.brand)



class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # Inherit from Car
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Example Usage
my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
my_electric_car.display_info()



