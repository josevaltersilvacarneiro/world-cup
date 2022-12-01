"""This file stores useful functions.

"""

def get_amount(name : str) -> int:

    while not ( amount := input(f'Number of {name}: ') ).isdecimal():
        print(f'{amount} isn\'t a number');

    return int(amount);

def get_option(options : list) -> int:

    while (
            not ( option := input() ).isdecimal() or
                ( option := int(option) ) not in options
        ): print(f'{option} isn\'t a valid option');

    return option;

def get_group(groups : dict) -> str:

    while ( group := input('Type the group: ').strip().upper() ) not in groups:
        print('Invalid group! Try again');

    return group;

def get_team(cup : dict, group : str, confirm : bool = True) -> str:

    if confirm:
        while ( team := input('Type the team: ').title().replace('Do', 'do') ) in cup['group']:
            print(f'The team {team} already in group {group}');
    else:
        while ( team := input('Type the team: ') ) not in cup['group']:
            print(f'The team {team} isn\'t in group {group}');

    return team;

def number_of_teams_registered(cup : dict) -> int:

    num_of_teams_registered : int = 0;

    for group in cup.values():

        num_of_teams_registered += len(group);

    return num_of_teams_registered;

def number_of_games_registered(games : dict) -> int:

    num_of_games_registered : int = 0;

    for group in cup.values():

        num_of_games_registered += len(group);

    return num_of_teams_registered;