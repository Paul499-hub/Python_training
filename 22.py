n = 3
ex=['-12','-5','-137', '7', '-9', '10']
min=0
for i in range(len(ex)):

    t=int(ex[i])

    if i==0:
        min=int(ex[0])

    if abs(t)<abs(min):
        min=t
print(min)