public class MenorNota {

    public static void main(String[] args) {

        Scanner d=new Scanner(System.in);
        float quantidade;


        float saque;


        System.out.println("//-------------DIGITE O VALOR DO SAQUE---------");        
        saque =d.nextFloat();

        if(saque%5!=0){
            System.out.print("Não existem notas disponiveis");

        }


        if(saque%100==0){
            quantidade=saque/100;

            System.out.print("Numero de notas retornado é: "+quantidade +"  VALOR DO SAQUE FOI :" + saque);

        }else if(saque%50==0){
            quantidade=saque/50;

            System.out.print("Numero de notas retornado é: "+quantidade +"  VALOR DO SAQUE FOI :" + saque);
        }else if(saque%20==0){
            quantidade=saque/20;
            System.out.print("Numero de notas retornado é: "+quantidade +"  VALOR DO SAQUE FOI :" + saque);

        }else if(saque%10==0){
            quantidade=saque/10;
            System.out.print("Numero de notas retornado é: "+quantidade +"  VALOR DO SAQUE FOI :" + saque);

        }else if(saque%5==0){
            quantidade=saque/5;
            System.out.print("Numero de notas retornado é: "+quantidade +"  VALOR DO SAQUE FOI :" + saque);

        }

    }
}