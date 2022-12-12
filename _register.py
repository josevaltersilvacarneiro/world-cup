"""The functions of this file are responsible
for registering the teams and the games.

"""

from _utils import (
            get_amount,
            get_group, get_non_empty_group,
            get_team, get_two_different_teams,
            get_date, get_place,
            max_number_of_games_registered_in_the_group,
            number_of_teams_to_register, number_of_games_to_register,
        );

def _register_team(cup : dict) -> None:

    groups : list = cup.keys();

    # Run until find an incomplete group    #

    while cup[( group := get_group(groups) )].__len__() > 3:
        print(f'The group {group} is already complete');

    # Get a team that hasn't yet been added #

    team = get_team(cup, group);

    # Add this team to the group typed by   #
    # the user                              #

    cup[group].append(team);

def _register_game(cup : dict, games : dict) -> None:

    while True:

        group : str = get_non_empty_group(cup);

        # Why is it necessary?               #
        # Send me an email and I'll answer.  #

        if games[group].__len__() == 6:
            print('All games in this group already were registered');
        elif games[group].__len__() == max_number_of_games_registered_in_the_group(cup, group):
            print('To register more games in this group, add more teams');
        else:
            break;

    found : bool = False;
    while not found:

        first_team, second_team = get_two_different_teams(cup, group, False);

        # Using a repetition loop, all the games looped. If #
        # find the game typed by the user, exit the loop    #
        # without executing the last statement; else conti- #
        # nue until run the last statement, which makes the #
        # 'found' flag true.                                #

        for game in games[group]:

            fir_team, sec_team = game[0], game[1];

            if (
                    (fir_team == first_team and sec_team == second_team) or
                    (fir_team == second_team and sec_team == first_team)
               ): break;
        else:
            found = True;

    num_of_goals_team_one : int = get_amount(f'Number of goals for {first_team}: ');
    num_of_goals_team_two : int = get_amount(f'Number of goals for {second_team}: ');

    # match attributes

    game = [
            first_team,             # first team name                    #
            second_team,            # second team name
            num_of_goals_team_one,  # number of goals for the first team #
            num_of_goals_team_two,  # number of ...          second team #
            get_date(),             # date and time of the match         #
            get_place(),            # stadium where the match was played #
        ];

    # Add the item - match - to the corresponding group

    games[group].append(game);

#------------------------------------------------------------------------#
#-------------------------------- public --------------------------------#

def register_teams(cup : dict) -> None:
    
    max_amount : int = number_of_teams_to_register(cup);

    # As long as amount of teams typed by the user is higher #
    # than the max missing quantity, run; else break         #

    while ( amount_of_teams := get_amount('Number of teams: ') ) > max_amount:
        print(f'Only {max_amount} teams left to register');

    # Register how many teams the user typed #

    for i in range(amount_of_teams):
        _register_team(cup);

def register_games(cup : dict, games : dict) -> None:
    
    max_amount : int = number_of_games_to_register(cup, games);

    # As long as amount of games typed by the user is higher #
    # than the max missing quantity, run; else break         #

    while ( amount_of_games := get_amount('Number of games: ') ) > max_amount:
        print(f'Only {max_amount} games left to register');
    
    # Register how many games the user typed #

    for i in range(amount_of_games):
        _register_game(cup, games);

