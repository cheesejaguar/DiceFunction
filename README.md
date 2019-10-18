# DiceFunction
Dicestring -> roll

Input can be one or more dice, with multiples separated by commas, ie:

`1d6`
`1d6,2d4`
`1d20,3d4,1d6`


Response is a JSON with keys for each of the type of dice rolled, and the values for each key being an array of the roll results.  Additionally there is a key for `sum` which is the sum of all dice rolled.  

dice.py is a standalone Flask server for the dice roll function, where dice_func.py is the version formatted for Google Cloud Functions.  The flask version accepts the URI `/dice_string/1d6,2d10` where the Cloud Function requires a URL param: `?dice_string=1d6,2d10
