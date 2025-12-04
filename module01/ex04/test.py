from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print("--- Test ZIP ---")
# Calcul attendu :
# (1.0 * 2) + (2.0 * 5) + (1.0 * 5) + (4.0 * 3) + (0.5 * 6)
# = 2 + 10 + 5 + 12 + 3 = 32.0
result_zip = Evaluator.zip_evaluate(coefs, words)
print(f"Resultat : {result_zip} (Attendu : 32.0)")

print("\n--- Test ENUMERATE ---")
result_enum = Evaluator.enumerate_evaluate(coefs, words)
print(f"Resultat : {result_enum} (Attendu : 32.0)")

print("\n--- Test ERREUR (Tailles différentes) ---")
coefs_bad = [1.0, 2.0] # Trop court
print(f"Zip retour : {Evaluator.zip_evaluate(coefs_bad, words)}")
print(f"Enumerate retour : {Evaluator.enumerate_evaluate(coefs_bad, words)}")