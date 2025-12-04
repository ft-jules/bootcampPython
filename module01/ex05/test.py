from the_bank import Account, Bank

print("--- Création de la banque ---")
bank = Bank()

print("\n--- Création de comptes ---")
# Compte valide (Jhon)
# name(1), id(2), value(3), zip(4) -> 4 attributs (Pair) -> OK
jhon = Account("Jhon", value=1000.0, zip="75000") 

# Compte corrompu (Jane)
# name(1), id(2), value(3), zip(4), addr(5) -> 5 attributs (Impair) -> CORROMPU
# En plus, on va ajouter un attribut 'b' pour compliquer
jane = Account("Jane", value=1000.0, zip="75000", addr="Paris")
jane.bizarre = "Attribut interdit" 

bank.add(jhon)
bank.add(jane)

print(f"Jhon corrompu ? {bank.is_corrupted(jhon)}") # Doit être False
print(f"Jane corrompu ? {bank.is_corrupted(jane)}") # Doit être True

print("\n--- Tentative de virement (Jane -> Jhon) ---")
# Doit échouer car Jane est corrompu
success = bank.transfer(jane, jhon, 100)
print(f"Virement réussi ? {success}") # False
print(f"Solde Jhon : {jhon.value}")    # 1000.0 (inchangé)

print("\n--- Réparation de Jane ---")
bank.fix_account(jane)
print(f"Jane corrompu après fix ? {bank.is_corrupted(jane)}") # False

print("\n--- Nouvelle tentative de virement ---")
success = bank.transfer(jane, jhon, 100)
print(f"Virement réussi ? {success}") # True
print(f"Solde Jhon : {jhon.value}")    # 1100.0
print(f"Solde Jane : {jane.value}")    # 900.0