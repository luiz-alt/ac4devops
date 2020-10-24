import os
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def fibonacci():
    i = 1
    a, b = 1 , 1
    val = [1,1]

    while i != 50:
        c = a+b
        a, b = b, c
        val.append(c)        
        i += 1

    return val

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
