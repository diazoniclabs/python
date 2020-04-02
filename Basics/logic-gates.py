def andgate(a,b):
    if a == 1 and b == 1:
      print(True)
    else:
      print(False)
def orgate(a,b):
    if a == 1 or b == 1:
      return True
    else:
      return False
while True:
    print(" And Or Logic Gates")
    a = int(input(' Enter a:'))
    b = int(input(' Enter b:'))        
    print(' Enter the Operation ')
    choice =  input( ' A- AND, O - OR ')
    if( choice  == 'A'):
        andgate(a,b)
    elif( choice  == 'O'):
        print(orgate(a,b))
    else:
        print(' Wrong input')
