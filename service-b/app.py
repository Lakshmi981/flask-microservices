from flask import Flask
import requests

app = Flask(__name__)

@app.route('/greet')
def greet():
    response = requests.get('http://localhost:5000/hello')
    return f"Service B says: '{response.text}' and adds ✨✨✨"

if __name__ == '__main__':
    app.run(port=5001)
