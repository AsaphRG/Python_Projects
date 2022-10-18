print('Esse triângulo é possível?  Vamos conferir!')
b = float(input('Me diga a base: '))
h = float(input('Me diga a altura: '))
hip = float(input('Me diga a hipotenusa: '))
if b < h + hip and h < b + hip and hip < h + b:
    print('Esse triângulo pode ser formado.')
else:
    print('Esse triângulo não pode ser formado.')
