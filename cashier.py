from tabulate import tabulate

header = ["No", "Item name", "Quantity", "Price IDR"] #this is the header for the shopping cart table that we will use

class Transaction: #this is the main class which will contain all the methods and features
    def __init__ (self, item, quantity, price, cart):
        self.item = item
        self.quantity = quantity
        self.price = price
        self.cart = []
    
    def add_item(self): #this is the feature to add an item to cart
        while True:
            self.item = (input ('Please type item name: ')) #this is where customer enters item name
            if self.item.isnumeric():
                print ('Invalid input, please enter item name.')
            else:
                break
                
        while True:
            try:
                self.quantity = int(input('Please enter item quantity: ')) #this is where customer enters item quantity
                break
            except ValueError:
                print ('Invalid input, please enter item quantity: ')
                
        while True:
            try:
                self.price = int(input('Please enter item price: ')) #this is where customer enters item price
                break
            except ValueError:
                print ('Invalid input, please enter item price.')
                                                                       
        transaction_list = [len(self.cart) +1, self.item, self.quantity, self.price]
        
        self.cart.append(transaction_list)
                                       
        return tabulate (self.cart, headers=header, tablefmt='grid') #this will allow the shopping cart to be tabulated and shown as grid
                                       
    def update_item_name(self): #this is to update or revise an existing item in the cart
        item_index = int(input('Please enter which item to be updated: ')) -1
        if item_index < 0 or item_index >= len(self.cart):
            print ('!WARNING! Item is not in the cart, please enter existing item number.')
            return
            
        new_item = input('Please enter new item: ')
                                       
        self.cart[item_index][1] = new_item
                                       
        return tabulate (self.cart, headers=header, tablefmt='grid')
        
    def update_item_quantity(self): #this is to update or revise an existing item quantity in the cart
        item_index = int(input('Please enter which item quantity to be updated: ')) -1
        if item_index <0 or item_index >= len(self.cart):
            print ('!WARNING! Item quantitiy is not in the cart, please update existing quantity: ')
            return
        
        new_quantity = input('Please enter new item quantity: ')
        
        self.cart[item_index][2] = new_quantity
        
        return tabulate (self.cart, headers=header, tablefmt='grid')
        
    def update_item_price(self): #this is to update or revise an existing item's price in the cart
        item_index = int(input('Please enter which item price to be updated: ')) -1
        if item_index <0 or item_index >= len(self.cart):
            print ('!WARNING! Item price is not in the cart, please update existing item price.')
            return
        
        new_item_price = input('Please enter new item price: ')
        
        self.cart[item_index][3] = new_item_price
        
        return tabulate (self.cart, headers=header, tablefmt='grid')
        
    def delete_item(self): #this is to remove an item, along with quantity and price, from the cart
        item_index = int(input('Please choose which item to be removed: ')) -1
        if item_index <0 or item_index >= len(self.cart):
            print ('!WARNING! Invalid item')
            return
        
        self.cart.pop (item_index)
        
        return tabulate (self.cart, headers=header, tablefmt='grid')
    
    def reset_transaction(self): #this is to reset the entire shopping cart to an empty one
        self.cart = []
        
        return tabulate (self.cart, headers=header, tablefmt='grid')
    
    def check_order(self): #this is to check if the orders are correct
        print ('Order is correct. Here is your cart:')
        
        return tabulate (self.cart, headers=header, tablefmt='grid')
    
    def total_price_disc(self): #this will show the total price, and if any discount is rewarded
        base_price = 0
        for item in self.cart:
            price = item[3]
            quantity = item[2]
            base_price = price*quantity
            
        if base_price > 500000:
            discount = base_price*0.1
            discount_price = base_price - discount
            return f'Great, you receive 10% discount! Your shopping price is now: IDR{discount_price}'
        
        elif base_price > 300000:
            discount = base_price*0.08
            discount_price = base_price - discount
            return f'Great, you receive 8% discount! Your shopping price is now: IDR{discount_price}'
        
        elif base_price > 200000:
            discount = base_price*0.05
            discount_price = base_price - discount
            return f'Great, you receive 5% discount! Your shopping price is now: IDR{discount_price}'
        
        else:
            print (f'your total shopping price is: IDR{base_price}')
        
