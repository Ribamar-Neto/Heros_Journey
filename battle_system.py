from characters import *
from interface import *
from user_interactions import *
from random import random, randint, choice
from time import sleep
from typing import Union

def battle(entity1: Enemy | Hero, enemy: Enemy):
    battle_title()
    entity1.talk()
    enemy.talk()
    sleep(2)
    first_health_points = entity1.health_points
    try:
        while entity1.health_points > 0 and enemy.health_points > 0:
            show_the_battle_status(entity1, enemy)
            sleep(1)
            if type(entity1) == Enemy:
                entity1.use_special_attack()
            enemy.use_special_attack()
            sleep(1)
            entity1.attack()
            enemy.health_points -= entity1.attack_damage
            enemy.attack()
            entity1.health_points -= enemy.attack_damage
            sleep(1.5)
        print('-'*20)
        if entity1.health_points > 0 and enemy.health_points <= 0:
            print(f'{entity1.get_name()} wins!', end=' ')
            print(';)' if type(entity1) == Hero else '')
            entity1.victory = True
            restore_health(entity1, first_health_points)
            item = items_drops()
            if item == 'miojo':
                entity1.health_points += 3
                print(f'The {enemy.get_name()} drops the Miojo.')
                print('Increases + 3HP')
                print(f'Actual health: {entity1.health_points}')
            elif item == 'weapon':
                weapons_types = ['sword', 'wandle', 'katana', 'gun']
                weapon_type = choice(weapons_types)
                attack_increase = randint(entity1.attack_damage-3, entity1.attack_damage+6)
                weapon = Weapon(weapon_type, attack_increase)
                print(f'A {weapon_type} with {attack_increase} has been dropped.')
                print('-'*30)
                print(f'Actual weapon: {entity1.weapon}', end='')
                print(f', with {weapon.attack_increase}' if entity1.weapon!=None else '')
                print('-'*30)
                answer = get_answer('Do you want to equip it? [y/n]')
                print('-'*30)
                if answer == 'y':
                    switch_weapon(entity1, weapon)
                else:
                    print('No weapons switch for today. "-*')
            elif item == None:
                print('No drops for this battle. ;-;')
        else:
            entity1.victory = False
            print(f'{enemy.get_name()} wins!', end=' ')
            print(':(' if type(entity1) == Hero else '')
    except KeyboardInterrupt:
        print('Thank you for your time using my game! :)')
        
        
def items_drops():
    number = randint(1, 2)
    return 'weapon' if number == 1 else 'miojo'
    

def switch_weapon(hero: Hero, new_weapon: Weapon):
    if hero.weapon != None:
        hero.attack_damage -= hero.weapon.attack_increase
    hero.weapon = new_weapon
    hero.is_weapon_equipped = False
    hero.equipWeapon()


def generate_enemy(hero: Hero):
    from random import randint, choice
    enemy_types = ['zombie', 'ogre']
    enemy_type = choice(enemy_types)
    enemy_attack = randint(hero.attack_damage-3, hero.attack_damage-1)
    enemy_health_points = randint(hero.health_points-4, hero.health_points+1)
    match enemy_type:
        case 'zombie':
            return Zombie(enemy_health_points, enemy_attack)
        case 'ogre':
            return Ogre(enemy_health_points, enemy_attack)


def restore_health(hero: Hero, first_health):
    hero.health_points = first_health
