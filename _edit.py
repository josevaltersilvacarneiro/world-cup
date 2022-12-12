"""The functions and procedures of this file are responsible
for editing the teams and the games.

"""

from _utils import (
            check,
            get_amount, get_option,
            get_group, get_non_empty_group,
            get_team, get_two_different_teams,
            get_date, get_place,
        );

def edit_team(cup : dict, games : dict) -> None:
    """This function replaces a team registered in the group
    by an unregistered team.

    """

    group    : str = get_non_empty_group(cup);

    team     : str = get_team(cup, group, False, 'Type the team you want to edit: ');
    new_team : str = get_team(cup, group, message='New team: ');
    
    message  : str = f'Do you really want to replace {team} by {new_team}';

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

    for game in games[group]:
        
        if  (
                (game[0] == first_team and game[1] == second_team) or
                (game[0] == second_team and game[1] == first_team)
            ):
                
            message : str = f'Do you really want to modify the game {first_team} vs {second_team}';

            if check(message):

                print(f'1 → The number of goals for team {first_team} is wrong');
                print(f'2 → The number of goals for team {second_team} is wrong');
                print ('3 → The time is wrong' );
                print ('4 → The place is wrong');

                option : int = get_option(
                        [
                            1,
                            2,
                            3,
                            4,
                        ]
                    );

                if option == 1:
                    
                    number_of_goals : int = get_amount(f'Number of goals for {first_team}: ');

                    if game[0] == first_team:
                        game[2] = number_of_goals;
                    else:
                        game[3] = number_of_goals;

                elif option == 2:
                    
                    number_of_goals : int = get_amount(f'Number of goals for {second_team}: ');

                    if game[1] == second_team:
                        game[3] = number_of_goals;
                    else:
                        game[2] = number_of_goals;

                elif option == 3:
                    game[4] = get_date();
                elif option == 4:
                    game[5] = get_place();

            break;
    else:
        print('The game that you\'re trying to edit hasn\'t been registered yet');

