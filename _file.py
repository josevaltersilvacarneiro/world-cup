""" The functions of this file are resposible
for getting the data in the file when the 
program is started - get() - and pushing the
data contained in the working memory when the 
program is finished - push().

"""

import json

_FILE = 'data.json'

def get() -> tuple:

    try:

        with open(_FILE) as fil:

            data = json.load(fil);

            cup = data['cup'];
            games = data['games'];

    except FileNotFoundError:
        groups : list = [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
            ];

        cup : dict = {group : list() for group in groups};
        games : dict = {group : list() for group in groups};

    return cup, games;

def push(cup : dict, games : dict) -> None:

    with open(_FILE, 'w') as fil:

        data = {
                'cup' : cup,
                'games' : games,
            };

        json.dump(data, fil);

