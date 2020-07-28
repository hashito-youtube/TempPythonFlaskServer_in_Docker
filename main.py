from flask import Flask
import os
app = Flask(__name__)

PORT=os.environ.get("PORT","80")


@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=int(PORT),host="0.0.0.0")