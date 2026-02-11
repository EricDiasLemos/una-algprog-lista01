
segura = input("A compra é segura? (S/N) ")
econômica = input("é o mais econômico? (S/N) ")

if segura == "S" and econômica == "S":
    vendedor = input("Qual o vendedor? (Amazon/Loja Oficial Apple/Outro) ")

    if vendedor == "Amazon" or vendedor == "Loja Oficial Apple":
        saldocartao = float(input("Qual o saldo do cartão? "))
        preco = float(input("Qual o preço do produto? "))
        frete = float(input("Qual o valor do frete? "))

        if saldocartao >= preco + frete:
            print("A compra é recomendada.")
        else:
            print("Saldo insuficiente para a compra.")
    else:
        print("O vendedor não é confiável.")
else:
    print("A compra não é recomendada.")

