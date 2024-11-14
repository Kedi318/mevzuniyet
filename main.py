from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/1')
def one():
    return render_template("1.html")

@app.route('/2')
def two():
    return render_template("2.html")

@app.route('/3')
def three():
    return render_template("3.html")

@app.route('/4')
def four():
    return render_template("4.html")

@app.route('/5')
def five():
    return render_template("5.html")

@app.route('/6')
def six():
    return render_template("6.html")

@app.route('/7')
def seven():
    return render_template("7.html")

@app.route('/8')
def eight():
    return render_template("8.html")

@app.route('/9')
def nine():
    return render_template("9.html")

@app.route('/10')
def ten():
    return render_template("10.html")

@app.route('/11')
def eleven():
    return render_template("11.html")

@app.route('/12')
def twelve():
    return render_template("12.html")

app.run(debug=True)