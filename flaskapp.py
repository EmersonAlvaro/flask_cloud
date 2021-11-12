from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Emerson \n'

@app.route('/random/<n>')
def randomvalues(n):
    values = np.random.randint(0, 10, int(n))
    result = {'values' : values.tolist()}
    return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True)