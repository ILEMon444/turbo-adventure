from flask import Flask

app = Flask(__name__)

@app.route('/main')

@app.route('/')
def index():
    return "<h1>Main page</h1>"

@app.route('/about')
def about():
    return "<h1>About us</h1>"

if __name__ == '__main__':
    app.run(debug=True)
