/*!
\page functions Página das Funções

# Página das Funções do Programa

Esta página apresenta uma visão geral das funções implementadas no
ficheiro **vector_operations.py**, indicando o seu papel no sistema de
operações com vetores e matrizes. A descrição detalhada de cada função
é gerada automaticamente a partir dos comentários Doxygen presentes no
código.

---

## Funções Principais

- **init_program()**  
  Função de entrada do programa. Trata da opção especial `--help`,
  recolhe o vetor inicial e gere o ciclo principal do menu, chamando as
  restantes funções conforme a opção escolhida pelo utilizador.

- **menu(numbers)**  
  Mostra o menu principal com todas as opções disponíveis para trabalhar
  sobre o vetor inicial e as matrizes associadas.

- **print_ajuda()**  
  Apresenta no ecrã a página de ajuda com texto formatado e informação
  sobre o propósito do menu, bem como um contacto fictício.

---

## Funções de Leitura e Validação

- **get_numbers_from_user(mensagem_inicial=None)**  
  Lê um conjunto de números inteiros fornecidos pelo utilizador, com
  validação do intervalo permitido. Pode receber uma mensagem inicial
  para diferenciar a leitura do vetor inicial da leitura de um novo
  vetor (opção 8).

---

## Funções de Operações sobre o Vetor

- **valor_mais_proximo(numbers, target=15)**  
  Determina o elemento do vetor cuja distância ao valor alvo (por
  defeito 15) é mínima.

- **cosseno_segunda_metade(numbers)**  
  Calcula o cosseno dos elementos que pertencem à segunda metade do
  vetor inicial.

- **ordernar_vector(numbers)**  
  Devolve uma nova lista com os elementos do vetor ordenados por ordem
  decrescente.

- **nao_divisiveis_por_tres(numbers)**  
  Filtra e devolve apenas os valores do vetor que não são divisíveis por
  3.

- **media_vetor(numbers)**  
  Calcula a média aritmética dos valores presentes no vetor.

- **soma_primeiro_com_dobro_segundo(numbers)**  
  Lê um novo vetor e calcula, posição a posição, a soma entre o valor do
  vetor inicial e o dobro do valor correspondente do novo vetor.

---

## Funções de Matrizes

- **matriz_2x10_quadruplo(numbers)**  
  Constrói uma matriz 2×10 em que a primeira linha é o vetor inicial e a
  segunda linha contém os mesmos valores multiplicados por 4.

- **mostrar_matriz(numbers)**  
  Imprime no ecrã uma matriz (lista de listas) com formatação tabular,
  facilitando a leitura dos valores.

- **produto_com_ordem_crescente(numbers)**  
  Gera uma matriz 10×10 a partir do produto entre cada elemento do vetor
  inicial e todos os elementos do mesmo vetor ordenado por ordem
  crescente.

- **transposta(matriz_10_x_10)**  
  Calcula e devolve a transposta de uma matriz 10×10 representada como
  lista de listas.

---

## Funções de Números Compostos

- **check_composto(number)**  
  Verifica se um número é composto, testando se possui algum divisor
  além de 1 e dele próprio.

- **elementos_compostos_vector(numbers)**  
  Percorre o vetor e devolve uma lista apenas com os elementos que são
  classificados como compostos pela função `check_composto()`.

---

*/