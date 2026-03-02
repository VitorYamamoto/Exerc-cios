lado1 = float(input("Digite um dos lados do triângulo: "))
lado2 = float(input("Digite um dos lados do triângulo: "))
lado3 = float(input("Digite um dos lados do triângulo: "))
if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("Triângulo escaleno")
    elif lado1 == lado2 and lado2 == lado3:
        print("Triângulo equilátero.")
    else:
        print("Triângulo isóceles")
