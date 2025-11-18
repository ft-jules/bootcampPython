import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        
        # --- Vérification du NOM (doit être une chaîne non vide) ---
        if not isinstance(name, str) or not name:
            print("Erreur : Le nom doit être une chaîne de caractères.")
            sys.exit()
        self.name = name

        # --- Vérification du NIVEAU (entier entre 1 et 5) ---
        if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
            print("Erreur : Le niveau de cuisson doit être un entier entre 1 et 5.")
            sys.exit()
        self.cooking_lvl = cooking_lvl

        # --- Vérification du TEMPS (entier positif) ---
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("Erreur : Le temps de cuisson doit être un nombre positif.")
            sys.exit()
        self.cooking_time = cooking_time

        # --- Vérification des INGRÉDIENTS (liste de chaînes) ---
        # On vérifie d'abord si c'est une liste
        if not isinstance(ingredients, list):
            print("Erreur : Les ingrédients doivent être une liste.")
            sys.exit()
        
        # Ensuite, on vérifie que CHAQUE élément de la liste est une chaîne
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                print("Erreur : Chaque ingrédient doit être une chaîne de caractères.")
                sys.exit()
        self.ingredients = ingredients

        # --- Vérification de la DESCRIPTION (chaîne) ---
        if not isinstance(description, str):
            print("Erreur : La description doit être une chaîne de caractères.")
            sys.exit()
        self.description = description

        # --- Vérification du TYPE (starter, lunch ou dessert) ---
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("Erreur : Le type doit être 'starter', 'lunch' ou 'dessert'.")
            sys.exit()
        self.recipe_type = recipe_type

    def __str__(self):
        """
        Retourne une présentation textuelle de la recette.
        """
        # On construit le texte ligne par ligne pour que ce soit propre
        txt = f"Recette : {self.name}\n"
        txt += f"Niveau  : {self.cooking_lvl}/5\n"
        txt += f"Temps   : {self.cooking_time} min\n"
        txt += f"Type    : {self.recipe_type}\n"
        txt += f"Ingrédients : {', '.join(self.ingredients)}\n"
        txt += f"Description : {self.description}"
        return txt