#Print 1 100
# WHEN CURRENT NUMBER MULTIPLE OF 3 print FIZZ instead 
# WHEN CURRENT NUMBER MULTIPLE OF 5 print BUZZ instead of number
# WHEN CURRENT NUMBER MULTIPLE OF 3 AND 5 print FizzBuzz


for i in range(1,101):
    if i%3==0 and i%5!=0:
        print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('FizzBuzz')
    else:
        print(f'{i}')
    
    