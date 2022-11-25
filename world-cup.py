#!/bin/env python

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
######################### File ##############################

def push():
    pass

def get():
    pass

#------------------------------------------------------------
########################## Functions ########################

def get_amount(name : str = 'equipes') -> int:

    while not ( amount := input(f'Quantidade de {name}: ') ).isdecimal(): pass

    return int(amount);

def get_option(begin, end) -> int:
    
    while (
            not ( option := input('Escolha uma opção do menu: ') ).isdecimal() or 
            not begin <= ( option := int(option) ) <= end
        ): pass

    return option;

def get_group() -> str:

    global groups;

    while ( group := input(f'Digite o grupo: ').upper() ) not in groups: pass

    return group;

def get_team(group : str, confirm : bool = True) -> str:

    global cup;

    if confirm:
        while ( team := input(f'Nome da seleção: ').title() ) in cup[group]: pass
    else:
        while ( team := input(f'Nome da seleção: ').title() ) not in cup[group]: pass

    return team

#------------------------------------------------------------
######################## Register ###########################

def register_teams() -> None:

    global cup;
    
    amount_of_teams = get_amount();

    for i in range(amount_of_teams):
        
        group = get_group();
        team = get_team(group);

        cup[group].append(team);

def register_game() -> None:

    global games;

    group = get_group();
    
    team_one = get_team(group, False);
    team_two = get_team(group, False);

    amount_of_goals_team_one = get_amount('gols da equipe 1');
    amount_of_goals_team_two = get_amount('gols da equipe 2');

    game = [team_one, team_two, amount_of_goals_team_one, amount_of_goals_team_two];

    games[group].append(game);

def register_games() -> None:
    
    amount_of_games = get_amount('jogos');

    for i in range(amount_of_games):

        register_game();

#------------------------------------------------------------
####################### Edit Registration ###################

def edit_team() -> None:
   
    global cup, games;

    group = get_group();

    team = get_team(group);
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
    team = get_team(group);
    
    check = input(f'Você realmente deseja excluir o {team} do grupo {group}: [S/N]').strip().upper();

    if check == 'S':
        
        for i, game in enumerate(games):

            if game[0] == team or game[1] == team:
                games.pop(i);

        cup[group].remove(team);

def delete_game() -> None:
    
    global games;

    group = get_group();
    team_one, team_two = get_team(group), get_team(group);

    check = input('Você deseja realmente excluir o jogo {} x {}: [S/N]').strip().upper();

    if check == 'S':

        for i, game in enumerate(games):

            if (
                    (game[0] == team_one and game[1] == team_two) or 
                    (game[0] == team_two and game[1] == team_one)
                ):

                    games.pop(i);
                    break;

def delete_registration() -> None:
    
    print('1 → Deletar equipe');
    print('2 → Deletar jogo');
    option = get_option(1, 2);

    if option == 1:
        delete_team();
    elif option == 2:
        delete_game();

#------------------------------------------------------------
########################## Main #############################

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

def print_menu() -> None:
    
    print('1 → Cadastrar equipes em seus grupos');
    print('2 → Cadastrar jogos');
    print('3 → Editar cadastro');
    print('4 → Excluir cadastro');
    print('5 → Sair');

def main() -> int:

    while True:
        print_menu();
        option = get_option(1, 5);

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

        update();

    return 0;

if __name__ == '__main__':
    exit(main());
