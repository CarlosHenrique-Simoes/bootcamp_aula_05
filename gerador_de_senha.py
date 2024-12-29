import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Bem-vindo ao gerador de senhas!")

quantidade_letras = int(input("Quantas letras você quer em sua senha? "))
quantidade_numeros = int(input("Quantos números você quer em sua senha? "))
quantidade_simbolos = int(input("Quantos símbolos você quer em sua senha? "))

senha = ""

for _ in range(1,quantidade_letras + 1):
    senha += random.choice(letras)

for _ in range(1,quantidade_numeros + 1):
    senha += random.choice(numeros)

for _ in range(1,quantidade_simbolos + 1):
    senha += random.choice(simbolos)

print(senha)

senha_em_lista = []

for _ in range(1, quantidade_letras + 1):
    senha_em_lista.append(random.choice(letras))

for _ in range(1, quantidade_numeros + 1):
    senha_em_lista.append(random.choice(numeros))

for _ in range(1, quantidade_simbolos + 1):
    senha_em_lista.append(random.choice(simbolos))

print(senha_em_lista)

random.shuffle(senha_em_lista)

print(senha_em_lista)

senha = ""

for _ in senha_em_lista:
    senha += _

print(f"Sua senha gerada é: {senha}")