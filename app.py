from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! V2'

if __name__ == '__main__':
    app.run(debug=True, port=8080)