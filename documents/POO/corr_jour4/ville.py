# -*- coding: utf-8 -*-

class Ville:
    
    def __init__(self, nom, nbHabitants = 0):
        self.nom = nom
        if nbHabitants > 0:
            self.nbHabitants = nbHabitants
        else:
            self.nbHabitants = 0
        
    def nbHabitantsConnu(self): 
        return self.nbHabitants > 0
    
    def __str__(self): 
        s  = "Ville de " + self.nom.upper()
        if self.nbHabitantsConnu():
            s += " ; " + str(self.nbHabitants) + " habitants"
        return s
    
    def categorie(self):
        if not self.nbHabitantsConnu():
            return '?'
        elif self.nbHabitants < 500000:
            return 'A'
        else:
            return 'B'
        
    def getNom(self):
        return self.nom
        
        
class Capitale(Ville):
    
    def __init__(self, nom, nomPays, pop = 0):
        super().__init__(nom, pop)
        self.nomPays = nomPays
    
    def categorie(self):
        return 'C'
    
    def __str__(self):
        return super().__str__() + "." + " Capitale de " + str(self.nomPays);
    


if __name__ == '__main__':
    v1 = Ville ("Toulouse")
    v2 = Ville ("Strasbourg", 272975)

    print(v1)
    print(v2)
    print("")
    
    c1 = Capitale("Paris", "France")
    c2 = Capitale("Rome", "Italie", 2700000)

    c1.nbHabitants = 2181371
    print(c1)
    print(c2)
    print("")

    print("catégorie de la ville de " + v1.getNom() + " : " + v1.categorie());
    print("catégorie de la ville de " + v2.getNom() + " : " + v2.categorie());
    print("catégorie de la ville de " + c1.getNom() + " : " + c1.categorie());
    print()
    
    
    
    
    
    