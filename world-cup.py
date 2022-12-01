#!/bin/env python

import _utils as ut

from _file import *
import _register as rg
import _edit as ed
import _delete as dl

groups = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
];

cup = { key : list() for key in groups };
games = { key : list() for key in groups };

def get_option(operation : str) -> int:

    options : list = [];

    if ut.is_any_team_registered():
        print(f'1 → {operation.upper()} team');
        options.append(1);
    if ut.is_any_game_registered():
        print(f'2 → {operation.upper()} game');
        options.append(2);

    return ut.get_option(options);

def register() -> None:

    option : int = get_option('register');

    rg.register_teams() if option == 1 else rg.register_games;

def edit_registration() -> None:

    option : int = get_option('edit');

    ed.edit_team() if option == 1 else ed.edit_game;

def delete_registration() -> None:

    option : int = get_option('delete');

    dl.delete_team() if option == 1 else dl.delete_game;

#------------------------------------------------------------
######################### Delete ############################

def delete_team() -> None:

    global cup, games;

    group = get_group();
    team = get_team(group, False);
    
    check = input(f'Você realmente deseja excluir o {team} do grupo {group}: [S/N]').strip().upper();

    if check == 'S':
        
        for i, game in enumerate(games[group]):

            if game[0] == team or game[1] == team:
                games.pop(i);

        cup[group].remove(team);

def delete_game() -> None:
    
    global games;

    group = get_group();
    team_one, team_two = get_team(group, False), get_team(group, False);

    check = input('Você deseja realmente excluir o jogo {} x {}: [S/N]').strip().upper();

    if check == 'S':

        for i, game in enumerate(games[group]):

            if (
                    (game[0] == team_one and game[1] == team_two) or 
                    (game[0] == team_two and game[1] == team_one)
                ):

                    games.pop(i);
                    break;

        else:
            print('O jogo que você está tentando excluir não existe');

#-----------------------------------------------------------#
############### All values were registered ##################

def goal_average_on_group(group : str) -> float:
    
    global games;

    number_of_goals : int = 0;

    for game in games[group]:

        number_of_goals += game[2] + game[3];

    return number_of_goals / len(games[group]) if number_of_goals else 0;

def goal_average() -> float:
    
    global groups;

    average_of_goals_on_groups : float = 0;

    for group in groups:

        average_of_goals_on_groups += goal_average_on_group(group);

    return average_of_goals_on_groups / len(groups);

def most_goals_in_the_cup() -> list:
    
    global games;

    data : list = [];

    for games_on_group in games.values():
        for game in games_on_group:

            max_game = max(game[2], game[3]);
            max_data = max(data[2], data[3]) if data else -1;

            if max_game > max_data:
                data = game;
    
    return data[:];

#-----------------------------------------------------------#
########################## Main #############################

def all_teams_registered() -> bool:

    for group in cup.values():

        if len(group) < 4:
            return False;

    return True;

def all_games_registered_on_group(group : str) -> bool:

    global games;

    return len(games[group]) == 6;

def all_games_registered() -> bool:

    global groups;

    for group in groups:

        if not all_games_registered_on_group(group):
            return False;

    return True;

def all_registered() -> bool:

    return all_teams_registered() and all_games_registered();

def none_registered() -> bool:

    global cup;

    for group in cup.values():

        if group:
            return False;

    return True;

#-----------------------------------------------------------#
########################## Print ############################

def print_goal_average() -> None:
    
    goal_average_on_cup = goal_average();

    print(f'A média de gols na copa é {goal_average_on_cup}');

def print_goal_average_by_group() -> None:
    
    global groups;

    for group in groups:

        goal_average = goal_average_on_group(group);

        print(f'A média de gols no grupo {group} é {goal_average:.2f}');

def print_team_with_most_goals_in_the_cup() -> None:
    
    game = most_goals_in_the_cup();

    print(f'{game[0]} [{game[2]}] vs [{game[3]}] {game[1]}');  

def update() -> None:

    global cup;

    for group, teams in cup.items():
        print('-' * 30);
        print('#', end='');
        print(group.center(28), end='');
        print('#');
        print('-' * 30);

        for team in teams:
            print(team);

    print('-' * 30);

def print_menu(all_registered : bool = False) -> None:
    
    print('1 → Cadastrar equipes em seus grupos');
    print('2 → Cadastrar jogos');
    print('3 → Editar cadastro');
    print('4 → Excluir cadastro');
    print('5 → Sair');

    if all_registered:
        print('6 → A média geral de gols na primeira fase');
        print('7 → A média de gols por jogo em cada grupo');
        print('8 → Qual seleção fez mais gols em uma partida');

def main() -> int:

    global cup, games;

    cup, games = get();            # Isso carrega os dados do arquivo, caso o arquivo exista

    while True:

        if all_registered():
            print_menu(True);
            option = get_option(range(3, 9));
        elif all_teams_registered():
            print_menu(True);
            option = get_option(range(2, 9));
        elif none_registered():
            print_menu();
            option = get_option([1, 5])
        else:
            print_menu();
            option = get_option(range(1, 6));

        if option == 1:
            register_teams();
        elif option == 2:
            register_games();
        elif option == 3:
            edit_registration();
        elif option == 4:
            delete_registration();
        elif option == 5:
            break;
        elif option == 6:
            print_goal_average();
        elif option == 7:
            print_goal_average_by_group();
        elif option == 8:
            print_team_with_most_goals_in_the_cup();

        update();

    push(cup, games);                                  # Isso empurra os dados do programa para o arquivo

    return 0;

if __name__ == '__main__':
    exit(main());
