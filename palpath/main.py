# Main Script: Run this file to start the PalPath Calculator.

import csv
import os
import difflib

class Creature:
    """A data model representing a single creature's stats and lineage."""
    def __init__(self, name, p1, p2, element, hp, atk, defense):
        self.name = name
        self.parent1 = p1 if p1 else None
        self.parent2 = p2 if p2 else None
        self.element = element
        self.hp = int(hp)      # 转换为整数，方便后续计算和排序
        self.atk = int(atk)
        self.defense = int(defense)

    def is_basic(self):
        return self.parent1 is None and self.parent2 is None

class BreedingSystem:
    def __init__(self, data_file):
        self.data_file = data_file
        self.database = {}  

    def load_data(self):
        if not os.path.exists(self.data_file):
            print(f"Error: Cannot find '{self.data_file}'")
            return False
        try:
            with open(self.data_file, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    pet = Creature(
                        name=row['Name'],
                        p1=row['Parent1'],
                        p2=row['Parent2'],
                        element=row['Element'],
                        hp=row['HP'],
                        atk=row['ATK'],
                        defense=row['DEF']
                    )
                    self.database[pet.name] = pet
            return True
        except Exception as e:
            print(f"Database loading error: {e}")
            return False

    def print_lineage_tree(self, creature_name, depth=0):
        indent = "  " * depth 
        pet = self.database.get(creature_name)
        
        if not pet:
            return

        if pet.is_basic():
            print(f"{indent}-> {pet.name} [Catch in Wild]")
            return
        
        print(f"{indent}-> {pet.name} requires: {pet.parent1} + {pet.parent2}")
        self.print_lineage_tree(pet.parent1, depth + 1)
        self.print_lineage_tree(pet.parent2, depth + 1)

    def get_unique_base_requirements(self, creature_name, unique_set):
        pet = self.database.get(creature_name)
        if not pet:
            return
            
        if pet.is_basic():
            unique_set.add(pet.name)  
            return
            
        self.get_unique_base_requirements(pet.parent1, unique_set)
        self.get_unique_base_requirements(pet.parent2, unique_set)

    def search_by_element(self, element):
        """Filters creatures by element."""
        results = [pet for pet in self.database.values() if pet.element.lower() == element.lower()]
        return results

    def get_top_creatures(self, stat_type, top_n=3):
        """Sorts creatures by a specific stat in descending order."""
        all_pets = list(self.database.values())
        if stat_type == 'ATK':
            all_pets.sort(key=lambda x: x.atk, reverse=True)
        elif stat_type == 'DEF':
            all_pets.sort(key=lambda x: x.defense, reverse=True)
        elif stat_type == 'HP':
            all_pets.sort(key=lambda x: x.hp, reverse=True)
        return all_pets[:top_n]


def main():
    print("="*55)
    print("Welcome to PalPath: The Smart Breeding Calculator")
    print("="*55)
    
    system = BreedingSystem("breeding_recipes.csv")
    if not system.load_data():
        return 

    while True:
        print("\n[Main Menu]")
        print("1. View Full Creature Database")
        print("2. Calculate Breeding Path & Requirements")
        print("3. Advanced Database Search (Filter & Rank)")
        print("4. Quit")
        
        choice = input("\nSelect an option (1/2/3/4): ").strip()
        
        if choice == '1':
            print(f"\n{'-'*55}")
            print(f"{'NAME':<15} | {'ELEMENT':<10} | {'HP':<5} | {'ATK':<5} | {'DEF':<5}")
            print(f"{'-'*55}")
            for name, pet in system.database.items():
                print(f"{name:<15} | {pet.element:<10} | {pet.hp:<5} | {pet.atk:<5} | {pet.defense:<5}")
            print(f"{'-'*55}")
                
        elif choice == '2':
            user_input = input("\nEnter the target creature (e.g., AstralKing): ").strip()
            if not user_input:
                continue

            valid_targets = list(system.database.keys())
            target_pet = None
            
            for t in valid_targets:
                if t.lower() == user_input.lower():
                    target_pet = t
                    break
            
            if not target_pet:
                matches = difflib.get_close_matches(user_input, valid_targets, n=1, cutoff=0.5)
                if matches:
                    target_pet = matches[0]
                    print(f"\n[*] Did you mean '{target_pet}'? Auto-correcting...")
                else:
                    print(f"[-] '{user_input}' not found in database.")
                    continue

            pet_obj = system.database[target_pet]
            print(f"\n--- Combat Stats for [{target_pet}] ---")
            print(f"Type: {pet_obj.element} | HP: {pet_obj.hp} | ATK: {pet_obj.atk} | DEF: {pet_obj.defense}")
            
            print(f"\n--- Breeding Lineage Tree ---")
            system.print_lineage_tree(target_pet)
            
            print("\n--- Unique Base Species Required ---")
            unique_bases = set()
            system.get_unique_base_requirements(target_pet, unique_bases)
            
            print(f"To breed a {target_pet}, you must catch at least one of each:")
            print(", ".join(unique_bases))
            print("-" * 37)
            
        elif choice == '3':
            print("\n--- Advanced Search ---")
            print("A. Search by Element (e.g., Fire, Ice, Dark)")
            print("B. Top 3 Attackers")
            print("C. Top 3 Defenders")
            sub_choice = input("Select query (A/B/C): ").strip().upper()
            
            if sub_choice == 'A':
                elem = input("Enter Element: ").strip()
                results = system.search_by_element(elem)
                if results:
                    print(f"\nFound {len(results)} '{elem}' creatures:")
                    for p in results:
                        print(f" - {p.name} (ATK: {p.atk}, DEF: {p.defense})")
                else:
                    print(f"\nNo creatures found with element '{elem}'.")
                    
            elif sub_choice == 'B':
                print("\n--- Top 3 Highest ATK ---")
                top_atk = system.get_top_creatures('ATK', 3)
                for i, p in enumerate(top_atk, 1):
                    print(f"{i}. {p.name:<15} - ATK: {p.atk}")
                    
            elif sub_choice == 'C':
                print("\n--- Top 3 Highest DEF ---")
                top_def = system.get_top_creatures('DEF', 3)
                for i, p in enumerate(top_def, 1):
                    print(f"{i}. {p.name:<15} - DEF: {p.defense}")
            else:
                print("Invalid search option.")
                
        elif choice == '4':
            print("\nSystem offline. Good luck out there!")
            break
            
        else:
            print("[-] Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
