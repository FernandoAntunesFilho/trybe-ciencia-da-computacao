def custo_pintura(tamanho_da_parede):
    litros = tamanho_da_parede / 3
    latas = litros / 18
    return (latas, latas * 80.00)


print(custo_pintura(108))
