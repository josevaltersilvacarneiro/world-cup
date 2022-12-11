"""This file stores useful functions.

"""

from datetime import date, time

_YEAR : int = 2022;

def _get_all_teams_registered(cup : dict) -> list:
    """This function looped all the groups and
    stores all the teams found in the teams list.
    At the end, it returns.

    cup : dict = {
        'A' : [],
        'B' : [],
        .
        .
        .
        'H' : [],
    }

    """

    teams : list = [];

    for group in cup.values():
        teams.extend(group)

    return teams;

def _is_any_data_registered(data : dict) -> bool:
    """This function looped all the groups.
    If there is at least one element added,
    it returns True; else it returns False.

    data : dict = {
        'A' : [],
        'B' : [],
        .
        .
        .
        'H' : [],
    }

    """

    for element in data.values():

        if len(element) > 0:
            return True;

    return False;

def _number_of_data_registered(data : dict) -> int:
    """This function returns how many values have
    already been added to the data dictionary.

    data : dict = {
        key_1 : [],
        key_2 : [],
        .
        .
        .
        key_n : [],
    }

    """

    num_of_data_registered : int = 0;

    for value in data.values():

        num_of_data_registered += len(value);

    return num_of_data_registered;

def _max_number_of_games_registered(cup : dict) -> int:
    """Using a repetiton loop, all groups looped.
    By means of the Fundamental Counting Theorem,
    the number of possible games in each group is
    found and then added to the accumulator varia-
    ble called 'max_sum_of_games_registered'. At
    the end, it's returned.

    """

    max_num_of_games_registered : int = 0;

    for group in cup.keys():
        max_num_of_games_registered += max_number_of_games_registered_in_the_group(cup, group);

    return max_num_of_games_registered;

#--------------------------------------------------#
#--------------------- Public ---------------------#

def check(message : str) -> bool:
    """This function waits for the user
    to type y or N for the question
    passed as argument and returns
    True (Y) or False (any).

    """

    check = input(f'{message}: [y/N]').strip().upper();

    return check == 'Y';

def get_amount(message : str) -> int:

    # As long as amount isn't a number, run;
    # else return this number

    while not ( amount := input(message) ).isdecimal():
        print(f'{amount} isn\'t a number');

    return int(amount);

def get_option(options : list) -> int:

    # As long as option isn't in options, run;
    # else return this option

    while (
            ( option := get_amount('Type your option: ') ) not in options
        ): print(f'{option} isn\'t a valid option');

    return option;

def get_group(groups : dict) -> str:

    # As long as typed group isn't in groups, run;
    # else return this group

    while ( group := input('Type the group: ').strip().upper() ) not in groups:
        print('Invalid group! Try again');

    return group;

def get_non_empty_group(data : dict) -> str:

    groups : list = data.keys();

    while data[( group := get_group(groups) )].__len__() == 0:
        print(f'The group {group} is empty');

    return group;

def get_team(cup : dict, group : str, confirm : bool = True, message : str = 'Type the team: ') -> str:

    all_teams_registered : list = _get_all_teams_registered(cup);

    if confirm:
        while ( team := input(message) ) in all_teams_registered:
            print(f'The team {team} is already registered');
    else:
        while ( team := input(message) ) not in cup[group]:
            print(f'The team {team} isn\'t in group {group}');

    return team;

def get_two_different_teams(cup : dict, group : str, confirm : bool = True) -> tuple:
    
    while (
            ( first_team := get_team(cup, group, confirm, 'Type the first team: ') )
            ==
            ( second_team := get_team(cup, group, confirm, 'Type the second team: ') )
        ): print('The teams must be different');

    return first_team, second_team;

def get_date() -> str:

    global _YEAR;

    while True:
        try:
            game_date = date(_YEAR, get_amount('Month: '), get_amount('Day: '));
            game_time = time(get_amount('Hours: '), get_amount('Minutes: '), 0);
        except ValueError:
            print('Invalid date. Try again!');
        else:
            return str(game_date.day) + '/' + str(game_date.month) + ' at ' + str(game_time.hour) + ':' + str(game_time.minute);

def get_place() -> str:

    return input('Place: ').upper();

def number_of_teams_registered(cup : dict) -> int:

    return _number_of_data_registered(cup);

def number_of_teams_to_register(cup : dict) -> int:

    # The amount of teams that can be added is
    # 32 minus the amount of team that has
    # already been added

    return 8 * 4 - number_of_teams_registered(cup);

def number_of_games_registered(games : dict) -> int:

    return _number_of_data_registered(games);

def max_number_of_games_registered_in_the_group(cup : dict, group : str) -> int:

    # Fundamental Counting Theorem

    num_of_teams_registered_in_the_group : int = len(cup[group]);
    num_of_possible_games = num_of_teams_registered_in_the_group * (num_of_teams_registered_in_the_group - 1) / 2;

    return num_of_possible_games;

def number_of_games_to_register(cup : dict, games : dict) -> int:

    # The amount of games that can be added is the
    # max amount than can be registered minus the
    # amount that has already been registered

    return _max_number_of_games_registered(cup) - number_of_games_registered(games);

def are_all_teams_registered(cup : dict):

    # If the amount of teams registered is less than
    # tha max amount, the all teams aren't added

    for group in cup.values():

        if len(group) < 4:
            return False;

    return True;

def are_all_games_registered(cup : dict, games : dict):
    
    # If the amount of games registered is less than
    # the max amount, then all game aren't added

    for group, value in games.items():

        # To find out the max num of games that can be
        # added to a group, The Fundamental Counting
        # Theorem must be used

        max_amount_of_elements : int = max_number_of_games_registered_in_the_group(cup, group);

        if len(value) < max_amount_of_elements:
            return False;

    return True;

def is_every_registered(cup : dict, games : dict):

    # If all the teams and all the games are registered, then
    # all is registered

    return are_all_teams_registered(cup) and are_all_games_registered(cup, games);

def is_any_team_registered(cup : dict):

    return _is_any_data_registered(cup);

def is_any_game_registered(games : dict):

    return _is_any_data_registered(games);

