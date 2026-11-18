# Neighborhood Action Dashboard

## Sistema de Gerenciamento de Ocorrências Comunitárias

**Projeto Acadêmico — FIAP**

**Aluno:** Leonardo Bezerra Lima 
**RM:** 575051
**Curso:** Ciências da Computação 
**Global Solution:** 2º Semestre de 2026
**Equipe:** Desenvolvimento individual
## 1. Objetivo

O Neighborhood Action Dashboard é um sistema desenvolvido em Python para organizar, consultar e gerenciar ocorrências comunitárias.

O projeto busca facilitar o acompanhamento de problemas urbanos relacionados à iluminação, limpeza, acessibilidade e conservação de espaços públicos.

## 2. Funcionalidades

O sistema possui as seguintes funcionalidades:

- Listagem de ocorrências cadastradas.
- Busca de ocorrências por identificação.
- Filtros por categoria e status.
- Atualização do status das ocorrências.
- Cálculo de estatísticas e percentuais.
- Histórico de atualizações.
- Fila de atendimento para ocorrências abertas.
- Validação de registros e identificação de dados incompletos.

## 3. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Estruturas de dados: listas, dicionários e filas.
- Funções, condicionais e estruturas de repetição.

## 4. Organização do projeto

**src/ocorrencias.py:** contém os dados das ocorrências e as funções responsáveis pelo gerenciamento, validação, filtros, estatísticas e fila de atendimento.

**src/sistema.py:** contém o menu principal que permite acessar as funcionalidades.

**data/:** diretório reservado para dados.

**docs/:** diretório reservado para documentação.

## 5. Como executar

Com o Python instalado, abra um terminal na pasta principal do projeto.

Execute o comando:

`python src/sistema.py`

O programa apresentará um menu interativo com as funcionalidades disponíveis.

Digite o número correspondente à opção desejada.

Para encerrar o programa, escolha a opção `0`.

## 6. Validação dos dados

O sistema contém 12 registros de exemplo, sendo 11 válidos e 1 inválido.

A ocorrência OC011 possui uma categoria vazia, permitindo demonstrar a identificação de registros incompletos.

As estatísticas utilizam os registros válidos.

## 7. Testes realizados

Foram realizados testes das funcionalidades de listagem, busca, filtros, atualização de status, estatísticas, histórico, fila de atendimento e encerramento do programa.

Os testes confirmaram o funcionamento das opções principais do menu.

## 8. Considerações finais

O projeto demonstra a aplicação de conceitos fundamentais de programação e estruturas de dados na resolução de problemas relacionados à gestão comunitária.

A solução utiliza funções independentes e um menu interativo para organizar as operações do sistema. 

## 9. Estruturas de Dados Utilizadas

O projeto utiliza diferentes estruturas de dados para organizar e consultar as ocorrências comunitárias.

**Lista:** armazena as ocorrências cadastradas, permitindo percorrer e analisar os registros.

**Dicionário:** organiza as ocorrências por identificador, facilitando a consulta de informações específicas.

**Fila (FIFO):** organiza as ocorrências abertas e válidas, seguindo a ordem de registro. FIFO significa *First In, First Out*, ou seja, primeiro a entrar, primeiro a sair.

**Pilha (LIFO):** permite consultar as últimas atualizações do histórico, apresentando os eventos na ordem inversa de inserção. LIFO significa *Last In, First Out*, ou seja, último a entrar, primeiro a sair.

**Hierarquia:** organiza os registros em três níveis: bairro simulado, categoria e ocorrências.

**Matriz:** utiliza uma lista de listas para representar as quantidades de ocorrências por categoria e status. 

## 10. Regras Lógicas e Validações

O sistema utiliza operadores booleanos e estruturas condicionais para validar os registros e controlar as operações.

**Operador AND (E):**

Utilizado para verificar se uma ocorrência é válida e está com status "Aberta" antes de incluí-la na fila de atendimento.

Exemplo em Python:

`if validar_ocorrencia(ocorrencia) and ocorrencia["status"] == "Aberta":`

As duas condições precisam ser verdadeiras.

**Operador OR (OU):**

Utilizado para identificar pendências. Uma ocorrência é considerada pendente quando seu status é "Aberta" ou "Em analise".

Exemplo:

`if status == "Aberta" or status == "Em analise":`

Basta uma das condições ser verdadeira.

**Operador NOT (NÃO):**

Utilizado para identificar registros inválidos e impedir determinadas operações.

Exemplo:

`if not validar_ocorrencia(ocorrencia):`

O operador NOT inverte o resultado da validação.

**Estruturas IF, ELIF e ELSE:**

São utilizadas no menu principal e nas regras do sistema para verificar entradas, executar funcionalidades e apresentar mensagens quando uma opção não é reconhecida.

As validações também impedem o cadastro de códigos duplicados, categorias desconhecidas e registros com campos obrigatórios vazios. 

## 11. Indicadores e Análise dos Resultados

O Neighborhood Action Dashboard apresenta indicadores calculados a partir das ocorrências válidas cadastradas no sistema.

### Quantidade de ocorrências

O conjunto inicial possui 12 ocorrências simuladas, sendo 11 válidas e 1 inválida (OC011), devido à ausência de categoria.

### Quantidade por categoria

- Iluminação: 3 ocorrências.
- Limpeza: 3 ocorrências.
- Conservação: 3 ocorrências.
- Acessibilidade: 2 ocorrências.

### Quantidade por status

