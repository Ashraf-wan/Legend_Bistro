import time
from numpy import random
import os

x = random(100)

print("Welcome to Legend Bistro!\n")

name = input("What is your name?\n")

code = '1021'

if name == code:
    os.system("python3 admin.py")
else:

    print("Hello " + name + ",thank you for coming in today.\n\n")

    print(
        "Here is the menu " + name +
        " pepperoni pizza,home special,cheese pizza,ham and cheese pizza,sausage pizza\n\n"
    )

    order = input("What would you like?\n")

    print("Sound delicious, your " + order + " will be delivered\n")

    time.sleep(10)

    print("Here is your " + order + ",enjoy.\n")

    time.sleep(10)

    print("This is the recipt " + name + ",you can pay the at the cashier")

    print("""

                    Legend Bistro
  Recipt is autogenarated using python and coded by Legend Bistro Inc
\n """ + order + " " + str(x) + """$\n""")

    print("\n\n")

    print("Hello " + name + ",please give me the recipt")
    
    howtopay = input("How do you want to pay? ")

    if howtopay == "cash":
      print("Sorry " + howtopay + " is not accepted.")
    else:
      print("Your payment is accepted,Thank you for purchasing our product.Goodbye!")
