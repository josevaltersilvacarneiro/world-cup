#!/bin/env python

from file import *
from register import *

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

#------------------------------------------------------------
####################### Edit Registration ###################

def edit_team() -> None:
   
    global cup, games;

    group = get_group();

    team = get_team(group, False);
    new_team = get_team(group);

    check = input(f'Você deseja substituir {team} por {new_team}: [S/N]').strip().upper();

    if check == 'S':
        
        for game in games[group]:

            if game[0] == team:
                game[0] = new_team
            elif game[1] == team:
                game[1] = new_team

        cup[group].remove(team)
        cup[group].append(new_team)

def edit_game() -> None:
    
    global games;

    group = get_group();
    team_one, team_two = get_team(group), get_team(group);

    for game in games[group]:

        if (game[0] == team_one and game[1] == team_two) or (game[0] == team_two and game[1] == team_one):
            
            print(f'1 → O nome {team_one} está errado');
            print(f'2 → O nome {team_two} está errado');
            print(f'3 → A quantidade de gols de {team_one} está errada');
            print(f'4 → A quantidade de gols de {team_two} está errada');

            option = get_option(1, 4);

            if option == 1:
                game[0] = get_team(group);
            elif option == 2:
                game[1] = get_team(group);
            elif option == 3:
                game[2] = get_amount('gols da equipe 1');
            elif option == 4:
                game[3] = get_amount('gols da equipe 2');

def edit_registration() -> None:
    
    print('1 → Editar equipe');
    print('2 → Editar jogo');
    option = get_option(1, 2);

    if option == 1:
        edit_team();
    else:
        edit_game();

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

def delete_registration() -> None:
    
    print('1 → Deletar equipe');
    print('2 → Deletar jogo');

    option = get_option([1, 2]);

    if option == 1:
        delete_team();
    elif option == 2:
        delete_game();

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
