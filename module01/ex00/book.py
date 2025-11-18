import sys
from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        """
        Initialise le livre de recettes.
        """
        # Vérification du nom
        if not isinstance(name, str) or not name:
            print("Erreur : Le nom du livre doit être une chaîne non vide.")
            sys.exit()
        
        self.name = name
        
        # Gestion des dates
        # On capture l'instant présent pour la création et la dernière màj
        self.creation_date = datetime.now()
        self.last_update = self.creation_date

        # Structure de stockage : Un dictionnaire avec des listes vides
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        """
        Cherche une recette par son nom dans toutes les catégories,
        l'affiche et la retourne.
        """
        # On parcourt chaque liste du dictionnaire (starter, lunch, dessert)
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(str(recipe)) # On utilise le __str__ de la recette !
                    return recipe
        
        print(f"Erreur : La recette '{name}' n'existe pas dans ce livre.")
        return None

    def get_recipes_by_types(self, recipe_type):
        """
        Retourne la liste des noms des recettes d'un type donné.
        """
        if recipe_type not in self.recipes_list:
            print(f"Erreur : Le type '{recipe_type}' n'existe pas.")
            return None
        
        # On crée une liste contenant juste les noms des recettes de ce type
        # C'est une "List Comprehension" (cf. fiche rappel Module 00 !)
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """
        Ajoute une recette au livre et met à jour la date.
        """
        # 1. Vérifier que c'est bien un objet de type Recipe
        if not isinstance(recipe, Recipe):
            print(f"Erreur : L'élément ajouté n'est pas une Recette (c'est un {type(recipe)}).")
            sys.exit() # Ou return, selon la sévérité voulue

        # 2. Ajouter la recette dans la bonne liste du dictionnaire
        # L'objet recipe connaît son propre type (recipe.recipe_type)
        self.recipes_list[recipe.recipe_type].append(recipe)

        # 3. Mettre à jour la date de dernière modification
        self.last_update = datetime.now()