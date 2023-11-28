package junit;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();
        assertEquals(5, calculator.add(2, 3));
        assertEquals(-1, calculator.add(-4, 3));
        
    }

    @Test
    public void testDiminuir() {
        Calculator calculator = new Calculator();
        assertEquals(2, calculator.diminuir(5, 3));
        assertEquals(-7, calculator.diminuir(-4, 3));
       
    }

    @Test
    public void testMult() {
        Calculator calculator = new Calculator();
        assertEquals(15, calculator.mult(5, 3));
        assertEquals(-12, calculator.mult(4, -3));
     
    }

    @Test
    public void testDiv() {
        Calculator calculator = new Calculator();
        assertEquals(2, calculator.div(6, 3));
        assertEquals(-2, calculator.div(6, -3));
      
    }

    @Test
    public void testDivisaoPorZero() {
        Calculator calculator = new Calculator();
        try {
            calculator.div(10, 0);
            fail("Deveria lançar uma exceção de divisão por zero.");
        } catch (ArithmeticException e) {
           
        }
    }

    @Test
    public void testOperacoesComNumerosNegativos() {
        Calculator calculator = new Calculator();
        assertEquals(-5, calculator.add(-2, -3));
        assertEquals(-1, calculator.diminuir(-4, -3));
        assertEquals(15, calculator.mult(-5, -3));
        assertEquals(2, calculator.div(-6, -3));
    }


    @Test
    public void testGrandesNumeros() {
        Calculator calculator = new Calculator();
        assertEquals(500000000, calculator.add(200000000, 300000000));
        assertEquals(-100000000, calculator.diminuir(-40000000, 60000000));
        assertEquals(1500000000, calculator.mult(5000000, 300));
        assertEquals(2, calculator.div(60000000, 30000000));
    }

   

}

