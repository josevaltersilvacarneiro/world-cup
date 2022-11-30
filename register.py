"""The functions of this file are responsible
for registering the teams and the games.

"""

def _register_team(cup : dict) -> None:

    while cup[( group := get_group() )].__len__() > 3:
        print(f'The group {group} is already complete');

    team = get_team(group);

    cup[group].append(team);

def _register_game(games : dict) -> None:

    while cup[( group := get_group(False) )].__len__() == 6:
        print(f'All games in this group already were registered');

    while (
            ( team_one := get_team(group, False) ) == ( team_two := get_team(group, False) )
        ): print('The teams must be different');

    num_of_goals_team_one, num_of_goals_team_two = get_amount('goals for team 1'), get_amount('goals for team 2');

    game = (
            team_one,
            team_two,
            num_of_goals_team_one,
            num_of_goals_team_two,
        );

    games[group].append(game);

def _number_of_teams_to_register() -> int:
    
    return 8 * 4 - number_of_teams_registered();

def _number_of_games_to_register() -> int:
    
    return 8 * 6 - number_of_games_registered();

#--------------------------------------------------------#
####################### public ###########################

def register_teams(cup : dict) -> None:
    
    max_amount : int = _number_of_teams_to_register();

    while ( amount_of_teams := get_amount('teams') ) > max_amount:
        print(f'Only {max_amount} teams left to register');

    for i in range(amount_of_teams):
        _register_team(cup);

def register_games(games : dict) -> None:
    
    max_amount : int = _number_of_games_to_register();

    while ( amount_of_games := get_amount('games') ) > max_amount:
        print(f'Only {max_amount} games left to register');
    
    for i in range(amount_of_games):
        _register_game(games);

