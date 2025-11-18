from book import Book
from recipe import Recipe
import time

print("--- DÉBUT DES TESTS ---")

# 1. Création du livre
mon_livre = Book("Le Grimoire du Code")
print(f"Livre créé : {mon_livre.name} à {mon_livre.creation_date}")

# 2. Création de recettes
tourte = Recipe("Tourte", 3, 60, ["farine", "sucre", "pommes"], "Une bonne tourte", "dessert")
salade = Recipe("Salade César", 1, 15, ["laitue", "poulet", "croutons"], "Léger et bon", "lunch")
soup = Recipe("Soupe Potiron", 2, 45, ["potiron", "eau", "sel"], "Pour l'hiver", "starter")

# 3. Ajout au livre
print("\n--- Ajout des recettes ---")
mon_livre.add_recipe(tourte)
mon_livre.add_recipe(salade)
mon_livre.add_recipe(soup)

# On attend un peu pour voir si last_update change bien
time.sleep(1.1) 
mon_livre.add_recipe(Recipe("Cookie", 1, 10, ["chocolat"], "Miam", "dessert"))

print(f"Date création : {mon_livre.creation_date}")
print(f"Dernière màj  : {mon_livre.last_update}")

# 4. Récupération par type
print("\n--- Recettes par type ---")
print("Desserts :", mon_livre.get_recipes_by_types("dessert"))
print("Entrées  :", mon_livre.get_recipes_by_types("starter"))

# 5. Récupération par nom
print("\n--- Recherche de 'Tourte' ---")
recette_trouvee = mon_livre.get_recipe_by_name("Tourte")

print("\n--- Recherche de 'Pizza' (Inexistante) ---")
mon_livre.get_recipe_by_name("Pizza")