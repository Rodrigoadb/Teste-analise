import unittest
from Calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):

    def test_somar(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.add(2, 3), 5)
        self.assertEqual(calculadora.add(-4, 3), -1)


    def test_subtrair(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.diminuir(5, 3), 2)
        self.assertEqual(calculadora.diminuir(-4,3), -7)


    def test_multiplicar(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.mult(5, 3), 15)
        self.assertEqual(calculadora.mult(-4, 3), -12)


    def test_dividir(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.div(6, 3), 2)
        self.assertEqual(calculadora.div(6, -3), -2)


    def test_divisao_por_zero(self):
        calculadora = Calculadora()
        try:
            self.assertEqual(calculadora.div(6, 0), 0)
            self.assertEqual(calculadora.div(-3, 0), 0)
        except ZeroDivisionError as e:
            print("Não é possível dividir por zero")


    def test_operacao_com_numeros_negativos(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.add(-2,-3), -5)
        self.assertEqual(calculadora.diminuir(-4, -3), -1)
        self.assertEqual(calculadora.mult(-5, -3), 15)
        self.assertEqual(calculadora.div(-6, -3), 2)


    def test_numeros_grandes(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.add(200000000, 300000000), 500000000)
        self.assertEqual(calculadora.diminuir(-40000000, 60000000), -100000000)
        self.assertEqual(calculadora.mult(5000000, 300), 1500000000)
        self.assertEqual(calculadora.div(60000000, 30000000), 2)


    def test_potencia(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.pot(2, 3), 8)
        self.assertEqual(calculadora.pot(4, 2), 16)

    def test_potencia_elevada_a_zero(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.pot(2, 0), 1)
        self.assertEqual(calculadora.pot(4, 0), 1)
    
    def test_radiciacao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.rad(4, 2), 2)
        self.assertEqual(calculadora.rad(8, 3), 2)
        self.assertEqual(calculadora.rad(256, 2), 16)
        self.assertEqual(calculadora.rad(9, 2), 3)
        self.assertEqual(calculadora.rad(625, 2), 25)
        self.assertEqual(calculadora.rad(125, 3), 5)
        self.assertEqual(calculadora.rad(36, 2), 6)
        self.assertEqual(calculadora.rad(32, 5), 2)
        self.assertEqual(calculadora.rad(100, 2), 10)
#  @Test
#     public void testRadiciacao() {
#         Calculator calculator = new Calculator();
#         assertEquals(2, calculator.rad(4));
#         assertEquals(4, calculator.rad(16));
#         assertEquals(16, calculator.rad(256));
#         assertEquals(3, calculator.rad(9));
#         assertEquals(5, calculator.rad(25));
#         assertEquals(6, calculator.rad(36));
#         assertEquals(10, calculator.rad(100));


#     }

if __name__ == "__main__":
    unittest.main()

    
    
    # @Test
    # public void testRadiciacao() {
    #     Calculator calculator = new Calculator();
    #     assertEquals(2, calculator.rad(4));
    #     assertEquals(4, calculator.rad(16));
    #     assertEquals(16, calculator.rad(256));
    #     assertEquals(3, calculator.rad(9));
    #     assertEquals(5, calculator.rad(25));
    #     assertEquals(6, calculator.rad(36));
    #     assertEquals(10, calculator.rad(100));


    # }