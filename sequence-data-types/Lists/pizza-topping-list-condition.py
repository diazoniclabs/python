available_toppings = ['onions','olives','cheese','capsicum']

required_topping = input('What topping do you want?')

if required_topping in available_toppings:
    print(" Adding " + required_topping + " Finished Pizza with " 
          + required_topping)
else: 
    
    print("Sorry, we dont have " + required_topping 
          + " Finished making Pizza without "+ required_topping)
