from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/admin?pass=420")
def panel():
    return render_template('panel.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)