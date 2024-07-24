from character import Character
import pygame
import random

class Mage(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Mage", armor=10, hit_points=max_hp)
        self.max_stamina = 10000000000
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 10
        self.strength = 15
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.current_damage = None
        self.attacks = {
            "Freeze": {"method": self.freeze, "stamina_cost": 10},
            "Brarade": {"method": self.brarade, "stamina_cost": 20},
            "Shock": {"method": self.shock, "stamina_cost": 30},
            "Fusion Grenade": {"method": self.fusion_grenade, "stamina_cost": 15},
            "Whimsical Posture": {"method": self.whimsical_posture, "stamina_cost": 5},
        }

    def choose_attack(self, target, chosen_attack):      
        attack_list = list(self.attacks.items())

        for i, (attack, info) in enumerate(attack_list):
            print(f"{i + 1}. {attack} (Stamina cost: {info['stamina_cost']})")
        
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if self.current_stamina >= attack_info["stamina_cost"]:
                self.current_stamina -= attack_info["stamina_cost"]
                attack_method = attack_info["method"]
                attack_method(target)
            else:
                print("Not enough stamina for this attack.")
        else:
            print("Invalid attack.")

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)




    def attack(self, target):
        # Calculate damage based on warrior's level, strength, and any weapon modifiers
        # For simplicity, let's assume the warrior's damage is directly proportional to their level
        damage = self.strength*self.level
        target.take_damage(damage)  # Apply damage to the target
        return int(damage)  # Return the amount of damage dealt

    def freeze(self, target):
        print(f"{self.name} Freezes {target.name}!")
        self.current_damage = self.strength
        target.take_damage(self.strength)  # Example: Charge deals damage equal to the warrior's strength
        print("freeze")
        

    def brarade(self, target):
        damage = self.strength  # Example: Basic attack damage equals warrior's strength
        self.current_damage = self.strength
        print(f"{self.name} Bararades {target.name} for {damage} damage!")
        target.take_damage(damage)

    def shock(self, targets):
        total_damage = 0
        self.current_damage = 0
        for target in targets:
            damage = self.strength * 2  # Example: Cleave attack deals double the warrior's strength to each target
            total_damage += damage
            self.current_damage += damage
            print(f"{self.name} Shocks {target.name} for {damage} damage!")
            target.take_damage(damage)
        print(f"{self.name} dealt a total of {total_damage} damage with Shock!")
        return int(damage)

    def fusion_grenade(self, target):
        damage = self.strength + 5
        self.current_damage += self.strength + 5  # Example: Shield bash deals warrior's strength plus 5 additional damage
        print(f"{self.name} Throws a Fusion Grenade on {target.name} for {damage} damage!")
        target.take_damage(damage)
        return int(damage)

    def whimsical_posture(self):
        self.armor_class += 5  # Example: Defensive stance increases armor class by 5
        print(f"{self.name} takes up a Whimsical Posture increasing their armor!")

    def Get_current_damage(self):
        return self.current_damage