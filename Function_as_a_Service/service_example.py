from flask import Flask, request, jsonify


# -*- coding: utf-8 -*-

'''
service_example.py
~~~~~~~~~~~~~~~~~~~~
App implements a simple microservice example in Flask. Function shift will add 1 or subtract 1 from list variable 'arr', depending on string variable 'method'.
'''

def shift(arr, method='add'):
    try:
        if method == 'add':
            return [o for o in map(lambda x: x + 1, arr)]
        elif method == 'subtract':
            return [o for o in map(lambda x: x - 1, arr)]
        else:
            return "method must be either add or subtract"
    except TypeError:
        return 'must be a list of numeric values'

app = Flask(__name__)

@app.route('/shift_compute', methods=['POST'])
def sentiment_compute():
    # converts json to native python dictionary datatype
    req = request.get_json(force=True)
    # parses dictionary for input parameters
    arr, method = req['data'], req['method']
    # returns function output as 'result'
    return(jsonify({"result": shift(arr, method)}))

if __name__ == "__main__":
    PORT = 8080
    DEBUG = True

    app.run(host='0.0.0.0', port=8080, debug=True)

# example call:
# curl -H "Content-Type: application/json" -X POST -d '{"data":[1,4,6], "method":"add"}' localhost:8080/shift_compute
