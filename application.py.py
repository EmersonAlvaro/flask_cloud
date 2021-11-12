from flask import Flask, jsonify
import numpy as np

application = app = Flask(__name__)

@application.route('/')
def index():
    return 'Hello Emerson \n'

@application.route('/random/<n>')
def randomvalues(n):
    values = np.random.randint(0, 10, int(n))
    result = {'values' : values.tolist()}
    return jsonify(result)

if __name__ == '__main__':
  application.run(debug=True)