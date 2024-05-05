# Hero system.
class Hero():
    
    def __init__(self, name:str, health_points:int, attack_damage:float):
        self.__name = name
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None
        self.enemies_defeateds = 0
        self.victory = True
        
    def equipWeapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            
    def get_name(self):
        return self.__name       
            
    def talk(self):
        print("I'm ready to fight, your monster! >:)")

    def attack(self):
        print(f'The Hero attack for {self.attack_damage} damage.')

class Weapon():
    
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase
    
# Enemies systems.
class Enemy():
    
    def __init__(self, name:str, health_points:int=10, attack_damage:float=1):
        self.__name = name
        self.health_points = health_points
        self.attack_damage = attack_damage
        
    def get_name(self): # Getter
        return self.__name
    
    def talk(self):
        print(f'I am a {self.__name}! Be prepared to fight.')
        
    def walk_foward(self):
        print(f'{self.__name.title()} moves closer to you.')
        
    def attack(self):
        print(f'{self.__name.title()} attacks for {self.attack_damage} damage.')
        
    def use_special_attack(self):
        print('Enemy has no a special attack.')
    
 
class Zombie(Enemy):
    
    def __init__(self, health_points:int, attack_damage:float):
        super().__init__(name='Zombie', health_points=health_points,
                       attack_damage=attack_damage)
        
    def talk(self):
        print('*Grumbling...*')
        
    def spread_disease(self):
        print('The zombie is trying to spread infection.')
        
    def use_special_attack(self):
        from random import random
        did_special_attack_work = random() < 0.10
        if did_special_attack_work:
            self.health_points += 2
            print('Zombie regenerated 2 HP!')
        

class Ogre(Enemy):
    
    def __init__(self, health_points:int, attack_damage:float):
        super().__init__(name='Ogre', health_points=health_points, 
                       attack_damage=attack_damage)
        
    def talk(self):
        print('Ogre is slamming hands all around.')
        
    def use_special_attack(self):
        from random import random
        did_special_attack_work = random() < 0.5
        if did_special_attack_work:
            self.attack_damage += 0.5
            print('Ogre attack was increased by 0.5!')
        