- Aberta: 5 ocorrências.
- Em análise: 4 ocorrências.
- Concluída: 2 ocorrências.

### Fórmula dos percentuais

Percentual = (Quantidade da categoria ou status / Total de ocorrências válidas) × 100

Por exemplo, o percentual de ocorrências abertas é:

(5 / 11) × 100 = 45,45%

### Indicador adicional de pendências

São consideradas pendentes as ocorrências com status "Aberta" ou "Em analise".

Quantidade de pendências = 5 + 4 = 9

Percentual de pendências = (9 / 11) × 100 = 81,82%

### Interpretação dos resultados

Os dados simulados mostram que 81,82% das ocorrências válidas ainda precisam de acompanhamento. 

## 12. Acessibilidade, Inclusão e Privacidade

O Neighborhood Action Dashboard foi desenvolvido considerando princípios de acessibilidade, inclusão e responsabilidade no uso da tecnologia.

### Acessibilidade

O sistema utiliza uma interface textual com opções numeradas e mensagens que identificam as operações realizadas.

A organização do menu busca facilitar a compreensão das funcionalidades, embora ainda existam limitações de acessibilidade que podem ser melhoradas em versões futuras.

### Inclusão

O projeto contempla quatro categorias de demandas comunitárias: iluminação, limpeza, conservação e acessibilidade.

A categoria Acessibilidade permite representar problemas como calçadas sem rampas e pisos irregulares, que podem dificultar a circulação de pessoas com deficiência ou mobilidade reduzida.

### Privacidade

Todos os registros utilizados na demonstração são fictícios.

O sistema não exige nomes, documentos, telefones ou outros dados pessoais dos moradores.

Também não realiza integração com órgãos públicos ou serviços externos.

### Limitações do projeto

O programa é um protótipo acadêmico desenvolvido em Python, utilizando uma interface de terminal.

As informações são armazenadas em estruturas de dados durante a execução. Novos cadastros e alterações de status não são preservados automaticamente após o encerramento do programa.

O sistema não garante o atendimento real das demandas comunitárias.

Melhorias futuras

Como possíveis melhorias, destacam-se o armazenamento permanente dos registros, uma interface mais acessível, novos filtros e recursos adicionais para acompanhamento das solicitações. 

## 13. Exemplos de Utilização

O sistema possui um menu interativo que permite executar as funcionalidades por meio de opções numeradas.

### Exemplo 1 — Cadastrar uma ocorrência

**Opção do menu:** 9

Dados informados:

- Código: OC013
- Categoria: Limpeza
- Descrição: Lixo acumulado
- Local: Rua Nova
- Data de abertura: 18/11/2026

**Resultado esperado:** ocorrência cadastrada com sucesso e status inicial definido como "Aberta".

### Exemplo 2 — Consultar uma ocorrência

**Opção do menu:** 2

Código informado: OC001

O sistema apresenta o identificador, a categoria, a descrição, o local, a data de abertura e o status da ocorrência.

### Exemplo 3 — Atualizar o status

**Opção do menu:** 5

Código informado: OC001

Novo status: Em analise

O sistema atualiza a situação da ocorrência e registra a alteração no histórico durante a execução.

### Exemplo 4 — Consultar indicadores

**Opção do menu:** 6

O sistema apresenta a quantidade e os percentuais de ocorrências válidas por categoria e situação.

A opção 13 apresenta o indicador adicional de pendências.

Exemplo 5 — Encerrar o sistema

Opção do menu: 0

O programa apresenta a mensagem:

"Encerrando o sistema. Ate logo!"

Observação: os cadastros e as alterações efetuadas durante os exemplos não são armazenados permanentemente após o encerramento do programa. 

## 14. Conclusões e Aprendizados
O desenvolvimento do Neighborhood Action Dashboard permitiu aplicar conhecimentos fundamentais das primeiras fases do curso de Ciências da Computação da FIAP.

O projeto demonstrou a utilização de funções, variáveis, estruturas condicionais, laços de repetição, listas, filas, pilhas, dicionários, hierarquias e matrizes.

Também foram desenvolvidas funcionalidades de cadastro, consulta, atualização de status, validação de dados e cálculo de indicadores.

Durante o desenvolvimento, foram realizados testes para identificar e corrigir erros de sintaxe, problemas de validação e falhas de integração entre módulos Python.

Os indicadores obtidos a partir dos dados simulados demonstram como a programação pode contribuir para organizar informações sobre demandas comunitárias.

Como aprendizado, destaca-se a importância de dividir um problema em etapas, testar cada funcionalidade e documentar as decisões técnicas.

O sistema representa um protótipo acadêmico e poderá receber melhorias futuras, como armazenamento permanente das informações e recursos adicionais de acessibilidade.

## 15. Comunidade Simulada

O projeto representa uma comunidade ficticia chamada Bairro Modelo.

A comunidade apresenta demandas relacionadas a iluminacao publica, limpeza, acessibilidade e conservacao de espacos coletivos.

O sistema busca organizar esses problemas e permitir o acompanhamento das ocorrencias registradas.

O publico beneficiado seria composto por moradores, representantes comunitarios e pessoas interessadas em acompanhar melhorias na infraestrutura local.

Todos os dados utilizados sao ficticios, sem identificacao pessoal de moradores.

## 16. Video de Apresentacao

Link do video no YouTube: A inserir apos a gravacao.

O video demonstrara o funcionamento do sistema, suas principais funcionalidades, estruturas de dados, validacoes e indicadores.

