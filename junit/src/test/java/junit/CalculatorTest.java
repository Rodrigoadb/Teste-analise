package junit;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CalculatorTest {

    public Calculator calc = new Calculator();


    /*Testando a Soma */
    @Test
    public void soma(){
        assertEquals(2, calc.add(1, 1));
    }

    /*Testando a Subtração */
    @Test
    public void subtracao(){
        int resultado = calc.diminuir(8,2);
        assertEquals(6, resultado);
    }

    /*Testando a multiplicacão */
    @Test
    public void multiplicacao(){
        assertEquals(25, calc.mult(5,5));
    }

    /*Testando a divisão */
    @Test
    public void divisao(){
        assertEquals(4, calc.div(8,2));
    }

}
