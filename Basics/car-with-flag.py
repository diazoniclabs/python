'''Usage of Flag Register in Python Programming'''

a= False   # Take a variable for Flag
while True:
    command=input("Enter the command: ")
    if command=="help":
        print("start - to start the car")
        print("stop - to stop")
        print("quit - to exit")
    elif (command=="start" and a==True):
        print(" Car is already started")
    elif (command=="start" and a==False):
        a=True
        print("Car Started")
    elif (command=="stop" and a==False):
        print(" Car is already stopped")
    elif (command=="stop" and a==True):
        a=False
        print("Car stopped")
    elif command=="quit":
        break
    else:
        print("I dont understand")
