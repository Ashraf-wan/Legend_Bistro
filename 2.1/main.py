import os

os.system("clear")

print("""

                 __          
 /  _ _ _   _/  / _)' __/_   
(__(-(/(-/)(/  /(_)/_) // () 
    _/                       

Welcome To Legend Bistro

[1]List the menu  [3]Admin panel
[2]Order          [4]Employee login
""")

lb = input("What do you want to do?\n")

if lb == "1":
    print(
        "pepperoni pizza,home special,cheese pizza,ham and cheese pizza,sausage pizza"
    )
elif lb == "2":
    os.system("python3 order.py")
elif lb == "3":
    code = input("Please put the code. ")
    if code == "1021":
        os.system("python3 admin.py")
    else:
        print("Sorry,wrong code.")
elif lb == "4":
    code1 = input("Please put the code. ")
    if code1 == "2021":
        os.system("python3 employee.py")
elif "refund" in lb:
    print("Here is you refund.")
else:
    print("invalid options")
