 #Conjuntos são coleções não ordenadas de itens únicos e mutáveis. 
 # Eles são úteis para remover duplicatas e realizar operações matemáticas de conjuntos 
 # (união, interseção).

#criando um conjunto (note que os itens são removidos se forem duplicados)

numeros = {1,2,3,4,2,3,5}
print(f"conjunto de numeros (sem duplicados): {numeros}")

#agora vamos adicionar um novo numero ao conjunto
numeros.add(6)
print(f"foi adicionado o numero 6 ao conjunto: {numeros}")

#removendo um numero do conjunto
numeros.remove(3)
print(f"apos remover o numero 3 do conjunto: {numeros}")

#operações de conjuntos
conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}

# Uniao (todos os elementos de ambos os conjuntos)
uniao = conjunto_a.union(conjunto_b)
print(f"Uniao de A e B: {uniao}")

# Interseção (elementos que estão em ambos os conjuntos)
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Intersecao de A e B: {intersecao}")
