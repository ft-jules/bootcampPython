#!/usr/bin/env python3

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_all_recipe_names(book):
    """Affiche toutes les clies (nomds de recettes) du cookbook."""
    print("Liste des recettes disponibles :")
    if not book:
        print("Le cookbook est vide.")
        return
    for recipe_name in book.keys():
        print(f"-{recipe_name}")

def print_recipe_details(book):
    """Demande un nom et affiche les détails d'une recette."""
    name = input("Veuillez entrer le nom de la recette a afficher : ")
    if name in book:
        recipe = book[name]
        print(f"Recette pour : {name}")
        print(f"  Type de plat : {recipe['meal']}")
        print(f"  Temps de préparation : {recipe['prep_time']} minutes")
        print("  Ingrédients :")
        for ingredients in recipe['ingredients']:
            print(f"     - {ingredients}")
    else:
        print(f"Désolé, la recette '{name}' n'existe pas.")

def delete_recipe(book):
    """Demande un nom et supprime une recette du cookbook."""
    name = input("Veuillez entrer le nom de la recette à supprimer : ")
    
    if name in book:
        # 'del' est le mot-clé Python pour supprimer un élément d'un dictionnaire
        del book[name]
        print(f"Recette '{name}' supprimée avec succès !")
    else:
        print(f"Désolé, la recette '{name}' n'existe pas.")

def add_recipe(book):
    """Ajoute une nouvelle recette au cookbook via les inputs utilisateur."""
    name = input(">>> Enter a name: ")
    if not name:
        print("Le nom ne peut pas être vide.")
        return
    ingredients = []
    print(">>> Enter ingredients (tapez 'fin' ou laissez vide pour terminer):")
    while True:
        ingredient = input("- ")
        if ingredient.lower() == 'fin' or not ingredient:
            break
        ingredient.append(ingredient)
    meal = input(">>> Enter a meal type: ")

    prep_time = None
    while prep_time is None:
        time_str = input(">>> Enter a preparation time (en minutes): ")
        try:
            prep_time = int(time_str)
            if prep_time < 0:
                print("Le temps ne peut pas être négatif.")
                prep_time = None
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier pour le temps.")

    # 5. Créer et ajouter la recette
    book[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"Recette '{name}' ajoutée avec succès !")

    # ------------------------------------------------------------------
# PARTIE 3: La boucle interactive (le "main")
# ------------------------------------------------------------------

def print_main_menu():
    """Affiche le menu principal des options."""
    print("\n" + "="*30)
    print("Welcome to the Python Cookbook !")
    print("List of available options:")
    print("  1: Add a recipe")
    print("  2: Delete a recipe")
    print("  3: Print a recipe")
    print("  4: Print all recipe names") # L'énoncé dit "Print the cookbook"
    print("  5: Quit")
    print("="*30)

def main_loop():
    """Boucle principale interactive du programme."""
    
    # Boucle infinie jusqu'à ce que l'utilisateur quitte (choix 5)
    while True:
        print_main_menu()
        choice = input("Please select an option: >> ")

        if choice == '1':
            # Appelle la fonction d'ajout
            add_recipe(cookbook)
        elif choice == '2':
            # Appelle la fonction de suppression
            delete_recipe(cookbook)
        elif choice == '3':
            # Appelle la fonction d'affichage de détails
            print_recipe_details(cookbook)
        elif choice == '4':
            # Appelle la fonction d'affichage de tous les noms
            print_all_recipe_names(cookbook)
        elif choice == '5':
            # Cas de sortie : on affiche un message et on sort de la boucle
            print("\nCookbook closed. Goodbye!")
            break
        else:
            # Gère toutes les autres entrées ("Hello", "9", etc.)
            print(f"\nSorry, this option '{choice}' does not exist.")
            print("Please select an option between 1 and 5.")

# ------------------------------------------------------------------
# POINT D'ENTRÉE : Lancement du script
# C'est ce bloc qui exécute le programme quand tu lances
# $> python3 recipe.py
# ------------------------------------------------------------------
if __name__ == "__main__":
    main_loop()