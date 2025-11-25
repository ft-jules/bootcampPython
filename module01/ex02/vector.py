class Vector:
    def __init__(self, arg):
        """
        Initialise le vecteur avec une liste, une taille ou un intervalle.
        """

        if isinstance(arg, list):
            if not arg:
                raise ValueError("empty list")
            self.values = arg
            self.shape = (len(self.values), len(self.values[0]))
        elif isinstance(arg, int):
            if arg <= 0:
                raise ValueError("taille nulle ou negative")
            self.values = [[float(i)] for i in range(arg)]
            self.shape = (arg, 1)