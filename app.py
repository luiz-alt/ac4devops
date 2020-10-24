import os
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def fibonacci():
   a = 1
   b = 0
   c = '0, '

   for i in range(51):
       t = a
       a = a + b
       b = t
       c += str(a) + '.'

    return c

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
