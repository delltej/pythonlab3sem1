#Tejveer singh
#22071721

#  empty dictionary to store the products and their brands
shoppingCart = {}
# Display the menu
print("Menu:-")
print("\nWELCOME TO THE AMANDO SHOPPING SITE")
print("Select 1.Add product to the cart \n")
print("Select 2.Search the product\n")
print("Select 3.Delete the product from the cart\n")
print("Select 4.Quit\n")
# Set the options variable to 0 to enter the loop
Options = 0
while (Options != 4):
  # for the choice of user

  Options = int(input("Enter your choice (Between 1 to 4): "))
  
 #add a product
  if Options == 1:
    user_input = int(input("Enter the number of product you want to add: "))

    v = 0

    while (v < user_input):
      lll = len(shoppingCart)
      if (lll < 5):
        B = input("Enter an item:- ")
        c = input("Enter the brand name:- ")
        shoppingCart.update({B: c})
        print("Product Inserted successfully")

      else:
        print("Cart is full")
      v = v + 1
#
  elif Options == 2:
    # If the product is found, print item and brand name
    A = input("Enter the item want to be search:- ")
    k = 0
    for i in shoppingCart.keys():
      if (i == A):
        print(i, ":", shoppingCart[i])
        k = 1
      else:
        pass
    if (k == 0):
      print("No product exists with this name")
#for delete of product
  elif Options == 3:
    if len(shoppingCart) == 0:
        print("Cart is empty, no item is found")
    else:
 # Get the product name from the user and remove it from the shopping cart
        A = input("Enter the product name: ")
        if A in shoppingCart:
            del shoppingCart[A]
            print("Product deleted from cart.")
        else:
            print("Product not found in cart.")
    # when user want to quiet      
  elif Options == 4:
    print("Thank you!!!")

  else:
    print("no option found")
# Print the final contents of the shopping cart
print(shoppingCart)


