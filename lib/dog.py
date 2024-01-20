#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.breed = breed
        self.name = name

    @property
    def name(self):
        return self._name
    
    @property
    def breed(self):
        return self._breed
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value =="":

            print("Name must be string between 1 and 25 characters.\n")
            self._name = None
        elif isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.\n")
            self._name = None

    @breed.setter        
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
    
            print("Breed must be in list of approved breeds.\n")
            self._breed = None

fido = Dog(name="Daisy", breed="Corgi")
# fido = Dog("Fido","Corgi")
# fido = Dog("FidoFidoFidoFidoFidoFidoFidoFidoFido","CorgiFido")
# fido.name = "FidoFidoFidoFidoFidoFidoFidoFidoFido"
# fido.breed = "CorgiFido"
# fido.name = ""
# fido.breed = "Corgi"
# print(fido.name)
# print(fido.breed)



