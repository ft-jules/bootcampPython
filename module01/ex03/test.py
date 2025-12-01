from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte."

print("--- Ordered ---")
for word in generator(text, sep=" ", option="ordered"):
    print(word)

print("\n--- Unique ---")
text_double = "Lorem Ipsum Lorem Ipsum"
for word in generator(text_double, sep=" ", option="unique"):
    print(word)

print("\n--- Shuffle ---")
# Lance plusieurs fois pour vérifier que ça change !
for word in generator(text, sep=" ", option="shuffle"):
    print(word)