import random

lista_de_palavras = []
with open("animais.txt", "r") as file:
    for animal in file:
        lista_de_palavras.append(animal.strip())


palavra_sorteada = random.choice(lista_de_palavras)
palavra_embaralhada = "".join(
    random.sample(palavra_sorteada, len(palavra_sorteada))
)

print("JOGO ADIVINHE A PALAVRA")
print("DICA:", lista_de_palavras)
print("Desembaralhe as letras:", palavra_embaralhada)

tentativas = 1
while tentativas <= 3:
    palavra_digitada = input("Adivinhe a palavra: ")
    palavra_digitada = palavra_digitada.upper()
    tentativas += 1
    if palavra_digitada == palavra_sorteada:
        print("Acertou!!!")
        break
    if tentativas > 3:
        print("Não foi desta vez... :(")
