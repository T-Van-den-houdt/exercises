# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
import re
from abc import ABC, abstractmethod
class Person:

    def __init__(self, id, name, is_a_student):
        self.id = id
        self.is_a_student = is_a_student
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if (self.is_valid_name(value)):
            self._name = value
        else:
            raise ValueError("Naam is ongeldig")

    @staticmethod
    def is_valid_name(name):
        pattern = '(\\w+) (\\w+)'
        if re.fullmatch(pattern, name):
            return True
        return False

person = Person(0, "Patje Krimson", False)

class Residence(ABC):
    
    def __init__(self, addres, area, number_of_rooms):
        self.addres = addres
        self.area = area
        self.number_of_rooms = number_of_rooms
        self._occupants = dict()

        @property
        def number_of_occupants(self):
            return len(self._occupants)

        @property
        def maximum_occupants(self):
            popa = self.area // 20
            popr = self.number_of_rooms * 2
            return min(popa, popr)

        def register_resident(self, person):
            if person in self._occupants:
                return 
            if self.number_of_occupants >= maximum_occupants:
                raise RuntimeError
            self._occupants[person.id] = person

    