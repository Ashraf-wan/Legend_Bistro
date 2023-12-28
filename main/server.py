import time
from flask import Flask, request, jsonify
import pandas as pd
import json
import sqlite3 as sql
import base64

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
    signed_in = False

    def order(sign_stats):
        if 'id' in request.args:
            id = int(request.args['id'])
            item = None
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
                return str("Your order is " + item['name'] + " Pizza " + "and the price is " + item['price'])
                if sign_stats == True:
                    return "Sign In Complete",201
            else:
                return "Error: Invalid id provided. No menu item found with the specified id.", 404
        else:
            return "Error: No id field provided. Please specify an id.", 404


@app.route('/api/v1/newacc')
def api_new_account():
    headers = request.headers
    b64cred = headers.get("Auth")
    cc_info = headers.get("CC")
    con = sql.connect("creds.db")
    cur = con.cursor()

    def base64_decode(str1, str2):
        base64_string = str1 + "," + str2
        base64_bytes = base64_string.encode("ascii")
        decoded_b64_string_bytes = base64.b64decode(base64_bytes)
        decoded_b64_string = decoded_b64_string_bytes.decode("ascii")
        tmp = decoded_b64_string.split(",")
        return tmp

    tmp = base64_decode(b64cred, cc_info)
    username = tmp[0]
    password = tmp[1]
    cvc = tmp[2]
    cn = tmp[3]
    ed = tmp[4]
    statement = f"INSERT INTO “users” VALUES (‘{username}’,’{password}’,'{cvc}','{cn}','{ed}');"
    cur.execute(statement)


def verify_password(b64creds, typeauth):
    con = sql.connect("creds.db")
    cur = con.cursor()
    base64_string = b64creds
    base64_bytes = base64_string.encode("ascii")
    decoded_b64_string_bytes = base64.b64decode(base64_bytes)
    decoded_b64_string = decoded_b64_string_bytes.decode("ascii")
    tmp = decoded_b64_string.split(",")
    username = tmp[0]
    password = tmp[1]
    statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
    statement_admin = f"SELECT username from admin WHERE username='{username}' AND Password = '{password}';"
    if typeauth == "admin":
        cur.execute(statement_admin)
        if not cur.fetchone():
            return False
        else:
            return True
    else:
        cur.execute(statement)
        if not cur.fetchone():
            return False
        else:
            return True


@app.route('/api/v1/admin')
def api_admin():
    headers = request.headers
    authtmp = headers.get("Auth")
    authstat = verify_password(authtmp, "admin")
    if authstat:
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
            {"Pizza Sales": filelistint},
            index=fileliststr
        )
        image = plotdata.plot(kind="bar").get_figure()
        image.savefig('plot.png')
        time.sleep(1000)
    else:
        return "Wrong username or password", 401


app.run(port=5000)
