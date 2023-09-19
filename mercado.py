
carrinho = []   
valorProduto = []

#Loop do carrinho 
while True:
    print("Digite o produto: ")
    addProduto = input()

    print("Digite o Valor do produto: ")
    addValor = input()

    
    print("o produto adicionado foi " +addProduto +" com o valor de: R$" +addValor +",00")
    carrinho.append(addProduto)
    valorProduto.append(addValor)

    print("seu carrinho: ")
    print(carrinho)

    print("Valor do produto")
    print(valorProduto)

    if addProduto == str('') or valorProduto == str(''):
        carrinho.pop()
        valorProduto.pop()
        break
    

#Resultado do carrinho
print("Seu carrinho tem: ")
for i in carrinho:
    print(i)
print("o valor deu: ")
for i in valorProduto:
    print(i)

soma = len(valorProduto)
print(sum(soma))

print(soma + soma)
