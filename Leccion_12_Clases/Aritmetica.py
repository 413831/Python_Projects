class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, multiplicar y dividir
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        if self.operandoB > 0:
            return self.operandoA / self.operandoB
        else:
            return 1

# TEST

aritmetica = Aritmetica(25,3)
print(aritmetica.sumar())
print(aritmetica.restar())
print(aritmetica.multiplicar())
print(aritmetica.dividir())
