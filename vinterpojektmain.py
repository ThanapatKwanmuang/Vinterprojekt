from vinterprojekt import Stats
import random

class Fighter(Stats):
    def __init__(self, name):
        super().__init__(60, 40, 50, 20, 30, 25)
        self.name = name

class Barbarian(Stats):
    def __init__(self, name):
        super().__init__(70, 20, 60, 10, 25, 15)
        self.name = name

class Bard(Stats):
    def __init__(self, name):
        super().__init__(30, 40, 30, 50, 40, 50)
        self.name = name

class Rogue(Stats):
    def __init__(self, name):
        super().__init__(40, 60, 30, 25, 35, 40)
        self.name = name

class Cleric(Stats):
    def __init__(self, name):
        super().__init__(30, 20, 40, 40, 50, 35)
        self.name = name

class Monk(Stats):
    def __init__(self, name):
        super().__init__(40, 60, 30, 25, 50, 30)
        self.name = name

class Paladin(Stats):
    def __init__(self, name):
        super().__init__(50, 30, 40, 20, 35, 40)
        self.name = name

class Ranger(Stats):
    def __init__(self, name):
        super().__init__(40, 50, 35, 25, 35, 25)
        self.name = name

class Druid(Stats):
    def __init__(self, name):
        super().__init__(30, 40, 30, 40, 50, 25)
        self.name = name

class Warlock(Stats):
    def __init__(self, name):
        super().__init__(20, 30, 30, 40, 30, 50)
        self.name = name

class Sorcerer(Stats):
    def __init__(self, name):
        super().__init__(20, 30, 30, 40, 30, 50)
        self.name = name

class Wizard(Stats):
    def __init__(self, name):
        super().__init__(20, 30, 30, 50, 30, 20)
        self.name = name


def create_character():
    print("Welcome to the Character Creator!")
    
    # Set default values for Human race
    race = "Human"
    
    # Get user input for character name
    name = input("Enter your character's name: ")
    
    # Choose a class (you can expand this to include other classes)
    character_class = input("Choose your class (Fighter/Rogue/Barbarian/Bard/Cleric/Monk/Paladin/Ranger/Druid/Sorcerer/Warlock/Wizard): ")
    
    # Assign default stats based on the chosen class
    class_dict = {
        'Fighter': Fighter,
        'Rogue': Rogue,
        # Add other classes here...
    }
    
    chosen_class = class_dict.get(character_class, Fighter)
    
    character = chosen_class(name)
    
    print(f"\nCharacter created successfully!\nName: {character.name}\nRace: {race}\nClass: {character_class}\nStats:")
    print(f"Strength: {character.Strength}")
    print(f"Dexterity: {character.Dexterity}")
    print(f"Constitution: {character.Constitution}")
    print(f"Intelligence: {character.Intelligence}")
    print(f"Wisdom: {character.Wisdom}")
    print(f"Charisma: {character.Charisma}")

if __name__ == "__main__":
    create_character()
