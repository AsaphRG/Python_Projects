# DuckSystems
Essa é uma CRUD para controle de contatos, obras e funcionarios feita para o DSIN Coder Challenge.
O sistema foi desenvolvido totalmente em Python e utilizei os módulos pyodbc, pandas, colorama e os.
Junto com os arquivos há um backup do banco de dados que utilizamos no sistema.

Como o tempo era curto acabei optando por trabalhar de forma estruturada porque tenho pouca experiência com POO e isso me exigiria uma modelagem maior do projeto.

Esse é o enunciado do desafio proposto pela DSIN.

Desafio
Após muitos anos de trabalho duro como pedreiro, nosso amigo Pato percebeu que já tinha passado da hora de tentar subir mais um degrau em sua vida profissional. Queria ser o primeiro pato futebolista, mas seus planos foram frustrados pela ascensão de Alexandre Pato; então, resolveu que seria o primeiro pedreiro futebolista, mas seus sonhos foram por água abaixo com o aparecimento e o sucesso do Luva de Pedreiro. Sem saber que outro rumo tomar, resolveu usar seus anos de experiência para abrir um novo negócio: uma pequena construtora. Em pouco tempo ele já contava com 10 funcionários, sendo: três pedreiros, cinco serventes, um serralheiro e mais um funcionário no setor administrativo.
Embora não fosse nenhum pato-aranha, sua trajetória empresarial teve um início próspero. Porém, como lhe disse certa vez seu tio, Benjamin Parker Duck: “com grandes poderes vêm grandes responsabilidades”. Assim, nosso amigo logo descobriu que a vida de empresário não é nada fácil. Com o rápido crescimento da empresa, passou a enfrentar diversos problemas para entregar as obras contratadas dentro dos prazos acordados e com a qualidade esperada pelos clientes. Quando era sozinho, era fácil gerenciar tudo na sua caderneta de notas, mas agora, com tantos clientes e colaboradores, quase sempre se perdia e fazia confusões com suas anotações.
Em um jantar com seu amigo Mark McQuack - um grande especialista da área de TI e cocriador das ferramentas Ducker (gerenciamento de contêineres) e do famoso buscador VaiPatoVai! -, Duck confidenciou seus problemas na condução da empresa. Mark sugeriu a Duck que buscasse a construção de um software que pudesse apoiar na gestão da empresa, aproveitando-se do fato de que nossa região é um polo tecnológico.
Duck, animado com a perspectiva de melhora na entrega de suas obras, entrou em contato com um time de TI. Ele então relatou suas principais dificuldades (abaixo), solicitando a construção de ferramentas que poderiam transformar sua empresa (e sua vida).

Principais dificuldades relatadas:
1 – Duck utiliza uma caderneta para anotar todos os detalhes de seu negócio, sendo majoritariamente utilizada para anotar os contatos dos fornecedores, parceiros e funcionários que trabalham em suas obras. Porém, na última sexta-feira, após o tradicional “churrasco da laje”, sua caderneta desapareceu, levando consigo todos os dados de contatos. Agora, será necessário refazer todo o trabalho. Duck busca modernizar e organizar melhor seus contatos além de utilizar uma solução mais segura que não tenha risco de perda dos dados;

2 – Outra grande dificuldade relatada está em estimar o tempo de duração de uma obra. Por instinto (e fazendo uso de sua longa experiência), ele tem as seguintes informações:
• Quanto maior a metragem da obra, mais tempo ela leva para ser finalizada. Em sua última entrega, trabalhando com um pedreiro e dois serventes, uma obra de 150 m² levou 8 meses para ser entregue;
• A chuva é um fator que influencia muito o tempo de entrega, principalmente em obras que têm início em meses com maior incidência de chuva, pois sempre existe uma demora maior até a fase da cobertura da laje;
• Obras assobradadas levam em torno de 30% a mais de tempo e 20% a mais de material do que obras térreas.

3 – Com o aumento da empresa, Duck percebeu que sua margem de lucro tem sido cada vez menor. Ele gostaria de retomar os 40% de lucro que obtinha na época que trabalhava em apenas uma obra.
• Atualmente os pedreiros recebem R$ 190,00 a diária, enquanto os serventes recebem R$ 95,00. Seu funcionário administrativo recebe dois salários mínimos por mês;
• Além dos custos com os seus funcionários, existe ainda o custo adicional de 10% a 15% com outros prestadores de serviços, como: pintor, eletricista, encanador, gesseiro, etc.

4 – Outro desejo de Duck seria estimular os melhores e mais produtivos funcionários com uma bonificação.

