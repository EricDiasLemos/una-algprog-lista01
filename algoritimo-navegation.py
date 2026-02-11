print("Bem-vindo ao Algoritimo de Navegação!")

novoeldorado = int(input("Qual a distancia da Estação Novo Eldorado: (em metros)"))

if novoeldorado >= 1000:

        print("Tendo em vista a distancia maior que 1 KM, é melhor ir de carro.")

else:
    chuva = input("Está chovendo? (S/N) ")
    chuva = chuva.upper()  # Convertendo a resposta para maiúscula para evitar erros de digitação

    if chuva == "S":
        print("Mesmo a distancia sendo menor que 1 KM, com a chuva é melhor ir de carro.")

    else:    
        print("Tendo em vista a distancia sendo", novoeldorado, "metros, é melhor ir a pé.")







