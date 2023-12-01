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
        int fatoracao = radical;
        int[] cont = {0, 0, 0};
        while(fatoracao != 1){
            if(fatoracao % 2 == 0){
                fatoracao = fatoracao / 2;
                cont[0] = cont[0] + 1;

            }
            else if(fatoracao % 3 == 0){
                fatoracao = fatoracao / 3;
                cont[1] = cont[1] + 1;
            }
            else if(fatoracao % 5 == 0){
                fatoracao = fatoracao / 5 ;
                cont[2] = cont[2] + 1;
            }
        }    
       

        int exp2 = 0;
        int exp3 = 0;
        int exp5 = 0;

        int resultado = 1;

        if(cont[0] != 0){
            exp2 = (cont[0] / 2);
            resultado = resultado * pot(2, exp2);
            
        }

        if(cont[1] != 0){
            exp3 = (cont[1] / 2);
            resultado = resultado * pot(3, exp3);
        }
        
        if(cont[2] != 0){
            exp5 = (cont[2] / 2);
            resultado = resultado * pot(5, exp5);
        }

        // Math.sqrt(resultado);
        return resultado;
    }

}
