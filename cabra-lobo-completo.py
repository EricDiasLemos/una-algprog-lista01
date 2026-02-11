cabra = "cabra"
lobo = "lobo"
couve = "couve"
riolado1 = [cabra,lobo,couve]
riolado2 = []
itens = 0

"Se o lobo ficar sozinho com a cabra ela morre"
"Se a cabra ficar sozinha com a couve ela come a couve"
"A couve pode ficar sozinha com o lobo sem problemas"

print("Rio lado 1:",riolado1)
print("Rio lado 2:",riolado2)

print("leva a cabra")
riolado1.remove(cabra)
riolado2.append(cabra)

print("leva o lobo e trás a cabra")
riolado1.remove(lobo)
riolado2.append(lobo)
riolado2.remove(cabra)
riolado1.append(cabra)

print("leva a couve")
riolado1.remove(couve)  
riolado2.append(couve)

print("leva a cabra")
riolado1.remove(cabra)
riolado2.append(cabra)

print("Rio lado 1:",riolado1)
print("Rio lado 2:",riolado2)


