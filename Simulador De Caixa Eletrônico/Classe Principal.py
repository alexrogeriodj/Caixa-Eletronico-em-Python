public class ContaBancaria {

   
    public static void main(String[] args) {
         Scanner tec = new Scanner(System.in);
        Menu M = new Menu();
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


//classe Menu


public class Menu {
    
    
      public void tela (){//tela de escolha
         
        
    Scanner tec = new Scanner(System.in);
    OperadorJ S = new OperadorJ();
   
    
    String escolha;
   
        System.out.println(" a- consultar saldo\n b- Depositar\n c- Sacar ");
                escolha = tec.nextLine();
               /* if("a".equals(escolha)){
                    S.setsaldo(c);
               
                }*/
                if("b".equals(escolha )){
    
                    S.depositar();
                
                }
             /* if ("c".equals(escolha)){
                    S.saque();
                
                }*/
            


    }
    //classe Operador


public class OperadorJ {
    float valor = 1000;
    
   public void depositar(){//exige do usuário valores para deposito
        float Vdeposito; 
       
        Scanner tec = new Scanner(System.in);
        Menu  box = new Menu();
        
         
            System.out.print("Digite um valor para depósito : ");
             Vdeposito = tec.nextInt();
             
            
            valor = valor + Vdeposito;
            
    
            System.out.println("Seu novo saldo é "+valor );
      
            box.tela();
        
        
    
    
    
   }
    
}

 