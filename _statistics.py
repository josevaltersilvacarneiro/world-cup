"""The functions of this file are responsible
for returning the statistical data.

"""

def _number_of_goals_in_the_group(games : dict, group : str) -> int:
    """This function looped all matches in the group
    passed as argument and adds up all goals made in
    the variable called 'num_of_goals_in_the_group'.
    At the end, returns it.

    games = {
        'A' : [
            [
                first_team,
                second_team,
                num_of_goals_for_the_first_team,
                num_of_go...         second_team,
                .
                .
                .
            ],
            .
            .
            .
        ],
        .
        .
        .
    }

    num_of_goals_in_the_group = (
        (games[group][i][0] + games[group][i][1]) + ... + (games[group][j][0] + games[group][j][1])
    ), 0 <= i < j, j = len(games[group])
    
    """

    num_of_goals_in_the_group : int = 0;

    for game in games[group]:

        num_of_goals_in_the_group += game[2] + game[3];

    return num_of_goals_in_the_group;

#-----------------------------------------------------------#
#------------------------- Public --------------------------#

def group_goal_average(games : dict, group : str) -> float:

    # Reference                                                #
    # https://pt.wikipedia.org/wiki/M%C3%A9dia_aritm%C3%A9tica #

    num_of_games : int = len(games[group]);

    # ZeroDivisionError                                        #

    return 0 if num_of_games == 0 else _number_of_goals_in_the_group(games, group) / num_of_games;

def goal_average(games : dict) -> float:
    """This function returns the average
    number of goals in the World Cup.

    """

    num_of_goals : int = 0;  # goal accumulator variable #
    num_of_games : int = 0;  # game accumu...   variable #

    # Loop all groups and add the number of goals to the #
    # corresponding accumulator variable. Idem for the   #
    # num of matches                                     #
 
    for key, value in games.items():
        num_of_goals += _number_of_goals_in_the_group(games, key);
        num_of_games += len(value);

    # ZeroDivisionError                                  #

    return None if num_of_games == 0 else num_of_goals / num_of_games;

def most_goals_in_a_game(games : dict) -> list:

    # Reference                                                                     #
    # https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list #

    data : list = [];

    for games_in_the_group in games.values():
        for game in games_in_the_group:

            max_number_of_goals_in_the_game = max(game[2], game[3]);
            max_number_of_goals_registered = max(data[2], data[3]) if data else -1;

            if max_number_of_goals_in_the_game > max_number_of_goals_registered:
                data = game;

    return data;
