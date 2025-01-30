#Construindo primeira classe

class Dog:
    def __init__(self, raca):
        self.idade = 10
        self.raca = raca

    def envelhecer(self, idade):
        idade += 1
        return idade


dog = Dog("Labrador")
dog.idade = 20

dog.idade = dog.envelhecer(10)

print(dog.idade)
print(dog.raca)


class Circle:
    def __init__(self, raio = 1):
        self.raio = raio

    def calcula_area(self):
        return self.raio * self.raio * 3.14
    


c1 = Circle(10)
print(c1.calcula_area())


#Herança 

class Animal:
    def __init__(self):
        print("Animal criado") 

    def quem_sou_eu(self):
        print("Eu sou um animal ")
        
    def comer(self):
        print("Comendo")


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Eu sou um cachorro")

    def quem_sou_eu(self):
        print("Eu sou um cachorro ")
    

animal = Animal()
print(animal.quem_sou_eu())
dog = Cachorro()
print(dog.quem_sou_eu())
