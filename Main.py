from Classes import Cliente
from Classes import Ordem


# ============== Função que printa os dados ==============
def printaInfos(ordem):
    print("Nome: ", ordem._primeiro_nome)
    print("Ultimo nome: ", ordem._ultimo_nome)
    print("Endereço: ",ordem._endereco)
    print("Numero de telefone: ",ordem._numero_telefone)
    print("Email: ",ordem._email)
    print("Genero: ",ordem._genero)
    print("Preço total: ",ordem._preco_total)
    print("Status: ",ordem._status)
    




# ============== Cria, setta e printa as classes ==============



ordem1 = Ordem("Gabriel", "Amaral", "Rua da Bandeira, 55", "51995619518", "gabriel.amaral155@hotmail.com", "Masculino", "500.40", "Vendido")
printaInfos(ordem1)