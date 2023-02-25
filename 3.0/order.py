import time
from numpy import random
import os

x = random.randint(50)

def loop():

 order = input("What would you like?\n")

 quantity = input("How many " + order + " would you want? ")

 price = 12

 total = price * int(quantity)

 print("Sound delicious, your " + order + " will be delivered\n")

 time.sleep(10)

 print("Here is your " + order + ",enjoy.\n")

 time.sleep(10)


 print("This is the recipt,you can pay the at the cashier")
 print("""

                    Legend Bistro
  Recipt is autogenarated using python and coded by Legend Bistro Inc
\n """ + order + " " + str(total) + """$\n""")
 print("Hello,please give me the recipt")

 time.sleep(3)

 howtopay = input("How do you want to pay? ")

 if howtopay == "cash":
   print("Sorry " + howtopay + " is not accepted.")
 else:
    print(
        "Your payment is accepted,Thank you for purchasing our product.Goodbye!"
    )
    file = os.system("cat total.txt")
    all_total = int(file) + int(total)
    os.system('echo "' + str(all_total) + '" ' + ">" + " total.txt")
loop()