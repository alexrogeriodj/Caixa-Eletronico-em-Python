class Nome:
    def __init__(self, nome):
        if nome is None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        self.chave = nome.strip().lower()

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.nome} Chave: {self.chave }>"

    def __eq__(self, outro):
        print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro.nome

        from nome import Nome
        A = Nome("Nilo")
        print(A)
        B = Nome("  ")
        C = Nome(None)

        from nome import Nome
        A = Nome("Nilo")
        A == Nome("Nilo")
        A != Nome("Nilo")
        A > Nome("Nilo")
        A < Nome("Nilo")
        A <= Nome("Nilo")
        A >= Nome("Nilo")

        A.CriaChave("X")
        Nome.CriaChave("X")

        A = Nome("Teste")
        A
        A.nome = "Nilo"
        A
        A.chave = "TST"
        A

        from nome import Nome
        A = Nome("Nilo")
        A
        A.nome = "Nilo Menezes"
        A
        A.__nome
        A.__chave
        A.chave
        A._Nome__chave