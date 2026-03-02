x = int(input("Digite a coordenada de X: "))
y = int(input("Digite a coordenada de y: "))

if x > 0 and y > 0:
    print("Quadrante 1")
elif x < 0 and y > 0:
    print("Quadrante 2")
elif x > 0 and y < 0:
    print("Quadrante 4")
elif x < 0 and y < 0:
    print("Quadrante 3")
else:
    print("Eixo")
