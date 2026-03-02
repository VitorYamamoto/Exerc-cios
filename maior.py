num = int(input("Digite um número: "))
maior = num
for cont in range (0, 2):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num 
print(f"O maior número é {maior}")