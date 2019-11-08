public class Saque {

public static void main(String[] args) {

Scanner s = new Scanner(System.in);
String str = s.nextLine();

int Nota100Contador = 0;
int Nota50Contador = 0;
int Nota20Contador = 0;
int Nota10Contador = 0;
int Nota5Contador = 0;
int Nota2Contador = 0;
int Nota1Contador = 0;

int Total = 0;

int ValorSacado = Integer.parseInt(str);

while (ValorSacado >= 100)
{
ValorSacado = ValorSacado – 100;
Nota100Contador++;
}
while (ValorSacado >= 50)
{
ValorSacado = ValorSacado – 50;
Nota50Contador++;
}
while (ValorSacado >= 20)
{
ValorSacado = ValorSacado – 20;
Nota20Contador++;
}
while (ValorSacado >= 10)
{
ValorSacado = ValorSacado – 10;
Nota10Contador++;
}
while (ValorSacado >= 5)
{
ValorSacado = ValorSacado – 5;
Nota5Contador++;
}
while (ValorSacado >= 2)
{
ValorSacado = ValorSacado – 2;
Nota2Contador++;
}
while (ValorSacado == 1)
{
ValorSacado = ValorSacado – 1;
Nota1Contador++;
}

System.out.println(“Notas de 100 sacadas: ” + Nota100Contador + “.”);
System.out.println(“Notas de 50 sacadas: ” + Nota50Contador + “.”);
System.out.println(“Notas de 20 sacadas: ” + Nota20Contador + “.”);
System.out.println(“Notas de 10 sacadas: ” + Nota10Contador + “.”);
System.out.println(“Notas de 5 sacadas: ” + Nota5Contador + “.”);
System.out.println(“Notas de 2 sacadas: ” + Nota2Contador + “.”);
System.out.println(“Notas de 1 sacadas: ” + Nota1Contador + “.”);
Total = Nota100Contador+
Nota50Contador+
Nota20Contador+
Nota10Contador+
Nota5Contador+
Nota2Contador+
Nota1Contador;
System.out.println(“Total de Notas: “+Total);
}
}