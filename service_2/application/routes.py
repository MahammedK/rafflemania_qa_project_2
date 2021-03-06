from application import app
from flask import Flask, Response, request
import random

raffleletters = ["O", "L", "M", "K", "A", "U", "B", "N", "I", "D", "H", "V", "E"]

@app.route('/letters', methods=['GET'])
def letters():
    letter_selected = random.choice(raffleletters)
    return Response(f"{letter_selected}", mimetype='text/plain')