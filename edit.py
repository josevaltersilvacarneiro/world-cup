"""The functions and procedures of this file are responsible
for editing the teams and the games.

"""

from utils import (
            get_amount, get_option
            get_group, get_team, get_two_different_teams,
            is_any_team_registered, is_any_game_registered
        );

def _get_group(cup : dict) -> str:

    while cup[( group := get_group() )].__len__() == 0:
        print(f'The group {group} is empty');

    return group;

def _check(message : str) -> bool:

    check = input(f'{message}: [y/N]').strip().upper();

    return check == 'Y';

def _edit_team(cup : dict, games : dict) -> None:

    group : str = _get_group(cup);

    team : str = get_team(group, False);
    new_team : str = get_team(group);
    
    message : str = f'Do you really want to replace {team} by {new_team}';

    if _check(message):

        for game in games[group]:

            if game[0] == team:
                game[0] = new_team;
            elif game[1] == team:
                game[1] = new_team;

        index = cup[group].index(team);
        cup[group][index] = new_team;

def _edit_game(cup : dict, games : dict) -> None:

    group : str = _get_group(cup);

    first_team, second_team = get_two_different_teams(cup, group, False);

    message : str = f'Do you really want to modify the game {first_team} vs {second_team}';

    if _check(message):

        print(f'1 → The number of goals for team {first_team} is wrong');
        print(f'2 → The number of goals for team {second_team} is wrong');

        option : int = get_option([1, 2]);

        for game in games[group]:

            if option == 1 or option == 2:
                game[option + 1] = get_amount(f'goals for team {option}');

#---------------------------------------------------------------------------------#
####################################### Public ####################################

def edit_registration() -> None:

    options : list = [];

    if is_any_team_registered():
        print('1 → Edit team');
        options.append(1);
    
    if is_any_game_registered():
        print('2 → Edit game');
        options.append(2);

    option = get_option(options);

    if option == 1:
        _edit_team();
    elif option == 2:
        _edit_game();

