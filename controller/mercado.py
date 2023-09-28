
carrinho = []   
valorProduto = []
#Loop do carrinho 
def addProduto():
    while True:

        print("Digite o produto: ")
        addProduto = input()

        print(" ")

        print("Digite o Valor do produto: ")
        addValor = int(input())


        print("o produto adicionado foi " +addProduto +" com o valor de: R$" + str(addValor)+",00") 
        carrinho.append(addProduto)
        valorProduto.append(addValor)

        print(" ")

        print("seu carrinho: ")
        for i in carrinho:
            print(i)
        print(" ")

        print("Valor do produto")

        print(" ")

        for i in valorProduto:
            print("R$"+str(i)+",00") 
        
        if addProduto == "" and addValor == 0:
        
            carrinho.pop()
            valorProduto.pop()
            break
    
def deletar():
    print("Voce deseja Deletar algum item do carrinho? (S/n)")
    resposta = input()

    if resposta == "S" or resposta == "s":
        print("digite o produto que deseja deletar")
        print(" ")

        remover = input()
        carrinho.remove(remover)
        
        print("Seu carrinho tem: ")
        print(" ")
        for i in carrinho:
            print(i)
    else:
        resultadoCarrinho()




#Resultado do carrinho
def resultadoCarrinho():
    print("Seu carrinho tem: ")
    for i in carrinho:
        print(i)

    print("o valor deu: ")
    aux = 0 
    for i in valorProduto:
        aux+=i
    print("R$"+str(aux)+",00") 
