'''PROGRAMA SKAITO DUOMENIS IS DATA.txt failo
JAME COPY/PASTE BUDU IKLIJUOTI VISI DUOMENYS IS DUOTU VARIJANTU DOKUMENTE

KAIP ATSKYRIMO MECHANIZMA NAUDOJU '~' SIMBOLY
pvz:

4 12 16 14 12 16	K – žaidimo kategorija, surinkti taškai
1 9 6 8 7 12	K – žaidimo kategorija, surinkti taškai
9 11 12 11 15 16	K – žaidimo kategorija, surinkti taškai
~ <---------------------------------------------------------------REIKIA!
11	M – dalyvių skaičius
3 11 25 6 14 3	
5 20 20 15 4 9	K – žaidimo kategorija, surinkti taškai
8 10 16 1 4 15	K – žaidimo kategorija, surinkti taškai

'''

def parse_txt_into_3Dlist():

    char_memory=''
    row_nums = []
    list2D = []
    list3D=[]
    
    with open('DATA.txt','r',encoding='utf-8') as file:
        for row in file:
            for char in row:
                if str.isdigit(char):
                    char_memory += char
                else:
                    if len(char_memory)>0: # IF CURRENT CHAR ISNT NUMBER AND PARSED NUMBER EXISTS IN MEMORY - ADD THAT NUMBER INTO THE LIST
                        row_nums.append( int(char_memory))
                        char_memory=''

                    if char=='~':  # IF SEPERATOR FOUND, PUT ALL COLECTED DATA INSIDE 3D LIST
                        list3D.append(list2D)
                        list2D=[]

            if len(row_nums)>0: # IF VALID NUMBERS FOUND IN THIS ROW, PUSH THEM INTO 2D LIST
                list2D.append(row_nums)
            row_nums=[]
            
    if len(list2D)>0: #IF THERE IS NO '~' AT THE END OF FILE, APPEND ANYWAY
        list3D.append(list2D)
    return list3D

def find_max_min(result_list):
    print(f'\nEXTRA TASK : find max min of result list:{result_list}')
    max=result_list[0]
    final_max_index=0
    min=result_list[0]
    final_min_index=0
    for i in range(len(result_list)):
        if result_list[i]>max:
            max=result_list[i]
            final_max_index=i
        if result_list[i]<min:
            min=result_list[i]
            final_min_index=i
    
    print(f'Game {final_max_index+1} had maximum score ({max}) in this variant.')
    print(f'Game {final_min_index+1} had minimum score ({min}) in this variant.')


result_list_memory=[0] * 10
valid_game_categories=list(range(1,11))
valid_num_members=list(range(5,21))
result_list=list([0]*10)
all_data = parse_txt_into_3Dlist()

for variant in all_data:
    print(f'variant:{variant}')

    ''' VARIANT NOW LOOKS LIKE THIS:
    variant:[[10],              <-- i=0
    [1, 15, 20, 22, 5, 9],      <-- i=1 , k=range(0,7)
    [5, 0, 6, 12, 14, 5], 
    [2, 12, 12, 5, 14, 13], 
    [7, 1, 1, 9, 6, 7], 
    [8, 11, 17, 15, 13, 9], 
    [10, 12, 20, 13, 14, 16], 
    [2, 11, 12, 11, 14, 9], 
    [4, 12, 16, 14, 12, 16], 
    [1, 9, 6, 8, 7, 12], 
    [9, 11, 12, 11, 15, 16]]     <-- i=10
    '''

    for i in range(len(variant)):
        if i==0:
            if variant[i][0] < 5 or variant[i][0] > 20:
                print(f'NOT ENOUGH PLAYERS!')
                break
        else:
            for k in range(len(variant[i])):
                if variant[i][0] >=1 and variant[i][0]<=10 and k>0:     # BECAUSE FIRST NUMBER OF EACH ROW IS GAME CATEGORY
                        result_list[ variant[i][0] - 1 ] += variant[i][k]
    for i in valid_game_categories:
        print(f'Game category: {i}       Total score:{result_list[i-1]}')
    

    for i in range(len(result_list)):
        result_list_memory[i] = result_list_memory[i] + result_list[i]   # ADD ALL SCORES OF ALL VARIANTS

    find_max_min(result_list)
    print('\n\n')
    result_list=list([0]*10)

print(f'RESULT LIST of TOTAL ADDED SCORES FOR EACH GAME: {result_list_memory}')
find_max_min(result_list_memory)


        
                





