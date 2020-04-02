def fruit(color,texture):
    if(color == 'red' and texture =='smooth'):
        print("Apple")
    elif (color == 'red' or texture =='smooth'):
        print(" Maybe an Apple")
    elif(color == 'yellow' and texture =='rough'):
        print("Lemon")
    elif(color == 'yellow' or texture =='rough'):
        print("Maybe a lemon")

while True:
    
    c = input("Enter the color")
    t = input("Enter the texture")
    if(c==("red" or "yellow") and t==("smooth" or "rough")):
        fruit(c,t)
    elif(c == "q" or t == "q"):
        break
    else:
        print("Enter correct input")

        
        

