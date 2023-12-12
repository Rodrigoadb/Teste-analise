class Calculadora:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def diminuir(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pot(self, a, b):
        return a ** b

    def rad(self, a, b):
        fatoracao = a
        cont = [0,0,0,0,0]

        while fatoracao != 1:
            if fatoracao % 2 == 0:
                fatoracao = fatoracao / 2
                cont[0] += 1

            elif fatoracao % 3 == 0:
                fatoracao = fatoracao / 3
                cont[1] += 1
            
            elif fatoracao % 5 == 0:
                fatoracao = fatoracao / 5
                cont[2] += 1
            
            elif fatoracao % 7 == 0:
                fatoracao = fatoracao / 7
                cont[3] += 1

            elif fatoracao % 11 == 0:
                fatoracao = fatoracao / 11
                cont[4] += 1

            exp = {"2": 0, "3": 0, "5": 0, "7": 0, "11": 0}

            resultado = 1

            if cont[0] != 0:
                exp["2"] = (cont[0] / b)
                resultado = resultado * self.pot(2, exp["2"])

            if cont[1] != 0:
                exp["3"] = (cont[1] / b)
                resultado = resultado * self.pot(3, exp["3"])

            if cont[2] != 0:
                exp["5"] = (cont[2] / b)
                resultado = resultado * self.pot(5, exp["5"])

            if cont[3] != 0:
                exp["7"] = (cont[3] / b)
                resultado = resultado * self.pot(7, exp["7"])

            if cont[4] != 0:
                exp["11"] = (cont[4] / b)
                resultado = resultado * self.pot(11, exp["11"])

        return resultado
