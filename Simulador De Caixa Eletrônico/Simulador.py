public class Caixa {

   
    public static void main(String[] args) {
        
        Scanner tec = new Scanner(System.in);
        Operador M = new Operador();
        int senha = 12345;
        int money;
            System.out.print("Digite sua senha : ");
                senha = tec.nextInt();
                
      if(senha == 12345){
                M.tela();
      }else{
          
          System.out.println("Senha incorreta! tente novamente!");
      }
   

    }
}
   
//Métodos a serem chamados (Classe Operador )


import java.util.Scanner;//importação para leitura de dados

// Métodos operadores

public class Operador { //mostra saldo na tela
   
   
    
    public void saldo(){
        
        int valor =  1000;
    
        System.out.println(" Seu saldo é "+ valor);
    
    }
    

    public void tela (){//tela de escolha
         
        
    Scanner tec = new Scanner(System.in);
    Operador S = new Operador();
   
    
    String escolha;
        System.out.println(" a- consultar saldo\n b- Depositar\n c- Sacar ");
                escolha = tec.nextLine();
                if("a".equals(escolha)){
                    S.saldo();
               
                }
                if("b".equals(escolha )){
    
                    S.depositar();
                
                }
                if ("c".equals(escolha)){
                    S.saque();
                
                }
            


    }
    public void depositar( ){//exige do usuário valores para deposito
        int Vdeposito; 
        int valor =  1000;
        Scanner tec = new Scanner(System.in);
        Operador  box = new Operador();
        
         
            System.out.print("Digite um valor para depósito : ");
             Vdeposito = tec.nextInt();
             
            
            valor = valor + Vdeposito;
            
    
            System.out.println("Seu novo saldo é "+valor );
      
            box.inter();
        
        
    
    
    
   }
   public void inter(){
       Scanner tec = new Scanner(System.in);
       Operador R = new Operador();
       String exite ;
         System.out.println(" e- voltar\n f - sair ");
                 exite = tec.nextLine();
                 if (exite.equals("e")){
          R.tela();}
                 if(exite.equals("f")){
                     System.exit(0);
                 
                 }
                    
        
   } 
   public void saque (){
       int valor =  1000;
       Scanner tec = new Scanner(System.in);
       Operador  box = new Operador();
       
       System.out.println("Digite o valor do seu saque: ");
        int Vsaque = tec.nextInt();
        valor = (valor -Vsaque);
        if(valor <Vsaque){
            System.out.println("você não possui mais  fundos suficientes! ");
            valor = 0;
        }
        
        System.out.println("seu novo saldo é :"+valor);
            box.inter();
   
   }
    
}