from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

# --- TEST MAP ---
print("--- MAP ---")
# Exemple 1 : Carré
x = [1, 2, 3, 4, 5]
print(list(ft_map(lambda t: t + 1, x))) 
# Attendu : [2, 3, 4, 5, 6]

# Exemple 2 : Addition de deux listes
print(list(ft_map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))
# Attendu : [11, 22, 33]

# --- TEST FILTER ---
print("\n--- FILTER ---")
# Exemple 1 : Garder les pairs
x = [1, 2, 3, 4, 5]
print(list(ft_filter(lambda t: t % 2 == 0, x)))
# Attendu : [2, 4]

# Exemple 2 : None (garder les True)
y = [0, 1, False, True, "Hello", ""]
print(list(ft_filter(None, y)))
# Attendu : [1, True, 'Hello']

# --- TEST REDUCE ---
print("\n--- REDUCE ---")
lst = ['H', 'e', 'l', 'l', 'o']
# Concaténation
print(ft_reduce(lambda u, v: u + v, lst))
# Attendu : "Hello"

# Somme avec initializer
nums = [1, 2, 3]
print(ft_reduce(lambda u, v: u + v, nums, 10))
# Attendu : 16 (10 + 1 + 2 + 3)