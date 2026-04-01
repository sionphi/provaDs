valorProduto = float(input("Digite o valor de seu produto: "))
descontoAplicado = int(input("Digite o desconto que foi dado: "))
valorDesconto = valorProduto * (descontoAplicado / 100)
valorFinal = valorProduto - valorDesconto

print(f"O valor final foi de {valorFinal:.2f}")