import time, requests
x = 4
user_order = str(x)
user_name = str("bob")
server = "http://127.0.0.1:5000"
method_payment = "cash"
adminpass = "AdminPass"
print("Test 1: Ordering a pizza")
try:
    order = requests.get(server + '/api/v1/order?id=' + user_order)
    time.sleep(2)
    print("\033[1;32;40m Test 1 Successful")
except:
    print("\033[1;31;40m Test 1 failed")
time.sleep(2)
print("Test 2: Paying for the order")
try:
    pay = requests.get(server + '/api/v1/paying?method=' + method_payment)
    time.sleep(2)
    print("\033[1;32;40m Test 2 Successful")
except:
    print("\033[1;31;40m Test 2 failed")
time.sleep(2)
requests.get(server + '/api/v1/name?name=' + user_name)
