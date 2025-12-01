from vector import Vector

print("--- Test Init ---")
try:
    print(f"Par liste : {Vector([[1., 2., 3.]])}")
    print(f"Par taille (3) : {Vector(3)}")
    print(f"Par range (10, 12) : {Vector((10, 12))}")
except Exception as e:
    print(e)

    print("\n--- TEST OPÉRATEURS ---")
v1 = Vector([[10., 11., 12.]]) # Ligne
v2 = Vector([[1., 2., 3.]])    # Ligne

print(f"v1 : {v1}")
print(f"v2 : {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2  = {v1 * 2}")
print(f"v1 / 2  = {v1 / 2}")

try:
    print(2 / v1)
except Exception as e:
    print(f"Test erreur division : {e}")