"""This file stores useful functions.

"""

def _are_all_data_registered(data : dict, max_amount_of_elements : int):

    for element in data.values():

        if len(element) < max_amount_of_elements:
            return False;

    return True;

def _is_any_data_registered(data : dict):

    for element in data.values():

        if len(element) > 0:
            return True;

    return False;

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

def get_team(cup : dict, group : str, confirm : bool = True, message : str = 'Type the team') -> str:

    if confirm:
        while ( team := input(message).title() ) in cup[group]:
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

def number_of_teams_registered(cup : dict) -> int:

    num_of_teams_registered : int = 0;

    for group in cup.values():

        num_of_teams_registered += len(group);

    return num_of_teams_registered;

def number_of_games_registered(games : dict) -> int:

    num_of_games_registered : int = 0;

    for group in games.values():

        num_of_games_registered += len(group);

    return num_of_games_registered;

def are_all_teams_registered(cup : dict):

    return _are_all_data_registered(cup, 4);

def are_all_games_registered(games : dict):

    return _are_all_data_registered(games, 6);

def is_every_registered(cup : dict, games : dict):

    return are_all_teams_registered(cup) and are_all_games_registered(games);

def is_any_team_registered(cup : dict):

    return _is_any_data_registered(cup);

def is_any_game_registered(games : dict):

    return _is_any_data_registered(games);

