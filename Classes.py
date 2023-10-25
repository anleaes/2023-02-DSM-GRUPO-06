# Classe Cliente
class Cliente:
    def __init__(self, primeiro_nome, ultimo_nome, endereco, numero_telefone, email, genero):
        self._primeiro_nome = primeiro_nome
        self._ultimo_nome = ultimo_nome
        self._endereco = endereco
        self._numero_telefone = numero_telefone
        self._email = email
        self._genero = genero
        
# Classe Ordem com herança do Cliente
class Ordem(Cliente):
    def __init__(self,primeiro_nome, ultimo_nome, endereco, numero_telefone, email, genero, preco_total, status):
        super().__init__(primeiro_nome, ultimo_nome, endereco, numero_telefone, email, genero)
        self._preco_total = preco_total
        self._status = status
               
# Classe Ordem de item        
class Order_Item(Produto):
    def __init__(self,nome, descricao, data_fabricacao, ativo, quantidade, preco_unidade):
        super().__init__(nome, descricao, data_fabricacao, ativo)
        self._quantidade = quantidade
        self._preco_unitario = preco_unidade