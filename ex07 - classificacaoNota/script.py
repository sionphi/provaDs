notaFinal = float(input("Digite sua nota final: (0-10) "))

if notaFinal >= 7:
    print("Aprovado")
elif notaFinal >= 5 and notaFinal < 7:
    print("Recuperação")
else:
    print("Reprovado")