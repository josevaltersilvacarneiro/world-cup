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

    check = input(f'{message}: [y/N]').strip().upper();

    return check == 'Y';

def get_amount(message : str) -> int:

    while not ( amount := input(message) ).isdecimal():
        print(f'{amount} isn\'t a number');

    return int(amount);

def get_option(options : list) -> int:

    while (
            ( option := get_amount('Type your option: ') ) not in options
        ): print(f'{option} isn\'t a valid option');

    return option;

def get_group(groups : dict) -> str:

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

def get_date() -> tuple:

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

    return input('Place: ');

def number_of_teams_registered(cup : dict) -> int:

    num_of_teams_registered : int = 0;

    for group in cup.values():

        num_of_teams_registered += len(group);

    return num_of_teams_registered;

def number_of_teams_to_register(cup : dict) -> int:

    return 8 * 4 - number_of_teams_registered(cup);

def number_of_games_registered(games : dict) -> int:

    num_of_games_registered : int = 0;

    for group in games.values():

        num_of_games_registered += len(group);

    return num_of_games_registered;

def max_number_of_games_registered_in_the_group(cup : dict, group : str) -> int:

    # Fundamental Counting Theorem

    num_of_teams_registered_in_the_group : int = len(cup[group]);
    num_of_possible_games = num_of_teams_registered_in_the_group * (num_of_teams_registered_in_the_group - 1) / 2;

    return num_of_possible_games;

def number_of_games_to_register(cup : dict, games : dict) -> int:

    return _max_number_of_games_registered(cup) - number_of_games_registered(games);

def are_all_teams_registered(cup : dict):

    for group in cup.values():

        if len(group) < 4:
            return False;

    return True;

def are_all_games_registered(cup : dict, games : dict):

    for group, value in games.items():

        max_amount_of_elements : int = max_number_of_games_registered_in_the_group(cup, group);

        if len(value) < max_amount_of_elements:
            return False;

    return True;

def is_every_registered(cup : dict, games : dict):

    return are_all_teams_registered(cup) and are_all_games_registered(cup, games);

def is_any_team_registered(cup : dict):

    return _is_any_data_registered(cup);

def is_any_game_registered(games : dict):

    return _is_any_data_registered(games);

