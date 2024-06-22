from characters import Hero, Weapon

def register_or_load_player():
    from time import sleep
    import json
    from characters import Hero
    
    try:
        a = open('data.json', 'r')
        contents = a.read()
        user_data = json.loads(contents)
        print('Loading data...')
        sleep(1.75)
        hero = Hero(user_data['name'], user_data['health_points'],
                    user_data['attack_damage'])
        weapon = Weapon(user_data['weapon_type'], user_data['weapon_attack_increase'])
        hero.weapon = weapon
        hero.equipWeapon()
        hero.enemies_defeateds = user_data['enemies_defeateds']
        return hero
        
    except: 
        a = open('data.json', 'wt+')
        user_data = {}
        print('RULES TO THE NAME:')
        print('1. Insert only 1 name.')
        print("2. Don't use signals or numbers.")
        print('-'*30)
        user_data['name'] = get_answer('name of the hero: ')
        user_data['health_points'] =  15
        user_data['attack_damage'] = 4
        user_data['weapon'] = None
        user_data['enemies_defeateds'] = 0
        contents = json.dumps(user_data)
        a.write(contents)
        print(f"Welcome to the Hero's Journey, {user_data['name']}!")
        a.close()
        sleep(2)
        return Hero(user_data['name'], user_data['health_points'],
                    user_data['attack_damage'])
    
    
def update_hero_data(hero: Hero):
    from json import loads, dumps
    a = open('data.json', 'r')
    contents = a.read()
    user_data = loads(contents)
    a = open('data.json', 'wt+')
    user_data['health_points'] = hero.health_points
    user_data['attack_damage'] = hero.attack_damage
    user_data['weapon_type'] = hero.weapon.weapon_type
    user_data['weapon_attack_increase'] = hero.weapon.attack_increase
    user_data['enemies_defeateds'] = hero.enemies_defeateds
    a.write(dumps(user_data))
    
    
def get_answer(content):
    from interface import clear_terminal
    answer = str(input(content))
    choice = 0
    while True:
        if answer == '' or choice == 'n':
            print('\033[31mERROR! TRY AGAIN, PLEASE!\033[m' if choice != 'n' else '')
            answer = str(input(content))
            choice = 'y'
            clear_terminal()
        else:
            while True:
                choice = input(f'{answer.title()}. Are you sure? [y/n] ').lower().strip()[0]
                if choice == 'y':
                    return answer
                elif choice == 'n':
                    break
                else:
                    print('\033[31mERROR! Answer only "y" or "n"!')
                    

def erase_user_data():
    a = open('data.json', 'wt+')
    a.write('')
        
