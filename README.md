# Retail Self-Checkout System

This is a Python Object-Oriented Programming project for Python I-II course from Pacmann.io | September 2023

**Introduction**

The background of the project is a fictional case study from the Pacmann.io team. Andi (not a real person), and Indonesian-based shop owner is looking to elevate the customer journey by automating the check-out system for his store. The system will enable customers to insert, edit, and check their items and orders before going to check out. To that end, Andi needs programmers to create a self-checkout program that have several feature requirements. 

**Features/Requirements**

Andi decided that the self-checkout system should have the following features:

    1. ``` add_item() ``` this is to add an item, the quantity, and price of the item to the cart
    2. ``` update_item_name() ``` this is to update/edit an existing item in the cart
    3. ``` update_item_quantity() ``` this is to update/edit the quantity of an existing item in the cart
    4. ``` update_item_price() ``` this is to update/edit the price of an existing item in the cart
    5. ``` delete_item() ``` this is to delete one row of item in the cart including the name, price, and quantity
    6. ``` reset_transaction() ``` this is to reset the entire cart into an empty one
    7. ``` check_order() ``` this is to check the current items in the cart
    8. ``` total_price_disc() ``` this is to see the total price of all the items in the cart, and apply discount, if any
    
These features were deemed essential to have in the system.

**Flowchart**

The program's chart is as follows:

![Pacmann.io_Project] (/Flowchart.png)

Every action taken by each functions will return the user to the main action prompt except the ```total_price_disc()``` which will then end the program.

**Test cases**

Test case 1: Add item with ```add_item()``` 
The buyer will add an item of their choosing with this option. They want to add the following:
    1. Fried Chicken. Quantity:2. Price: 20000
    2. Toothpase. Quantity:3. Price: 15000

The journey goes like this. The user enters their name below:

(/img1.png)

Then, the date, time, and transaction ID and the main action prompt will appear

(/img2.png)

Then, the user must choose option 1 which will execute ```add_item()```, and enter the first item name (Fried Chicken), quantity (2), and price (20000). 

(/img3.png)

Then, the user must repeat choosing option 1 and do the same for Toothpaste. Afterwards, it will look like this:

(/img4.png)

Suddenly, the user, being the forgetful person that they are, remembers that they actually did not want to buy toothpaste and decides to remove it from the cart. They must use option 5, which will execute ```delete_item()``` and then choose 2 to remove toothpaste from cart. The cart will look like this

(/img5.png)

Alas, this one customer really is forgetful. They forgot that they are on a strict diet and must not eat chickens. So they must remove all the items on the cart. They must choose option 6, which will run ```reset_transaction()``` and empty the cart.

(/img6.png)

Now, after deciding that they've had enough fun at the store, the customer wants to go home and chill. He must check out his cart by choosing option 8, which will execute ```total_price_disc()``` and ends the program for good.

(/img7.png)

The customer should now be happy that they received discount due to their excessive spending and goes home in peace. 

**Conclusion**

This program is a simple yet effective way to elevate your customer journey. However, this may not be suitable for a large retail store where customers may purchase many items and in bulk as they would have to add each item one by one. 

Also, this is where the author realises that programming is not easy.

Best regards,
Your fellow homo sapiens
