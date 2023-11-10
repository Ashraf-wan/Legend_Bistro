from flask import Flask, request, jsonify
import pandas as pd
import json

with open('Menu.json') as menu:
    menu_read = menu.read()
    menus_item = json.loads(menu_read)
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to Legend Bistro</h1>'


@app.route('/api/v1/menu')
def menu():
    return jsonify(menus_item)


@app.route('/api/v1/order')
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, return an error message.
    if 'id' in request.args:
        id = int(request.args['id'])
        item = None
        # Loop through the data and match results that fit the requested ID.
        # IDs are unique, but other fields might return many results
        for menu in menus_item:
            if menu['id'] == id:
                item = menu
                break
        with open('report.txt', 'r') as f:
            number1 = int(item['line']) - 1
            reading = f.readlines()
            line = int(reading[number1]) + 1
        reading[number1] = str(line) + "\n"
        with open('report.txt', 'w') as f:
            f.write("".join(str(item) for item in reading))
        if item:
            return str("Your order is " + item['name'] + " and the price is " + item['price'])
        else:
            return "Error: Invalid id provided. No menu item found with the specified id."
    else:
        return "Error: No id field provided. Please specify an id."


@app.route("/api/v1/name")
def api_name():
    # Check if a name was provided as part of the URL.
    # If name is provided, assign it to a variable.
    # If no name is provided, return an error message.
    if 'name' in request.args:
        user_name = request.args['name']
        return user_name
    else:
        return "Error: No name field provided. Please specify a name."


# file deepcode ignore MissingClose: <please specify a reason of ignoring this>

@app.route('/api/v1/paying')
def api_paying():
    # Check if a payment method was provided as part of the URL.
    # If payment method is provided, return a confirmation message.
    # If no payment method is provided, return an error message.
    if 'method' in request.args:
        return 'Thank you for purchasing from legend bistro, we will deliver your order in 5 minutes'
    else:
        return "Error: No method field provided. Please specify a method."
@app.route('/api/v1/admin')
def api_admin():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'AdminPass':
        f = open('report.txt', 'r')
        filetmp = f.read()
        filelisttmp = filetmp.split('\n')
        filelist = []
        for listtmp in filelisttmp:
            if listtmp.isdigit():
                filelist.append(int(listtmp))
            else:
                filelist.append(listtmp)
        filelistint = [x for x in filelist if isinstance(x, int)]
        fileliststr = [x for x in filelist if isinstance(x, str)]
        plotdata = pd.DataFrame(
            {"Pizza Type": [filelistint]},
            index=[fileliststr]
        )
        plotdata.plot(kind="bar")
    else:
        return "Error: Wrong Password from the user", 401

app.run(port=5000)