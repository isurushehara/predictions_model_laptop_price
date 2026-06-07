from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.POST == 'POST':
        ram = request.form['ram']
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)