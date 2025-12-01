##
# @file vector_operations.py
# @brief Programa interativo para processamento de vetores e matrizes.
#
# @details Este programa permite ao utilizador introduzir um conjunto de valores
#          inteiros e executar várias operações, incluindo cálculo de medidas,
#          transformações do vetor, geração de matrizes e operações de produto
#          e transposição. O menu apresentado ao utilizador organiza todas as
#          funcionalidades disponíveis, incluindo uma opção de ajuda adicional.
#
# @author Grupo 1
# @date Novembro 2025

##
# @brief Apresenta o menu principal de operações ao utilizador.
#
# @details Esta função mostra todas as opções disponíveis para manipulação
#          do vetor previamente introduzido, bem como operações adicionais
#          sobre matrizes. Limita-se a imprimir o menu no ecrã, sem executar
#          qualquer operação, permitindo que o utilizador selecione a ação
#          pretendida.
#
# @param numbers Vetor introduzido pelo utilizador, mostrado no cabeçalho do menu.
# @return Não devolve valores; apenas imprime o menu.

import sys
import math

def menu(numbers):
    print(f"\nMenu: {numbers}")
    print('1 - Determinação do elemento mais próximo de 15')
    print('2 - Cálculo do cosseno da segunda metade do vetor')
    print('3 - Reordenamento do vetor por ordem decrescente')
    print('4 - Extração dos valores que não são divisíveis por três')
    print('5 - Construção de uma matriz 2x10 com o quádruplo dos valores')
    print('6 - Cálculo da média do vetor')

    # 1 - Leitura de um novo vetor, cálculo e devolução da soma do primeiro vetor com o dobro do segundo;
    print('7 - Ajuda adicional')
    print('8 - Leitura de um novo vetor e soma com o dobro dos seus valores ao vetor inicial')
    print('9 - Números compostos no vetor inicial')
    print('10 - Matriz 10x10 do produto entre o vetor inicial e o mesmo vetor ordenado')
    print('11 - Matriz 10x10 transposta (da matriz de produtos)')
    print('0 - Terminar o programa')

##
# @brief Lê um conjunto de números inteiros inseridos pelo utilizador.
#
# @details Esta função solicita ao utilizador que introduza um número
#          fixo de valores inteiros (entre -10 e 27). Cada valor é
#          validado individualmente; se estiver fora do intervalo ou
#          não for inteiro, é pedido novamente. Caso seja fornecida
#          uma mensagem inicial, esta é exibida antes da leitura dos
#          números, permitindo diferenciar a leitura do vetor inicial
#          da leitura de um novo vetor na opção 8.
#
# @param mensagem_inicial Mensagem opcional apresentada antes da leitura
#        dos números (utilizada, por exemplo, na opção 8).
#
# @return Lista contendo todos os valores válidos introduzidos pelo utilizador.

def get_numbers_from_user(mensagem_inicial=None):
    min_accepted_value = -10
    max_accepted_value = 27
    max_vector_size = 10
    numbers = []

    # Mensagem opcional (diferente para vetor inicial / novo vetor)
    if mensagem_inicial is not None:
        print("\n" + mensagem_inicial)
        print(f"Vamos ler {max_vector_size} números inteiros "
              f"entre {min_accepted_value} e {max_accepted_value}.\n")

    while len(numbers) < max_vector_size:
        try:
            inserted_number = int(input(
                f"Insira o número inteiro {len(numbers)+1} de {max_vector_size} "
                f"(entre {min_accepted_value} e {max_accepted_value}): "
            ))

            if min_accepted_value <= inserted_number <= max_accepted_value:
                numbers.append(inserted_number)
            else:
                print(f"O valor deve estar entre {min_accepted_value} e {max_accepted_value}.")
        except ValueError:
            print("Entrada inválida! Tente novamente.")

    return numbers

##
# @brief Determina o valor do vetor que está mais próximo do alvo indicado.
#
# @details A função percorre todos os elementos do vetor e calcula a diferença
#          absoluta entre cada valor e o alvo (`target`). O elemento cuja
#          diferença for menor é considerado o mais próximo. O valor por defeito
#          do alvo é 15, mas pode ser alterado se necessário.
#
# @param numbers Vetor de números inteiros onde será feita a pesquisa.
# @param target Valor de referência para o qual se procura o elemento mais próximo.
# @return O valor do vetor cuja distância ao alvo é mínima.

