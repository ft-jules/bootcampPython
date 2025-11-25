from game import GotCharacter, Stark

print("--- DÉBUT DES TESTS EX01 ---")

# 1. Test de la classe de base GotCharacter
print("\n--- Test 1 : Personnage générique ---")
try:
    luigi = GotCharacter("Luigi")
    print(f"Personnage créé : {luigi.first_name}")
    print(f"Est en vie ? {luigi.is_alive}")
except Exception as e:
    print(f"Erreur lors de la création de GotCharacter : {e}")

# 2. Test de la classe enfant Stark
print("\n--- Test 2 : Famille Stark ---")
try:
    arya = Stark("Arya")
    print(f"Personnage créé : {arya.first_name} {arya.family_name}")
    print(f"Est en vie ? {arya.is_alive}")
    print(f"Devise : {arya.house_words}")
except Exception as e:
    print(f"Erreur lors de la création de Stark : {e}")

# 3. Test des méthodes
print("\n--- Test 3 : Méthodes ---")
print("Appel de print_house_words() :")
arya.print_house_words() # Doit afficher "Winter is Coming"

print(f"\nAvant die(), is_alive = {arya.is_alive}")
arya.die()
print(f"Après die(), is_alive = {arya.is_alive}")

# 4. Vérification de l'héritage
print("\n--- Test 4 : Vérification Héritage ---")
is_stark = isinstance(arya, Stark)
is_got = isinstance(arya, GotCharacter)
print(f"Arya est un Stark ? {is_stark}")
print(f"Arya est un GotCharacter ? {is_got}")

if is_stark and is_got and not arya.is_alive:
    print("\n✅ SUCCÈS : Tout semble fonctionner correctement !")
else:
    print("\n❌ ÉCHEC : Il y a un problème dans la logique.")