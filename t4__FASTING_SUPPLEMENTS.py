MVA={} #<-- in mg


Amino_acid_sup_one={'cinkas':10,
'glicinas':226, 'prolinas':123,
'glutamo rugstis':105, 'hidroksiprolinas':92,
'alaninas':88, 'argininas':88,
'asparto rugstis':54, 'lizinas':46,
'serinas':45, 'fenilalaninas':30,
'leucinas':27, 'treoninas':20,
'valinas':17,'izoleucinas':14,
'histidinas':22, 'triptofanas':8,
'metioninas':6, 'tirozinas':5,
'citrulinas':5}

Multi_vitamin_sup_one={'vitaminas a':0.8,
'vitaminas d3':0.005, 'vitaminas e':10,
'vitaminas c':30, 'vitaminas b1':1.4,
'vitaminas b2':1.6, 'niacinas':17.8,
'pantoteno rugstis':5.51, 'vitaminas b6':2,
'vitaminas b12':0.001, 'folio rugstis':0.2,
'biotinas':0.025, 'gelezis':14,
'cinkas':2.5, 'jodas':0.15,
'manganas':0.5, 'cholinas':2,
'rutinas':10 }

Potassium_supplement_one={
'kalio citratas':400}

Multi_vitamin_sup_two= {'kalcis':400,
'magnis':155, 'cinkas':8.5,
'vitaminas d3':0.002
}


def insert_to_MVA(MVA, supplement):
    pass
    # ITERATE THROUGH SUPPLEMENT KEYS
    for key,val in supplement.items():
        #print(f'key:{key}  value:{val}')

        if key in MVA:
            print(f'overlap: {key}')
            MVA[key]+=supplement[key]
        else:
            MVA[key]=supplement[key]


def check_limit(MVA):
    print(f'----------- UPPER LIMIT CHECK -------------- O.O  ')
    if MVA['cinkas']>40:
        print(f'TOO MUCH (cinkas): Nausea, Stomach cramps, Headaches,Loss of appetite, Copper deficiency (too much zinc can interfere with copper absorption)')
    else:
        print(f'cinkas below upper limit (40mg): {MVA["cinkas"]}')

    if MVA['vitaminas d3']>0.1:
        print('''Taking too much vitamin D over time can lead to vitamin D toxicity (also known as hypervitaminosis D). This can result in:
        Hypercalcemia (excessive calcium levels in the blood)
        Symptoms include nausea, vomiting, weakness, frequent urination, and kidney problems.
        Kidney damage from too much calcium.
        Calcification of soft tissues, such as blood vessels, heart, and lungs.''')
    else:
        print(f'vitaminas d below upper limit (0.1mg): {MVA["vitaminas d3"]}')


# insert_to_MVA(MVA,Amino_acid_sup_one) # 1/3
# print(f'MVA:{MVA}\n')
# insert_to_MVA(MVA,Multi_vitamin_sup_one)# 1/1
# print(f'MVA:{MVA}\n')

# insert_to_MVA(MVA,Amino_acid_sup_one) # 2/3
# print(f'MVA:{MVA}\n')
# insert_to_MVA(MVA,Potassium_supplement_one) # 1/1
# print(f'MVA:{MVA}\n')
# insert_to_MVA(MVA,Multi_vitamin_sup_two) # 1/2
# print(f'MVA:{MVA}\n')
# insert_to_MVA(MVA,Amino_acid_sup_one) # 3/3
# print(f'MVA:{MVA}\n')


insert_to_MVA(MVA,Multi_vitamin_sup_one)# 1/1
print(f'MVA:{MVA}\n')

insert_to_MVA(MVA,Multi_vitamin_sup_two) # 1/2
print(f'MVA:{MVA}\n')


# insert_to_MVA(MVA,Potassium_supplement_one) # 1/1
# print(f'MVA:{MVA}\n')

# insert_to_MVA(MVA,Amino_acid_sup_one) # 1/3
# print(f'MVA:{MVA}\n')

# insert_to_MVA(MVA,Multi_vitamin_sup_two) # 1/2
# print(f'MVA:{MVA}\n')

# insert_to_MVA(MVA,Amino_acid_sup_one) # 2/3
# print(f'MVA:{MVA}\n')



check_limit(MVA)


