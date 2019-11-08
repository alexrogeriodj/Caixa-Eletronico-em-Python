public classCaixaEletronico {
	private final Integer[] notas = new Integer[] { 100, 50, 20, 10, 5, 2 };
	private int valorSaque = 0;
	
	public int getValorSaque() {
		return valorSaque;
	}

	public void setValorSaque(int valorSaque) {
		this.valorSaque = valorSaque;
	}

	public List<Integer> getNotas() {
		return Collections.unmodifiableList(Arrays.asList(notas));
	}

	private boolean sacar(final Integer valor) {
		if(valor <= 0) {
			throw new IllegalArgumentException();
		}
		boolean status = false;
		int resto = valor % 100;
		if((resto) == 0 || 
				((resto = valor % 50) == 0) || 
				((resto = valor % 20) == 0) || 
				((resto = valor % 10) == 0) || 
				((resto = valor % 5) == 0) || 
				((resto = valor % 2) == 0)) {
			status = true;
		}
		return status;
	}

	public static void main(String[] args) {
		CaixaEletronico caixaEletronico = new CaixaEletronico();
		boolean status = false;
		for(int i = 1; i < 500; i++) {
			status = caixaEletronico.sacar(i);
			System.out.println(i + " = " + (status ? "Saque permitido." : "Não é possivel sacar esse valor."));

			public class Principal {
	
	public static void calcular(double valor){
		int[] cedulas = {100,50,25,10,5,2};
		
		for(int i = 0; i < cedulas.length; i++){
			if( valor >= cedulas[i] ){
				System.out.println( (int)valor/cedulas[i] + " notas de " + cedulas[i]);
				valor = valor % cedulas[i];
			}
			
		}
		System.out.println("Sobram: " +valor);
	}
	
	public static void main(String[] args) {
		calcular(1553.5);
	}
}
					