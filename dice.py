from random import randint
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/roll/<input>')
def roll_dice(input):
    response = dict()
    dice = input.split(",")
    dice = [each.encode("ascii", "ignore") for each in dice]
    for each in dice:
        num, sides = each.split("d")
        response.update({sides: [randint(1,int(sides)+1) for roll in range(int(num))]})
    response["sum"] = sum([item for sublist in response.values() for item in sublist])
    return jsonify(response)

if __name__ == '__main__':
    app.run()
