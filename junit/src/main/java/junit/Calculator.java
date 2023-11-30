package junit;

public class Calculator {
    
    public int add(int a, int b){
        return a+b;
    }

    public int diminuir(int a, int b){
        return a-b; 
    }

    public int mult(int m, int l){
        return m*l;
    }

    public int div(int d, int v){
        return d/v;
    }

    public int pot(int b, int e){
        int resultado = 1;

        for (int i = 0; i < e; i++) {
            resultado = resultado * b;
        }
        return resultado;
    }

    public int rad(int radical){
       return (int) Math.sqrt(radical);
    }

}
