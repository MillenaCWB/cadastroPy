from cliente import cliente
from cadastro_cliente import CadastroCliente
def test_cadastro_sucesso():
    cliente = Cliente('Will',20,'will@teste.com')
    cadastro_cliente = CadastroCliente ()
    resposta = Cadastro_cliente.cadastra_cliente(cliente)
    assert reposta = "Cadastro realizado com sucesso"

def test_cadastro_nome_menor_que_tres():
    cliente = cliente('Wi',20,'will@test.com')
    cadastro_cliente = CadastroCliente ()
    resposta = Cadastro_cliente.cadastra_cliente(cliente)
    assert reposta = "Erro no cadastro"
