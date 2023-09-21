

print("Escolha uma opção")
print("1- realizar compra")
print("2- adicionar um produto ao estoque")
print("3- sair")
menu = int(input())

match menu:
    case 1:
        print("Realizar compra")
    case 2:
        print("Adicionar um produto ao estoque")
    case 3:
        print("sair")
    case "":
        print("Escola alguma opção")
