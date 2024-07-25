from character import Character

class Warrior(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Warrior", armor=10, hit_points=max_hp)
        self.max_stamina = 150
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 10
        self.strength = 15
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.current_attack_message = None
        self.current_damage = None
        self.attacks = {
            "Charge": {"method": self.charge, "stamina_cost": 10},
            "Punch": {"method": self.punch, "stamina_cost": 20},
            "Cleave Attack": {"method": self.cleave_attack, "stamina_cost": 30},
            "Shield Bash": {"method": self.shield_bash, "stamina_cost": 15},
            "Defensive Stance": {"method": self.defensive_stance, "stamina_cost": 5},
        }

    def getAttacks(self):
        attack_list = list(self.attacks.items())
        attack_sting_list = []
        for i, (attack, info) in enumerate(attack_list):
            attack_sting_list.append(str(f"{i + 1}. {attack} (Stamina cost: {info['stamina_cost']})"  ))
        return attack_sting_list

    def choose_attack(self, target, chosen_attack):      
        attack_list = list(self.attacks.items())
        
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if self.current_stamina >= attack_info["stamina_cost"]:
                self.current_stamina -= attack_info["stamina_cost"]
                attack_method = attack_info["method"]
                attack_method(target)
                return "attack complete"
            else:
                return "no stam"
        else:
            return "Invalid attack"

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)




    def attack(self, target):
        # Calculate damage based on warrior's level, strength, and any weapon modifiers
        # For simplicity, let's assume the warrior's damage is directly proportional to their level
        damage = self.strength*self.level
        target.take_damage(damage)  # Apply damage to the target
        return damage  # Return the amount of damage dealt

    def charge(self, target):
        damage = self.strength
        target.take_damage(damage)  # Example: Charge deals damage equal to the warrior's strength
        self.current_attack_message = str(f"{self.name} charges towards {target.name} for {damage} damage!")

    def punch(self, target):
        damage = self.strength + self.armor  # Example: Basic attack damage equals warrior's strength
        self.current_damage = self.strength
        target.take_damage(damage)
        self.current_attack_message = str(f"{self.name} punches {target.name} for {damage} damage!")

    def cleave_attack(self, target):
        total_damage = 0
        self.current_damage = total_damage
        damage = self.strength * 2  # Example: Cleave attack deals double the warrior's strength to each target
        total_damage += damage
        target.take_damage(damage)
        self.current_attack_message = str(f"{self.name} dealt a total of {total_damage} damage with cleave!")

    def shield_bash(self, target):
        damage = self.strength + 5  # Example: Shield bash deals warrior's strength plus 5 additional damage
        self.current_damage = self.strength + 5
        target.take_damage(damage)
        self.current_attack_message = str(f"{self.name} performs a shield bash on {target.name} for {damage} damage!")

    def defensive_stance(self, target):
        self.armor_class += 5  # Example: Defensive stance increases armor class by 5
        self.current_attack_message = str(f"{self.name} enters a defensive stance, increasing armor class!")
    
    def Get_current_damage(self):
        return self.current_damage

    def getHealth(self):
        return self.current_hp
    
    def getMaxHealth(self):
        return self.max_hp
    
    def getStamina(self):
        return self.current_stamina
    
    def getMaxStamina(self):
        return self.max_stamina
    
    def get_current_attack_message(self):
        return self.current_attack_message
    
