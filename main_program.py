from interface import *
from characters import *
from user_interactions import *
from battle_system import *
from time import sleep

title_screen()
sleep(2)
clear_terminal()

hero = register_or_load_player()
clear_terminal()
while True:
    enemy = generate_enemy(hero)
    if not hero.victory:
        defeated_screen()
        print(f'Enemies defeated: {hero.enemies_defeateds}')
        break
    battle(hero, enemy)
    update_hero_data(hero)
    sleep(2.5)
    clear_terminal()
erase_user_data()
print('Thank you for your time using my game! :)')
