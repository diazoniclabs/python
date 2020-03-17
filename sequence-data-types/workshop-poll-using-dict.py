responses = {}

flag = True

while flag:
    
    name = input('What is your name? ')
    workshop = input(' What workshop you want to attend? ')
    
    responses [name] = workshop
    
    repeat = input(' Would you like someone else respond also? no for exit')
    if repeat =='no':
        flag =False

print('Poll Results')
for name,workshop in responses.items():
    print(name + ' would like to attend ' + workshop)
        
