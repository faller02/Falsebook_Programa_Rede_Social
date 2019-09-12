import funções
dados = list()
while 1:
    print("-------------------------------------------------------")
    print("Bem Vindo ao Fallsebook")
    print("-------------------------------------------------------")
    Principal=input("  O quê você deseja?\n------------------------------------------------------- \n (A) Criar sua conta \n (B) Remover sua conta \n (C) Encontrar minha conta \n (D) Imprimir Conta \n (E) Sair da Página \n ").lower()
    print("o tamanho de dados é", len(dados))
    if Principal == "a":
        funções.criarusu(dados)

    if Principal == "b":
        funções.removerusu(dados)

    if Principal == "c":
        funções.buscarusu(dados)

    if Principal == "d":
        funções.imprimir(dados)

    if Principal == "e":
        break
