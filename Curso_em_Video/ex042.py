b = float(input('Insira a base: '))
h = float(input('Insira a altura: '))
hip = float(input('Insira a hipotenusa: '))
if b < h + hip and h < b + hip and hip < h + b:
    if b == h == hip:
        print('Esse é um triângulo equilátero.')
    elif b == h or b == hip or h == b or h == hip or hip == b or hip == h:
        print('Este é um triângulo isósceles.')
    else:
        print('Este é um triângulo escaleno.')
else:
    print('Não é possível fazer um triângulo com essas medidas.')
