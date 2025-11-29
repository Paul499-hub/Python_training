input='1 7 16 -7 15 -15 3 -3 4 5 -4 6 -7 2 -2 12 -1 1'
input=input.split()
glist = input
min=0

for i in range(len(glist)):
    current=int(glist[i])
    if i==0:
        min=current
    if abs(current)<abs(min):
        min=current
    if abs(current and current>min)==abs(min):
        min=current
print(min)