def m2(comp, lar):
    print(f"A área de um terreno de {comp}m x {lar}m é de {comp * lar}m².")


print("Controle de terrenos.")
print("-" * 30)
m2(float(input("Comprimento (m): ")), float(input("Largura (m): ")))
