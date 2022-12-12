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
    team  : str = get_team(cup, group, False);

    message : str = f'Do you really want to delete {team} from the group {group}';

    if check(message):

        # Chain Deletion                    #
        # The foreing key must be deleted   #
        # before the primary key            #

        for i, game in enumerate(games[group]):

            if game[0] == team or game[1] == team:
                games[group].pop(i);

        cup[group].remove(team);

def delete_game(cup : dict, games : dict) -> None:
    """This procedure allows that the user to delete
    any match.

    """

    group : str = get_non_empty_group(cup);
    first_team, second_team = get_two_different_teams(cup, group, False);

    # Using a repetition loop, all the games looped. If find #
    # the game typed by the user, ask the user if he wants   #
    # to delete it. If yes, delete it and break; else break. #
    # If when scanning all games, none are found, run the    #
    # last statement, which shows the user that the game     #
    # hasn't been registered yet.                            #

    for i, game in enumerate(games[group]):
            
        if  (
                (game[0] == first_team and game[1] == second_team) or
                (game[0] == second_team and game[1] == first_team)
            ):

            message : str = f'Do you really to delete the game {first_team} vs {second_team}';

            if check(message):
                games[group].pop(i);

            break;

    else:
        print('The game that you\'re trying to delete has not been registered yet');

