altura = float(input("Informe a altura em metros: "))
peso = float(input("Informe o peso em quilogramas: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Acima do peso")
else:
    print("Obeso")
