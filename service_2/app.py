from flask import Flask, Response
import random

app = Flask(__name__)

raffle_letters = ["O", "L", "M", "K", "A", "U", "B", "N", "I", "D", "H", "V", "E"]

@app.route('/letters', methods=['GET'])
def letters():
    letter_selected = random.choice(raffle_letters)
    return Response(f"{letter_selected}", mimetype='text/plain')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)