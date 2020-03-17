''' A simple calculator using functions'''

def sum(a,b):
    c = a+b
    print (c)
def dif(a,b):
    c = a-b
    print (c)
def mul(a,b):
    c = a*b
    print (c)
def div(a,b):
    c = a/b
    print (c)
while True:
    print(" CALCULATOR")
    a = int(input(' Enter 1st :'))
    b = int(input(' Enter 2nd :'))        
    print(' Enter the Operation ')
    choice =  input( ' A- Addition, S - Subtraction, M- Multiplication and D- Division ')
    if( choice  == 'A'):
        sum(a,b)
    elif( choice  == 'S'):
        dif(a,b)
    elif( choice  == 'M'):
        mul(a,b)
    elif( choice  == 'D'):
        div(a,b)
    else:
        print(' Wrong input')
