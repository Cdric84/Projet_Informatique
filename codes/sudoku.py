

class Sudoku():
    def __init__(self, n):
        # Pour l'instant, n=3
        self.n = n
        self.cote = n**2
        self.grille = [0]*(n**2)


    def ligne(self, l):
        # l de 0 à 8
        n = self.n
        return [self.grille[n*l+k] for k in range(n)]

    def colonne(self, c):
        # c de 0 à 8
        n = self.n
        return [self.grille[n*k+c] for k in range(n)]

    def carre(self, nc):
        n = self.n
        lc = n*(nc//3)
        cc = n*(nc%n)
        return [self.grille[n*k+lc] for k in range(n)]
