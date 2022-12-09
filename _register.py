"""The functions of this file are responsible
for registering the teams and the games.

"""

from _utils import (
            get_amount,
            get_group,
            get_team, get_two_different_teams,
            get_date, get_place,
            max_number_of_games_registered_in_the_group,
            number_of_teams_to_register, number_of_games_to_register,
        );

def _register_team(cup : dict) -> None:

    groups : list = cup.keys();

    while cup[( group := get_group(groups) )].__len__() > 3:
        print(f'The group {group} is already complete');

    team = get_team(cup, group);

    cup[group].append(team);

def _register_game(cup : dict, games : dict) -> None:

    groups : list = cup.keys();

    while True:

        group : str = get_group(groups);

        if games[group].__len__() == 6:
            print('All games in this group already were registered');
        elif games[group].__len__() == max_number_of_games_registered_in_the_group(cup, group):
            print('To register more games in this group, add more teams');
        else:
            break;

    found : bool = False;
    while not found:

        first_team, second_team = get_two_different_teams(cup, group, False);

        for game in games[group]:

            fir_team, sec_team = game[0], game[1];

            if not (
                (fir_team == first_team and sec_team == second_team) or
                (fir_team == second_team and sec_team == first_team)
            ): found = True; break;
        else:
            found = True;

    num_of_goals_team_one : int = get_amount(f'Number of goals for {first_team}: ');
    num_of_goals_team_two : int = get_amount(f'Number of goals for {second_team}: ');

    game = [
            first_team,
            second_team,
            num_of_goals_team_one,
            num_of_goals_team_two,
            get_date(),
            get_place(),
        ];

    games[group].append(game);

#--------------------------------------------------------#
#------------------------ public ------------------------#

def register_teams(cup : dict) -> None:
    
    max_amount : int = number_of_teams_to_register(cup);

    while ( amount_of_teams := get_amount('Number of teams: ') ) > max_amount:
        print(f'Only {max_amount} teams left to register');

    for i in range(amount_of_teams):
        _register_team(cup);

def register_games(cup : dict, games : dict) -> None:
    
    max_amount : int = number_of_games_to_register(cup, games);

    while ( amount_of_games := get_amount('Number of games: ') ) > max_amount:
        print(f'Only {max_amount} games left to register');
    
    for i in range(amount_of_games):
        _register_game(cup, games);

