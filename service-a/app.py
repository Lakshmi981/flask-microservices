from flask import Flask

app = Flask(__name__)

@app.route('/hello')
print("Lakshmee was here!")
def hello():
    return "Hello from Service A!"

if __name__ == '__main__':
    app.run(port=5000)
