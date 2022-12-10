"""The functions of this file are responsible
for returning the statistical data.

"""

def _number_of_goals_in_the_group(games : dict, group : str) -> int:

    num_of_goals_in_the_group : int = 0;

    for game in games[group]:

        num_of_goals_in_the_group += game[2] + game[3];

    return num_of_goals_in_the_group;

#-----------------------------------------------------------#
#------------------------- Public --------------------------#

def group_goal_average(games : dict, group : str) -> float:

    num_of_games : int = len(games[group]);

    return 0 if num_of_games == 0 else _number_of_goals_in_the_group(games, group) / num_of_games;

def goal_average(games : dict) -> float:

    num_of_goals : int = 0;
    num_of_games : int = 0;

    for key, value in games.items():
        num_of_goals += _number_of_goals_in_the_group(games, key);
        num_of_games += len(value);

    return None if num_of_games == 0 else num_of_goals / num_of_games;

def most_goals_in_a_game(games : dict) -> list:

    data : list = [];

    for games_in_the_group in games.values():
        for game in games_in_the_group:

            max_number_of_goals_in_the_game = max(game[2], game[3]);
            max_number_of_goals_registered = max(data[2], data[3]) if data else -1;

            if max_number_of_goals_in_the_game > max_number_of_goals_registered:
                data = game;

    return data;
