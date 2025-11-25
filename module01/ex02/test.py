from vector import Vector

print("--- Test Init ---")
try:
    print(f"Par liste : {Vector([[1., 2., 3.]])}")
    print(f"Par taille (3) : {Vector(3)}")
    print(f"Par range (10, 12) : {Vector((10, 12))}")
except Exception as e:
    print(e)