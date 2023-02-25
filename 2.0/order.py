import time
from numpy import random

x = random.randint(50)

def loop():

 order = input("What would you like?\n")

 print("Sound delicious, your " + order + " will be delivered\n")

 time.sleep(10)

 print("Here is your " + order + ",enjoy.\n")

 time.sleep(10)

 nd = input("Would you like a second order? ")

 if nd == "yes":
   loop()
 else:
   print("This is the recipt,you can pay the at the cashier")

   print("""

                    Legend Bistro
  Recipt is autogenarated using python and coded by Legend Bistro Inc
\n """ + order + " " + str(x) + """$\n""")

   print("\n")

   print("Hello,please give me the recipt")

   time.sleep(3)

   howtopay = input("How do you want to pay? ")

   if howtopay == "cash":
       print("Sorry " + howtopay + " is not accepted.")
   else:
       print(
        "Your payment is accepted,Thank you for purchasing our product.Goodbye!"
       )

loop()