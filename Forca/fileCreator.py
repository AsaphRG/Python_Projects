list = """cama; colchão; mesa de cabeceira; abajur; tapete; guarda-roupa; espelho; cômoda; sofá; poltrona; sofá-cama; rack; luminária; almofada; cadeira; aparador; fogão; geladeira; mesa; armário; cortina; persiana; lustre; quadro""".replace("; ", "; ")
txt = open("Móvel.txt", "w")
txt.write(list)
print(txt)
