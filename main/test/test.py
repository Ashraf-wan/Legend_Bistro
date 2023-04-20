import time, requests
x = 4
user_order = str(x)
user_name = str("bob")
server = "http://127.0.0.1:5000"
method_payment = "cash"
print("Test 1: Ordering a pizza")
try:
    order = requests.get(server + '/api/v1/order?id=' + user_order)
    print(order.content.decode('utf-8'))
    time.sleep(2)
    print("\033[1;32;40m Test 1 Successful")
except:
    print("failed")