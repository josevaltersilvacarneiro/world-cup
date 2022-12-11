"""The functions and procedures of this file are responsible
for editing the teams and the games.

"""

from _utils import (
            check,
            get_amount, get_option,
            get_group, get_non_empty_group,
            get_team, get_two_different_teams,
        );

def edit_team(cup : dict, games : dict) -> None:

    group : str = get_non_empty_group(cup);
    team, new_team = get_team(cup, group, False), get_team(cup, group, message='New team: ');
    
    message : str = f'Do you really want to replace {team} by {new_team}';

    if check(message):

        for game in games[group]:

            if game[0] == team:
                game[0] = new_team;
            elif game[1] == team:
                game[1] = new_team;

        index = cup[group].index(team);
        cup[group][index] = new_team;

def edit_game(cup : dict, games : dict) -> None:

    group : str = get_non_empty_group(cup);
    first_team, second_team = get_two_different_teams(cup, group, False);

    message : str = f'Do you really want to modify the game {first_team} vs {second_team}';

    if check(message):

        for game in games[group]:
        
            if  (
                    (game[0] == first_team and game[1] == second_team) or
                    (game[0] == second_team and game[1] == first_team)
                ):
                
                print(f'1 → The number of goals for team {first_team} is wrong');
                print(f'2 → The number of goals for team {second_team} is wrong');

                option : int = get_option([1, 2]);

                if option == 1 or option == 2:
                    game[option + 1] = get_amount(f'goals for team {option}');

                break;
        else:
            print('The game that you\'re trying to edit hasn\'t been registered yet');

