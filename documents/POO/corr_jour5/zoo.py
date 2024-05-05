# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta

class Carnivore:
    @abstractmethod
    def manger(self, animal):
        pass
    
class Herbivore:
    @abstractmethod
    def manger(self):
        pass
    
class Omnivore:
    @abstractmethod
    def manger(self, animal=None):
        pass

class Animal(metaclass=ABCMeta):
    def __init__(self, poids, couleur):
        self.poids = poids
        self.couleur = couleur
    @abstractmethod
    def moyenExpression(self):
        pass
    @abstractmethod
    def deplacement(self):
        pass
    def __str__(self):
        return "Je suis un animal. "
    
class AnimalDomestique(Animal, metaclass=ABCMeta):
    def __init__(self, poids, couleur, nom):
        super().__init__(poids, couleur)
        self.nom = nom
    def deplacement(self):
        print ('Je me déplace en appartement.')
    def __str__(self):
        return super().__str__() + "Je suis un animal domestique. "
        
class AnimalSauvage(Animal, metaclass=ABCMeta):
    def __init__(self, poids, couleur):
        super().__init__(poids, couleur)
    def deplacement(self):
        print ('Je me déplace dans la nature.')
    def __str__(self):
        return super().__str__() + "Je suis un animal sauvage. "
    
class Chat(AnimalDomestique, Carnivore):
    def __init__(self, poids, couleur, nom):
        super().__init__(poids, couleur, nom)
    def moyenExpression(self):
        print ('Je miaule')
    def __str__(self):
        return super().__str__() + "Je suis un chat qui s'appelle: " + self.nom + "."
    def manger(self, proie):
        print ("Je mange un " + proie.__class__.__name__)
        if isinstance(proie, Lapin):
            Lapin.compteurLapin -= 1
        
class Chien(AnimalDomestique, Carnivore):
    def __init__(self, poids, couleur, nom):
        super().__init__(poids, couleur, nom)
    def moyenExpression(self):
        print ("J'aboie")   
    def manger(self, proie):
        print ("Je dévore un " + proie.__class__.__name__)
        if isinstance(proie, Lapin):
            Lapin.compteurLapin -= 1
    
class Lapin(AnimalDomestique, Herbivore):
    compteurLapin = 0
    def __init__(self, poids, couleur, nom):
        super().__init__(poids, couleur, nom)
        Lapin.compteurLapin += 1
    def moyenExpression(self):
        print ('Je glapis')
    def __str__(self):
        return super().__str__() + "Je suis un chat qui s'appelle: " + self.nom + "."
    def manger(self):
        print ("Je grignotte.")
    

class Tigre(AnimalSauvage, Carnivore):
    def __init__(self, poids, couleur):
        super().__init__(poids, couleur)
    def moyenExpression(self):
        print ('Je rugis')
    def __str__(self):
        return super().__str__() + "Je suis un tigre."
    def manger(self, proie):
        print ("Je déchire un " + proie.__class__.__name__)
        if isinstance(proie, Lapin):
            Lapin.compteurLapin -= 1
        
class Vache(AnimalSauvage, Herbivore):
    def __init__(self, poids, couleur):
        super().__init__(poids, couleur)
    def moyenExpression(self):
        print ('Je mugit.')
    def manger(self):
        print ("Je broute.")

class Sanglier(AnimalSauvage, Omnivore):
    def __init__(self, poids, couleur):
        super().__init__(poids, couleur)
    def moyenExpression(self):
        print ('Je grogne')
    def manger(self, proie=None):
        if proie is None:
            print ("Je mange.")
        else:
            print ("Je déchire un " + proie.__class__.__name__)
            if isinstance(proie, Lapin):
                Lapin.compteurLapin -= 1



try:
    a = Animal(150, 'Bleu')
    ad = AnimalDomestique(150, 'Bleu', 'Bunny')
    ad.deplacement()
except:
    #print ('erreur maitrisée')
    pass

bunny = Lapin(150, 'Bleu', 'Bunny')
print (bunny)
bunny.deplacement()
bunny.moyenExpression()

bunny2 = Lapin(150, 'Bleu', 'Bunny')
bunny3 = Lapin(150, 'Bleu', 'Bunny')

felix = Chat(18, 'Blanc', 'Felix')
chips = Chat(16, 'Noir', 'Chips')

tigrou = Tigre(899, 'orange')
vache1 = Vache(550, 'Verte')
vache2 = Vache(625, 'Gris clair')
vache3 = Vache(653, 'Vert foncé')

# bunny
animaux = [felix, chips, tigrou, vache1, vache2, vache3]
print ('Nombre de lapins = ' + str(Lapin.compteurLapin))

for a in animaux:
    if isinstance(a, Carnivore):
        if Lapin.compteurLapin > 1:
            a.manger(bunny)
        else:
            print ("pas assez de lapin")

















