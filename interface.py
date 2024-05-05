def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt'else 'clear') or None
    
def show_the_battle_status(entit1, entit2):
    print('-'*30)
    print(f'{entit1.get_name()}: {entit1.health_points} HP left.')
    print(f'{entit2.get_name()}: {entit2.health_points} HP left.')
    print('-'*30)
    
def title_screen():
    print('-='*15)
    print('{: ^30}'.format("The hero's journey".upper()))
    print('-='*15)
    
    
def battle_title():
    print('-'*30)
    print('{: ^30}'.format('battle'.upper()))
    print('-'*30)


def defeated_screen():
    print('-'*30)
    print('{}'.format('YOU LOSE! :('))
    print('-'*30)
