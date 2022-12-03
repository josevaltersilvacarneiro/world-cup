"""The functions and procedures of this file are responsible
for deleting the teams and the games.

"""

from _utils import (
            check,
            get_non_empty_group,
            get_team, get_two_different_teams
        );

def delete_team(cup : dict, games : dict) -> None:

    group : str = get_non_empty_group(cup);
    team : str = get_team(cup, group, False);

    message : str = f'Do you really want to delete {team} from the group {group}';

    if check(message):

        for i, game in enumerate(games[group]):

            if game[0] == team or game[1] == team:
                games[group].pop(i);

        cup[group].remove(team);

def delete_game(cup : dict, games : dict) -> None:

    group : str = get_non_empty_group(cup);
    first_team, second_team = get_two_different_teams(cup, group, False);

    message : str = f'Do you really to delete the game {first_team} vs {second_team}';

    if check(message):

        for i, game in enumerate(games[group]):
            
            if (
                (game[0] == first_team and game[1] == second_team) or
                (game[0] == second_team and game[1] == first_team)
                    ):
            
                games[group].pop(i);

                break;
        else:
            print('The game that you\'re trying to delete has not been registered yet');

