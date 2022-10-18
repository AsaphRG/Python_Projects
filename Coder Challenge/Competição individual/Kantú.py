"""
Desafio 3: Império de Kantú

No império fictício de Kantú, o ano tem exatamente 360 dias e encontra-se dividido em 12 meses, cada um com exatos 30 dias. São eles: Yan, Feng, Maro, Abra, Mê, Yun, Yulu, Hago, Satur, Otobra, Navobra e Dodeca.

Cada dia, assim como os nossos, são compostos de 24 horas, sendo que cada hora tem 60 minutos e cada minuto, 60 segundos.

O imperador Jarg Ka-tûr incumbe seus melhores engenheiros, astrólogos e artesãos de uma desafiante tarefa: Construir uma enorme ampulheta que consiga marcar precisamente o tempo de um mês. É claro que produzir tal artigo não seria fácil e exigiria muitos cálculos e testes.

A ordem para a construção foi dada no dia 7 de Maro de 1533. O projeto teve início às 6h30 da manhã do dia seguinte e após exatos 437 dias a obra estava terminada.

No mesmo dia da finalização da construção houve uma grande festividade que durou até o dia seguinte, quando então a ampulheta foi posta em funcionamento tão logo as sombras desapareceram do chão, anunciando o meio-dia.

A gigantesca engenhoca era composta de 136,08 toneladas de areia e funcionou da seguinte forma:

·       A areia começou caindo em uma velocidade constante de 105 gramas por segundo (g/s);

·       Exatamente no momento em que restava metade da areia para cair, a velocidade de queda abruptamente foi para 35g/s e permaneceu nesse valor constante até o cair do último grão de areia;

Qual a exata data em que a última porção de areia terminou de cair?

Atenção: Escreva a data no formato [dia]/[nome do mês]/[ano]. Ex.: 04/Yan/1533

**Neste desafio 3 há alteração no enunciado a cada vez que ele é aberto.
"""
mesExt = ["Yan", "Feng", "Maro", "Abra", "Mê", "Yun", "Yulu", "Hago", "Satur", "Otobra", "Navobra", "Dodeca"]
diaInicio = 8 + 1  # Como o primeiro dia é o dia zero o dia 1 será apenas o dia seguinte, de modo que isso também precisa de um ajuste para que a data esteja correta
mesInicio = 3 - 1  # Esse é o mês 3, mas como o retorno do mês se dá por uma consulta à lista precisa que o valor seja adaptado
anoInicio = 1533
total = 0
total += anoInicio * 360 + mesInicio * 30 + diaInicio
total += 30  # A ampulheta foi feita para calcular exatamente um mês, que é o equivalente a 30 dias. O grande desafio do algoritmo não é calcular o tempo que passou, mas a formatação da data da forma correta
restoMes = total % 360
totalAno = total // 360
total -= 360 * totalAno
restoDia = total % 30
totalMes = total // 30
total -= 30 * totalMes
if restoDia + 1 < 10:
    print(f"0{restoDia}/{mesExt[totalMes]}/{totalAno}")
else:
    print(f"{restoDia}/{mesExt[totalMes]}/{totalAno}")