def valor_mais_proximo(numbers, target=15):
    menor_diferenca = float('inf') # cria um valor que representa infinito positivo em Python
    valor_mais_proximo = None

    for number in numbers:
        diferenca = abs(number - target)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            valor_mais_proximo = number
    
    return valor_mais_proximo

    # forma mais simplificada de fazer isso
    #return min(numbers, key=lambda number: abs(number-target))

##
# @brief Calcula o cosseno dos valores presentes na segunda metade do vetor.
#
# @details A função divide o vetor ao meio e seleciona apenas os elementos da
#          segunda metade. Em seguida, aplica a função matemática cosseno a cada
#          um desses valores, devolvendo um novo vetor com os resultados.
#
# @param numbers Vetor de números inteiros sobre o qual será aplicado o cálculo.
# @return Um vetor contendo os valores do cosseno da segunda metade do vetor inicial.

def cosseno_segunda_metade(numbers):
    # Calcular o index da segunda metade
    metade_index = len(numbers) // 2

    # Criar um array dos numeros da segunda metade
    segunda_metade_vector = numbers[metade_index:]

    # calcular o cosseno de cada elemento da segunda metade do array
    return [math.cos(number) for number in segunda_metade_vector]

##
# @brief Ordena o vetor por ordem decrescente.
#
# @details A função recebe um vetor de números e devolve uma nova lista com
#          os mesmos elementos, mas organizada por ordem decrescente, usando
#          a função interna `sorted(vetor, reverse=True)` do Python.
#
# @param numbers Vetor de números a ser ordenado.
# @return Uma nova lista com os valores ordenados de forma decrescente.

def ordernar_vector(numbers):
    return sorted(numbers, reverse=True)

##
# @brief Filtra os valores do vetor que não são divisíveis por três.
#
# @details A função percorre todos os elementos do vetor e seleciona apenas
#          aqueles cujo resto da divisão por três é diferente de zero. O resultado
#          é devolvido como um novo vetor.
#
# @param numbers Vetor de números inteiros a analisar.
# @return Um novo vetor contendo apenas os valores que não são divisíveis por três.

def nao_divisiveis_por_tres(numbers):
    # results = []

    # for number in numbers:
    #     if number % 3 != 0:
    #         results.append(number)
    # return results

    # podes fazer de outra forma:
    return [number for number in numbers if number % 3 != 0]

##
# @brief Constrói uma matriz 2x10 com os valores originais e quadruplicados.
#
# @details A função cria uma matriz com duas linhas e dez colunas. A primeira
#          linha contém os valores originais do vetor fornecido, enquanto a
#          segunda linha contém os mesmos valores multiplicados por quatro.
#
# @param numbers Vetor de dez números inteiros usado para construir a matriz.
# @return Uma matriz 2x10 onde a primeira linha são os valores originais
#         e a segunda linha os valores quadruplicados.

def matriz_2x10_quadruplo(numbers):
    result = []
    for i in range(2):
        result.append([])
        for f in range(10):

            # result[i].append(numbers[f] if i == 0 else numbers[f] * 4)
            if i == 0:
                result[i].append(numbers[f])
            else:
                result[i].append(numbers[f] * 4)
            
    return result

##
# @brief Mostra uma matriz no ecrã de forma formatada.
#
# @details A função percorre cada linha da matriz recebida e imprime os seus
#          elementos separados por tabulação, facilitando a leitura visual da
#          estrutura em forma de tabela.
#
# @param numbers Matriz (lista de listas) a ser apresentada no ecrã.
# @return Não devolve valores; apenas imprime a matriz.

def mostrar_matriz(numbers):
    for linha in numbers:
        print(' '.join(f"{number:6}" for number in linha))

##
# @brief Calcula a média dos valores do vetor.
#
# @details A função soma todos os elementos do vetor e divide o resultado
#          pelo número total de valores, devolvendo a média aritmética.
#
# @param numbers Vetor de números inteiros ou reais.
# @return A média aritmética dos valores do vetor.

def media_vetor(numbers):
    return sum(numbers) / len(numbers)

