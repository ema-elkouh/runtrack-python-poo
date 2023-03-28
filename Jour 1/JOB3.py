class Operation:
    def additioner(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        return self.nombre1 + self.nombre2

operation = Operation(12,3)

resultat = operation.additioner()

print(resultat)
