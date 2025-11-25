import sys

class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        """
        Initialise un personnage générique de Game of Thrones.
        """
        # Vérification des types
        if not isinstance(first_name, str) or not first_name:
            print("Erreur : Le prénom doit être une chaîne de caractères non vide.")
            sys.exit()
        if not isinstance(is_alive, bool):
            print("Erreur : is_alive doit être un booléen (True/False).")
            sys.exit()

        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        """
        Initialise un membre de la famille Stark.
        """
        # Appel du constructeur parent pour initialiser first_name et is_alive
        super().__init__(first_name, is_alive)
        
        # Attributs spécifiques aux Stark
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """
        Affiche la devise de la Maison.
        """
        print(self.house_words)

    def die(self):
        """
        Tue le personnage (passe is_alive à False).
        """
        self.is_alive = False
        