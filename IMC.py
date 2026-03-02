kg = float(input("Digite seu peso em KG: "))
altura = float(input("Digite a sua altura em metros: "))
imc = kg / altura ** 2
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")