import requests
import time

server = input("Enter the server IP address: ")
print("""

                 __          
 /  _ _ _   _/  / _)' __/_   
(__(-(/(-/)(/  /(_)/_) // () 
    _/                       

Welcome To Legend Bistro

[1]List the menu  
[2]Order          
""")

choice = input("What do you want to do?\n")

if choice == "1":
    response = requests.get(server + '/api/v1/menu')
    # print the menu
    print("\nLegend Bistro Menu\n")
    for item in response.json():
        print(item['id'], item['name'], item['price'])
elif choice == "2":
    user_name = input("What is you name?\n")
    user_order = input("What would you like to order?\n")
    order = requests.get(server + '/api/v1/order?id=' + user_order)
    print(order.content.decode('utf-8'))
    print("....")
    time.sleep(5)
    method_payment = input("How would you like to pay?\n")
    pay = requests.get(server + '/api/v1/paying?method=' + method_payment)
    print(pay.content.decode('utf-8'))
    requests.get(server + '/api/v1/name?name=' + user_name)
else:
    print("invalid options")