##
# @brief Soma cada elemento do vetor inicial com o dobro dos elementos de um novo vetor.
#
# @details A função solicita ao utilizador um segundo vetor com o mesmo tamanho
#          através de `get_numbers_from_user()`. Em seguida, combina os dois
#          vetores elemento a elemento, somando cada valor do vetor inicial com
#          o dobro do valor correspondente do segundo vetor. A operação é feita
#          utilizando a função `zip()` para emparelhar os elementos.
#
# @param numbers Vetor inicial previamente introduzido pelo utilizador.
# @return Um novo vetor resultante da operação: elemento_inicial + 2 × elemento_novo.

def soma_primeiro_com_dobro_segundo(numbers):
    print('\n[8] Leitura de um NOVO vetor para somar com o vetor inicial...')

    numbers_2 = get_numbers_from_user(
        "Agora vamos ler um NOVO vetor.\n"
        "Este vetor será usado apenas para calcular a soma com o dobro dos seus valores "
        "em relação ao vetor inicial."
    )

    result = [el1 + (el2 * 2) for el1, el2 in zip(numbers, numbers_2)]

    return numbers_2, result


##
# @brief Verifica se um número é composto.
#
# @details A função considera que apenas números maiores ou iguais a 2
#          podem ser compostos. Em seguida, testa se o número possui
#          algum divisor além de 1 e dele próprio. Caso exista um divisor,
#          o número é classificado como composto; caso contrário, é primo.
#
# @param number Número inteiro a ser analisado.
# @return True se o número for composto; False caso contrário.

def check_composto(number):
    # Números menores que 2 não são compostos
    if number < 2:
        return False

    # Verificar se o número tem algum divisor além de 1 e dele próprio
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True  # Encontrou divisor → é composto

    return False  # Não encontrou nenhum divisor → é primo

##
# @brief Devolve todos os números compostos presentes no vetor.
#
# @details A função percorre o vetor recebido e utiliza `check_composto()`
#          para determinar quais elementos são compostos. Apenas os valores
#          classificados como compostos são incluídos no vetor resultante.
#
# @param numbers Vetor de números inteiros a analisar.
# @return Um novo vetor contendo apenas os números compostos encontrados.

def elementos_compostos_vector(numbers):
    return [number for number in numbers if check_composto(number)]

##
# @brief Gera uma matriz 10x10 com o produto entre cada valor do vetor e o vetor ordenado.
#
# @details A função ordena o vetor recebido por ordem crescente e, para cada
#          elemento do vetor original, calcula o produto com todos os elementos
#          do vetor ordenado. O resultado é organizado numa matriz 10x10,
#          onde cada linha corresponde a um valor original multiplicado por
#          todos os valores ordenados.
#
# @param numbers Vetor inicial de números inteiros.
# @return Uma matriz 10x10 resultante dos produtos entre o vetor original e o vetor ordenado.

def produto_com_ordem_crescente(numbers):
    matriz_10_x_10 = []
    numbers_sorted = sorted(numbers)

    for number in numbers:
        matriz_10_x_10.append([number * number_sorted for number_sorted in numbers_sorted])
    
    return matriz_10_x_10

##
# @brief Gera a transposta de uma matriz.
#
# @details A função recebe uma matriz representada como uma lista de listas
#          e utiliza `zip()` para agrupar os elementos por coluna. Cada grupo
#          é convertido novamente para lista, formando assim a matriz transposta.
#
# @param matriz_10_x_10 Matriz que se pretende transpor.
# @return Uma nova matriz correspondente à transposta da matriz dada.

def transposta(matriz_10_x_10):
    return [list(linha) for linha in zip(*matriz_10_x_10)]

##
# @brief Mostra a página de ajuda do menu principal.
#
# @details Esta função imprime um pequeno texto explicativo sobre
#          o propósito do menu, descrevendo de forma breve que cada
#          opção corresponde a uma operação diferente realizada sobre
#          o vetor introduzido pelo utilizador. Inclui também uma nota
#          final com um contacto fictício para dúvidas ou informação.
#
# @return Não devolve valores; apenas apresenta texto formatado no ecrã.

