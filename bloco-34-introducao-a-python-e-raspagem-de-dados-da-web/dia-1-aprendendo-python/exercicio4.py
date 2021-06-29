nomes = ["José", "Lucas", "Nádia", "Fernando", "Cairo", "Joana"]
maior_nome = ""


for nome in nomes:
    if len(nome) > len(maior_nome):
        maior_nome = nome
print(maior_nome)
