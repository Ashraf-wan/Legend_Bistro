from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api
import time
import json

menus_item = [
    {
        "id": 1,
        "name": "Classic Pizza",
        "price": "$8.00",
        "line": 2
    },
    {
        "id": 2,
        "name": "Pepperoni Pizza",
        "price": "$10.00",
        "line": 4
    },
    {
        "id": 3,
        "name": "Cheese Pizza",
        "price": "$12.00",
        "line": 6
    },
    {
        "id": 4,
        "name": "Meat Lover's Pizza",
        "price": "$16.00",
        "line": 8
    },
    {
        "id": 5,
        "name": "Veggie Pizza",
        "price": "$14.00",
        "line": 10
    },
    {
        "id": 6,
        "name": "Hawaiian Pizza",
        "price": "$13.00",
        "line": 12
    },
    {
        "id": 7,
        "name": "Margherita Pizza",
        "price": "$11.00",
        "line": 14
    },
    {
        "id": 8,
        "name": "BBQ Chicken Pizza",
        "price": "$15.00",
        "line": 16
    },
    {
        "id": 9,
        "name": "Supreme Pizza",
        "price": "$17.00",
        "line": 18
    },
    {
        "id": 10,
        "name": "Mushroom Pizza",
        "price": "$12.00",
        "line": 20
    }
]

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
        with open('report.txt','r') as f:
            number1 = int(item['line']) - 1
            reading = f.readlines()
            line = int(reading[number1]) + 1
        reading[number1] = str(line) + "\n"
        with open('report.txt','w') as f:
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


app.run(port=5000, debug=True)
