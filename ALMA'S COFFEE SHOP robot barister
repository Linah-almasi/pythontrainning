class customer():
  
  def welcome_customer(customer_name): 
    print("\n")
    print(f"Welcome to our online coffee  shop ALMA'S COFFEE SHOP,{customer_name}!\n")
    print("We are thrilled to have you here.\n")
    print("Feel free to browse our wide range of coffee and enjoy your shopping experience!\n")

  customer_name = input("Please enter your name: \n" ) 

  welcome_customer(customer_name)

  print("We deal in a wide range progucts as listed below : \n")

  products = {
        "latte": 0.99,
        "cappuccino": 0.50,
        "espresso": 0.75,
        "mocha": 1.50,
        "americano":0.54,
        "turkish coffee":1.00,
        "cold brew":0.98,
    }

  for product, price in products.items():
        print(f"{product}: ${price}")
    
  print("\n")

  print("what would you like to have today,?\n" + customer_name )

  item = input("Please input your today's order: "  +  customer_name + "\n")

  if item == "latte":
        item_price = 0.99
  elif item == "cappuccino":
        item_price = 0.50
  elif item == "espresso":
        item_price = 0.75
  elif item == "mocha":
        item_price = 1.50
  elif item =="americano":
        item_price = 0.54
  elif item == "turkish coffee":
        item_price = 1.00
  elif item == "cold brew":
        item_price =0.98
  else:
        print(f"What you orderd, {customer_name}! is not in the menu")
    
        exit()
    
  print(f"The price for the {item} category is ${item_price}. \n")

  quantity = int (input(f"How many cups of the {item},would you like to have \n" ))

  total_price = item_price * quantity

  print(f"The total price for {item} coffees is ${total_price}.")

  print(f"Please confirm your payment ,{customer_name}")

  output = input("Have you received an online recipt for payment? \n" )

  if output =="yes":
    
       print("Wait for our delivery person to deliver your coffee(s) \n" + customer_name )
    
  else:
    
        print("Kindly confirm if you have made the payments correctly or if there was a problem please re-order again")
    
  print(f"""Thank you {customer_name} for shopping with us \n
    See you next time when you want the best coffee in town \n
    ALMA'S COFFEE SHOP the best place to shop for quality coffee \n""")

    




    
