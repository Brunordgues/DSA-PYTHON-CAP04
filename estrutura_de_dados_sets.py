'''
Estruturas de Dados - Conjuntos (Sets)
Conjuntos são coleções não ordenadas de itens únicos e mutáveis. 
Eles são úteis para remover duplicatas e 
realizar operações matemáticas de conjuntos (união, interseção).
'''

"""
=== SETS (Conjuntos) ===

CARACTERÍSTICAS:
- Elementos únicos (sem duplicatas)
- Não ordenado (não mantém sequência)
- Busca rápida O(1) (usa tabela hash)
- Elementos precisam ser imutáveis (str, int, tuple)

CRIAÇÃO:
meu_set = {1, 2, 3}
vazio = set()  # {} é dicionário!

OPERAÇÕES:
|  (união)          # {1,2} | {2,3}  → {1,2,3}
&  (interseção)     # {1,2} & {2,3}  → {2}
-  (diferença)      # {1,2} - {2,3}  → {1}
^  (diferença simétrica) # {1,2} ^ {2,3} → {1,3}

MÉTODOS ÚTEIS:
add(5)        # adiciona elemento
remove(5)     # remove (erro se não existir)
discard(5)    # remove (não dá erro)
clear()       # limpa tudo
copy()        # copia o set

EXEMPLO PRÁTICO:
lista_com_dupes = [1, 2, 2, 3, 3, 3]
lista_sem_dupes = list(set(lista_com_dupes))  # [1, 2, 3]
"""

# Criando um conjunto (note que os itens duplicados são removidos)
numeros = {1, 2, 2, 3, 4, 2, 5, 3, 5}
print(f"Conjunto de numeros (sem duplicatas): {numeros}")

# Adicionando um novo número ao conjunto
numeros.add(6)
print(f"Foi adicionado o numero 6 ao conjunto: {numeros}")

# Removendo um número do conjunto
numeros.remove(3)
print(f"Apos remover o numero 3 do conjunto: {numeros}")

# Criando as variáveis que estavam faltando
conjunto_unico = numeros
lista_sem_duplicatas = list(numeros)

# Exibindo os resultados finais
print(f"\nLista original: {numeros}")
print(f"\nConjunto (sem duplicatas): {conjunto_unico}")
print(f"\nConvertida de volta para Lista: {lista_sem_duplicatas}\n")


# Operações de conjunto
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# União (todos os elementos de ambos os conjuntos)
uniao = conjunto_a.union(conjunto_b)
print(f"uniao de A e B: {uniao}")

# Interseção (elementos que estão em ambos os conjuntos)
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Intersecao de A e B: {intersecao}")