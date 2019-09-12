def criarusu(dados):
    nome = input('Insira seu nome : ')
    data = input("Iremos Inserir sua data de nascimento (OK) : ").lower()
    if data == 'ok':
        dia = eval(input("Insira seu Dia: "))
        while (dia<1 or dia>31):
            dia = eval(input("Insira seu Dia: "))
        mês = eval(input("Insira seu Mês: "))
        while (mês>12 or mês<1):
            mês = eval(input("Insira seu Mês: "))
            if mês == 2 and dia>31:
                break
        ano = eval(input("Insira seu Ano: "))
        if (ano > 2019):
            print("Seu ano é invalido")
        else:
            print("Sua data é", dia, "/", mês, "/", ano)
            datacorreta= dia, "/", mês, "/", ano
            nickname = input("Insira o nome de usuário: ")
            senha = (input("Sua Senha -> "))
            contagem = len(senha)
            if len(senha) > 8 or contagem < 16:
                user = {"nome": nome, "nick": nickname, "data": datacorreta, "senha": senha}
                dados.append(user)
                print(dados)
                if len(dados) > 0:
                    print("Usuário Criado")
                else:
                    print("não ta indo")

            else:
                print("Sua Senha é Invalida:")
                print("Sua data é", dia, "/", mês, "/", ano)
                datacorreta = dia, "/", mês, "/", ano
                nickname = input("Insira o nome de usuário: ")
                if nickname in dados:
                    print("O Nome de usuário já existe")
                else:
                    senha = (input("Sua Senha -> "))
                    contagem = len(senha)
                    if len(senha) > 8 or contagem < 16:
                        nickname = nome, datacorreta, senha
                        user = {"nome": nome, "nick": nickname, "data": datacorreta, "senha": senha}
                        dados.append(user)
                        print(dados)
                        if len(dados) > 0:
                            print(dados)
                        else:
                            print("não ta indo")



                    else:
                        print("Sua Senha é Invalida:")
    return dados




def removerusu(dados):
    print("Insira o nome do usuário, qual você deseja remover")
    delete=input(" ")
    for n in range(1,len(dados)+1):
        dados.remove(delete)


def buscarusu(dados):
    print("Bem vindo ao programa de busca de usuário!")
    busc=input("Insira o nome do usuário: ")
    i=0
    while i < len(dados):

        dados[i][nickname]
            print("O usuário existe!")
        else:
            print("O usuário não existe!")]
        i=+1





def imprimir(dados):
    print("Bem vindo ao programa de impressão de usuário")
    for n in range(0,len(dados)+1):
        print(dados)