def print_ajuda():
    print(r"""
══════════════════════════════════════════════════════
                        AJUDA
══════════════════════════════════════════════════════

Este menu serve como ponto central para todas as operações
do programa. Através das opções disponíveis, é possível
aplicar cálculos, transformar o vetor ou produzir matrizes
derivadas dos valores introduzidos. Cada seleção executa a
função correspondente e devolve o menu para nova escolha.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Em caso de dúvidas ou necessidade de mais informações, 
contacte: grupo1@ubi.pt
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

##
# @brief Inicia o programa e gere o ciclo principal do menu.
#
# @details Esta função trata do caso especial em que o programa é executado
#          com a flag '--help', mostrando a página de ajuda. Caso contrário,
#          lê inicialmente um vetor de números inteiros fornecido pelo
#          utilizador e entra num ciclo em que apresenta o menu principal,
#          lê a opção escolhida e chama a função correspondente. As operações
#          incluem cálculos sobre o vetor inicial, criação de matrizes 2x10
#          e 10x10, geração da transposta e leitura de um segundo vetor para
#          a soma com o dobro dos seus valores. O ciclo termina quando o
#          utilizador seleciona a opção 0.
#
# @return Não devolve valores; coordena apenas a execução das restantes funções.

def init_program():

    if '--help' in sys.argv:
        print(r"""
══════════════════════════════════════════════════════
                        AJUDA
══════════════════════════════════════════════════════

Este menu serve como ponto central para todas as operações
do programa. Através das opções disponíveis, é possível
aplicar cálculos, transformar o vetor ou produzir matrizes
derivadas dos valores introduzidos. Cada seleção executa a
função correspondente e devolve o menu para nova escolha.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Em caso de dúvidas ou necessidade de mais informações, 
contacte: grupo1@ubi.pt
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        return

    # 1 - Recolher os numeros
    numbers = get_numbers_from_user(
        "Bem-vindo! Vamos começar por ler o vetor INICIAL que será usado nas operações do menu."
    )
    while True:
        menu(numbers)
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            valor = valor_mais_proximo(numbers, target=15)
            print(f"\n[1] O valor do vetor mais próximo de 15 é: {valor}\n")

        elif opcao == '2':
            resultados = cosseno_segunda_metade(numbers)
            print("\n[2] Cosseno dos elementos da segunda metade do vetor:")
            print("    ", resultados, "\n")

        elif opcao == '3':
            vetor_ordenado = ordernar_vector(numbers)
            print("\n[3] Vetor ordenado por ordem decrescente:")
            print("    ", vetor_ordenado, "\n")

        elif opcao == '4':
            filtrados = nao_divisiveis_por_tres(numbers)
            print("\n[4] Valores do vetor que NÃO são divisíveis por 3:")
            print("    ", filtrados, "\n")

        elif opcao == '5':
            print("\n[5] Matriz 2x10 com a primeira linha igual ao vetor inicial")
            print("    e a segunda linha com os valores quadruplicados:\n")
            result = matriz_2x10_quadruplo(numbers)
            mostrar_matriz(result)
            print()

        elif opcao == '6':
            media = media_vetor(numbers)
            print(f"\n[6] A média dos valores do vetor é: {media:.2f}\n")

        elif opcao == '7':
            print_ajuda()

        elif opcao == '8':
            numbers_2, result = soma_primeiro_com_dobro_segundo(numbers)

            print("\n[8] Vetor inicial utilizado na operação:")
            print("    ", numbers)
            print("    Novo vetor lido nesta opção:")
            print("    ", numbers_2)
            print("    Resultado da soma do vetor inicial com o DOBRO do novo vetor:")
            print("    ", result, "\n")

        elif opcao == '9':
            compostos = elementos_compostos_vector(numbers)
            print("\n[9] Números compostos (não primos) presentes no vetor inicial:")
            if compostos:
                print("    ", compostos, "\n")
            else:
                print("    O vetor inicial não contém números compostos.\n")

        elif opcao == '10':
            print("\n[10] Matriz 10x10 resultante do produto entre o vetor inicial")
            print("     e o mesmo vetor ordenado por ordem crescente:\n")
            result = produto_com_ordem_crescente(numbers)
            mostrar_matriz(result)
            print()

        elif opcao == '11':
            print("\n[11] Matriz 10x10 transposta da matriz de produtos (opção 10):\n")
            result_10_x_10 = produto_com_ordem_crescente(numbers)
            transp_result = transposta(result_10_x_10)
            mostrar_matriz(transp_result)
            print()

        elif opcao == '0':
            print("\nPrograma terminado. Obrigado por utilizar o sistema!\n")
            break

        else:
            print("\nOpção inválida! Por favor, tente novamente.\n")

if __name__ == '__main__':
    init_program()
