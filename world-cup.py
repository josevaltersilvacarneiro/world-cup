#!/bin/env python

import _utils as ut
from _file import *
import _register as rg
import _edit as ed
import _delete as dl
import _statistics as st

def _insertion_sort(classification : dict, key : str) -> None:

    for group in classification.values():
    
        length : int = len(group);

        for i in range(length):
            current = group[i];
            j = i - 1;

            while j >= 0 and group[j][key] < current[key]:
                group[j+1] = group[j];
                j-= 1;
            
            group[j+1] = current;

def _get_ranking(cup : dict, games : dict) -> dict:

    classification : dict = { group : list() for group, teams in cup.items() };

    for group, teams in cup.items():
        for team in teams:

            team_data = dict();

            team_data['name'] = team;
            team_data['pt'] = 0;  # Points
            team_data['gd'] = 0;  # Goal Difference
            team_data['gs'] = 0;  # Goals Scored
            team_data['gc'] = 0;  # Goals Conceded
            
            for game in games[group]:
                
                if game[0] == team:

                    if game[2] > game[3]:
                        team_data['pt'] += 3;
                    elif game[2] == game[3]:
                        team_data['pt'] += 1;

                    team_data['gs'] += game[2];
                    team_data['gc'] += game[3];
                    team_data['gd'] += team_data['gs'] - team_data['gc'];

                elif game[1] == team:

                    if game[3] > game[2]:
                        team_data['pt'] += 3;
                    elif game[3] == game[2]:
                        team_data['pt'] += 1;

                    team_data['gs'] += game[3];
                    team_data['gc'] += game[2];
                    team_data['gd'] += team_data['gs'] - team_data['gc'];

            classification[group].append(team_data);

    # Insertion Sort Algorithm

    _insertion_sort(classification, 'gs');
    _insertion_sort(classification, 'gd');
    _insertion_sort(classification, 'pt');

    return classification;

def get_option(games : dict, operation : str) -> int:

    options : list = [1];

    print(f'1 → {operation} team');

    if ut.is_any_game_registered(games):
        print(f'2 → {operation} game');
        options.append(2);

    return ut.get_option(options);

def register(cup : dict, games : dict) -> None:

    options : list = [1];

    print('1 → Register teams');

    if not ut.are_all_games_registered(games):
        print('2 → Register games');
        options.append(2);
    
    option = ut.get_option(options)

    rg.register_teams(cup) if option == 1 else rg.register_games(cup, games);

def edit(cup : dict, games : dict) -> None:

    option : int = get_option(games, 'Edit');

    ed.edit_team(cup, games) if option == 1 else ed.edit_game(cup, games);

def delete(cup : dict, games : dict) -> None:

    option : int = get_option(games, 'Delete');

    dl.delete_team(cup, games) if option == 1 else dl.delete_game(cup, games);

#-----------------------------------------------------------#
########################## Print ############################

def print_goal_average(games : dict) -> None:
    
    goal_average : float = st.goal_average();

    print(f'The average of goals in the first phase of the World Cup was {goal_average}');

def print_group_goal_average(games : dict) -> None:
    
    for group in games.keys():

        group_goal_average : float = st.group_goal_average(games, group);

        print(f'The average of goals in the group {group} in the first phase was {group_goal_average}');

def print_team_with_most_goals_in_the_cup(games : dict) -> None:
    
    game : list = st.most_goals_in_a_game(games);

    print(f'{game[0]} [{game[2]}] vs [{game[3]}] {game[1]}');  

def print_teams(cup : dict, games : dict) -> None:

    classification : dict = _get_ranking(cup, games);

    for group, teams in classification.items():

        print('-' * 32, '#', sep='\n', end='');
        print(group.center(30), end='');
        print('#', '-' * 32, sep='\n');
        
        print(
                '{:<20}'.format('Name'), 
                'PT',
                'GD',
                'GS',
                'GC',
                sep=' '
            );
        for team in teams:
            print(
                    '{:<20}'.format(team['name']), 
                    '{:02}'.format(team['pt']),
                    '{:2}'.format(team['gd']),
                    '{:02}'.format(team['gs']),
                    '{:02}'.format(team['gc']),
                    sep=' '
                );

    print('-' * 32);

    enter = input('Press enter to continue');

def main() -> int:

    options : list = [6];
    cup, games = get();            # Isso carrega os dados do arquivo, caso o arquivo exista

    while True:

        if not ut.is_every_registered(cup, games):

            print('1 → Register');
            options.append(1);

        if ut.is_any_team_registered(cup):

            print('2 → Edit');
            print('3 → Delete');

            options.extend([2, 3]);

        if ut.is_every_registered(cup, games):

            print('4 → Statistic');
            print('5 → Release of the next phase games');

            options.extend([4, 5]);

        print('6 → Exit');
        
        option : int = ut.get_option(options);

        print_teams(cup, games);

        if option == 1:
            register(cup, games);
        elif option == 2:
            edit(cup, games);
        elif option == 3:
            delete(cup, games);
        elif option == 4:
            pass
        elif option == 5:
            pass;
        elif option == 6:
            break;

    push(cup, games);                                  # Isso empurra os dados do programa para o arquivo

    return 0;

if __name__ == '__main__':
    exit(main());
