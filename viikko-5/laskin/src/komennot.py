from sovelluslogiikka import Sovelluslogiikka

class Summa:
    def __init__(self, logic: Sovelluslogiikka, input):
        self.logic = logic
        self.input = input

    def suorita(self):
        self.logic.plus(self.input())

class Erotus:
    def __init__(self, logic: Sovelluslogiikka, input):
        self.logic = logic
        self.input = input

    def suorita(self):
        self.logic.miinus(self.input())

class Nollaus:
    def __init__(self, logic: Sovelluslogiikka, input):
        self.logic = logic
        self.input = input

    def suorita(self):
        self.logic.aseta_arvo(0)

class Kumoa:
    def __init__(self, logic: Sovelluslogiikka, input):
        self.logic = logic
        self.input = input

    def suorita(self):
        self.logic.aseta_arvo(self.logic.edellinen())
