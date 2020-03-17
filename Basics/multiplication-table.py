'''n = int(input(' Multiplication table of : '))
for i in range(1,11,1):
    print( n, '*' , i , '=' , n*i)'''


while True:
    n = input(' Multiplication table of : ')
    if( n== 'q'):
        break
    else:
        for i in range(1,11,1):
            print( n, '*' , i , '=' , int(n)*i)

print('Program Ended')

'''Here I have taken Type Casting for multiplying the value of n'''
