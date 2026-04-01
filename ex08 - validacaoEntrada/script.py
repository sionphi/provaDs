idade = int(input("Digite sua idade: "))
tensDocumento = bool(input("Tem documento: "))
estaAcompanhado = bool(input("Está acompanhado: "))

if idade >= 18 and tensDocumento == True or estaAcompanhado == True:
    print("Entrada permitida")
else:
    print("Entrada Negada!")