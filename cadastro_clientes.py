class CadastroClientes():
    def _init_(self):
        self.cadastro = []

    def cadastrar_cliente (self,cliente):
        self.cadastro.append(cliente)
        if self.cadastro > 0:
            return "Cadastro realizado com sucesso"