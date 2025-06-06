📄 Descrição do Projeto
Este projeto em Python é uma ferramenta de Análise de Dados desenvolvida para auxiliar empresas de marketing a identificar e segmentar seu público-alvo para campanhas de e-mail marketing. O objetivo principal é determinar, com base em critérios como idade e classe social, quais indivíduos são elegíveis para receber e-mails específicos (por exemplo, marketing de bebidas alcoólicas, brinquedos ou passagens aéreas).
Utilizando a biblioteca NumPy, o programa permite uma análise eficiente dos dados, fornecendo resultados claros sobre a permissão de envio de e-mails para diferentes segmentos de clientes.

🚀 Funcionalidades
O programa oferece um menu interativo com as seguintes opções de análise:

Exibir Dados Gerais Carregados: Mostra um panorama completo dos dados de clientes, incluindo nomes, idades, classes sociais, contagem total de registros, idade máxima e mínima.
Análise para E-mail Marketing de Álcool: Verifica quais clientes têm idade superior a 18 anos, tornando-os elegíveis para campanhas de bebidas alcoólicas.
Análise para E-mail Marketing de Brinquedos: Identifica clientes com idade igual ou inferior a 12 anos, adequados para campanhas de brinquedos.
Análise para E-mail Marketing de Passagens de Avião: Segmenta clientes com idade igual ou superior a 22 anos e que pertencem às classes sociais "a", "b" ou "c", consideradas público-alvo para passagens aéreas. Lista os nomes dos clientes elegíveis.

💻 Tecnologias Utilizadas
Python: Linguagem de programação principal.
NumPy: Biblioteca fundamental para computação numérica e manipulação eficiente de arrays de dados.
Sistema Operacional: Funcionalidades de limpeza de tela (os.system('clear'/'cls')) para uma melhor experiência de usuário no terminal.

⚙️ Como Rodar o Projeto
Siga os passos abaixo para clonar o repositório e executar o programa em sua máquina:

Clone o Repositório:
Abra seu terminal ou prompt de comando e execute:
git clone https://github.com/PortilloGacp/Analise-de-dados-Marketing.git

Navegue até o Diretório do Projeto:
cd Analise-de-dados-Marketing

Instale as Dependências:
pip install numpy

Execute o Programa:
python Analise.py
