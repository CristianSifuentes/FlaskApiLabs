from flask import jsonify

def response(data):
    return jsonify({
        'succes': True,
        "data": data
    }),200
