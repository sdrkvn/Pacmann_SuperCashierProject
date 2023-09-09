import datetime #importing the date and time of transaction
import uuid #importing the user-generated ID 
from cashier import * #importing the Transaction module to start the cashier features

#the below section is for the home page
print ('*' *55)
print ('\U0001F64F' 'Welcome to An-Mart!' '\U0001F64F')
print ('*' *55)
print ()

while True:
    buyer_name = input('Please enter your name here:')
    break

from datetime import datetime #importing the date & time to be shown

dt = datetime.now()
print (f'Date/Time:', dt) #showing the date and time
ID = uuid.uuid1() #generating the transaction ID

print ('*'*55)

print (f'Hello, {buyer_name}')
print (f'Date/Time = {dt}')
print (f'Transaction ID = {ID}')
       
print ('*'*55)

trnsct_123 = Transaction('Item', 'Price', 'Quantity', 'Shopping Cart')

end_programme = True

while end_programme:
    print ('Your cart:')
    
    print ('-'*55)
    print (f'1. Add item')
    print (f'2. Edit item name')
    print (f'3. Edit item quantity')
    print (f'4. Edit item price')
    print (f'5. Delete item')
    print (f'6. Reset shopping cart')
    print (f'7. Check order')
    print (f'8. Check out')
    print ('-'*55)
    
    boolean = True
    buyer_input = 0

    while boolean:
        try:
            buyer_input = int(input('Please select your choice:'))
            len_choices = range (1,9)
            if buyer_input not in len_choices:
                print (f'Please select between options 1-8')
            else:
                boolean = False
        except ValueError:
            print('Please select between options 1-8')
        
        if buyer_input == 1: #if buyer selects option 1
            print ('Adding new item to shopping cart')
            print (trnsct_123.add_item())
        
        elif buyer_input == 2: #if buyer selects option 2
            print ('Updating item name in your cart')
            print (trnsct_123.update_item_name())
        
        elif buyer_input == 3: #if buyer selects option 3
            print ('Updating item quantity in your cart')
            print (trnsct_123.update_item_quantity())
        
        elif buyer_input == 4: #if buyer selects option 4
            print ('Updating item price in your cart')
            print (trnsct_123.update_item_price())
    
        elif buyer_input == 5: #if buyer selects option 5
            print ('Removing item from your cart')
            print (trnsct_123.delete_item())
               
        elif buyer_input == 6: #if buyer selects option 6
            print ('Resetting all the items on your cart')
            print (trnsct_123.reset_transaction())
            print ('Your cart has been reset and is now empty')
               
        elif buyer_input == 7: #if buyer selects option 7
            print ('Here is your cart')
            print (trnsct_123.check_order())
    
        elif buyer_input == 8: #if buyer selects option 8
            print ('Checking out your cart')
            print (trnsct_123.check_order())
            print (trnsct_123.total_price_disc())
            print ('Thank you for shopping at An-Mart! Please come again!') #printing a goodbye message
               
            end_programme = False
