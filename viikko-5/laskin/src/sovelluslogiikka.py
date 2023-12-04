class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen = arvo

    def miinus(self, operandi):
        self._edellinen = self._arvo
        self._arvo -= operandi

    def plus(self, operandi):
        self._edellinen = self._arvo
        self._arvo += operandi

    def nollaa(self):
        self.aseta_arvo(0)

    def aseta_arvo(self, arvo):
        self._edellinen = self._arvo
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def edellinen(self):
        return self._edellinen
