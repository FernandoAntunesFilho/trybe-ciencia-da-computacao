def triangulo(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        if (a == b) and (b == c):
            return "Triângulo Equilátero"
        elif (a == b) or (b == c) or (c == a):
            return "Triângulo Isóceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é Triângulo"


print(triangulo(5, 11, 11))
