def roll_dice(request):
    from random import randint
    from flask import jsonify
    response = dict()
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_args and 'dice_string' in request_args:
        dice = request_args['dice_string']
    elif request_json and 'dice_string' in request_json:
        dice = request_json['dice_string']

    dice = dice.split(",")
    dice = [each.encode("ascii", "ignore") for each in dice if each]
    for each in dice:
        num, sides = each.decode().split("d")
        response.update({sides: [randint(1,int(sides)) for roll in range(int(num))]})
    response["sum"] = sum([item for sublist in response.values() for item in sublist])
    return jsonify(response)
