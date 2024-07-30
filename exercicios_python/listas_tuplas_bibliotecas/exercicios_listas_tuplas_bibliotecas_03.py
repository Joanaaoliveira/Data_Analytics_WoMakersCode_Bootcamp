carrinho_compras = {
    'biscoito': {'valor': 2.75},
    'leite': {'valor': 4.25},
    'café': {'valor': 22.50}
}

def calcular_total(carrinho):
    total = 0
    for detalhes in carrinho.values():
        total += detalhes['valor']
    return total

print(f'O valor da sua compra é R${calcular_total(carrinho_compras):.2f}')