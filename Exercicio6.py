numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o multiplicador inicial: "))
fim = int(input("Digite o multiplicador final: "))

if inicio > fim:
    print("Intervalo inválido: o início deve ser menor ou igual ao fim.")
else:
    print(f"\n-- TABUADA DO {numero} --")
    
    for multiplicador in range(inicio, fim + 1):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
