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
        elif isinstance(arg, tuple):
            if len(arg) != 2:
                raise ValueError("L'intervalle doit contenir deux elements (debut, fin)")
            start, end = arg
            if start > end:
                raise ValueError("Le debut ne peut pas etre superieur a la fin")
            self.values = [[float(i)] for i in range(start, end)]
            self.shape = (len(self.values), 1)
        else:
            raise TypeError("Argument invalide pour initialiser un Vector")
    
    def dot(self, v):
        """Calcule le produit scalaire"""
        if not isinstance(Vector, v):
            raise TypeError("Le produit scalaire necessite un autre vecteur")
        if self.shape != v.shape:
            raise ValueError("Les vecteurs doivent avoir la meme forme")

        result = 0.0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result += self.values[i][j] * v.values[i][j]
        return result

    def T(self):
        """Retourne la transposee (Ligne <-> Colonne)"""
        if self.shape[0] == 1:
            new = [[x] for x in self.values[0]]
        else:
            new = [[x[0] for x in self.values]]
        return Vector(new)

    def __str__ (self):
        return f"Vector ({self.values})"

    def __repr__ (self):
        return f"Vector ({self.values})"

    def __add__(self, other): # self + other
        if not isinstance(other, Vector):
            raise TypeError("type error")
        if self.shape != other.shape:
            raise ValueError("values error")
        new = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                val = self.values[i][j] + other.values[i][j]
                row.append(val)
            new.append(row)
        return Vector(new)

    def __radd__(self, other): # other + self
        return self.__add__(other)

    def __sub__(self, other): # self = other
        if not isinstance(other, Vector):
            raise TypeError("type error")
        if self.shape != other.shape:
            raise ValueError("values error")
        new = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                val = self.values[i][j] - other.values[i][j]
                row.append(val)
            new.append(row)
        return Vector(new)

    def __rsub__(self, other): # other - self
        result = self - other
        return result * -1

    def __mul__(self, scalar): # (1, 2, 3) * 2
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError("type error")
        new = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                val = self.values[i][j] * scalar
                row.append(val)
            new.append(row)
        return Vector(new)

    def __rmul__(self, scalar): # 2 * (1, 2, 3)
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar): # (1, 2, 3) / 2
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError("type error")
        if scalar == 0:
            raise ZeroDivisionError("pas de div par zero")
        new = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                val = self.values[i][j] / scalar
                row.append(val)
            new.append(row)
        return Vector(new)

    def __rtruediv__(self, scalar):
        raise NotImplementedError("Not defined")