#criando uma lista 

frutas = ['Bannana', 'Maca', 'Laranja', 'Abacaxi', 'Uva']
print(f"lista de frutas: {frutas}")

#agora vamos acessar a primeira e a ultima fruta da lista
print(f"A primeira fruta da lista e: {frutas[0]}")
print(f"a ultima fruta da lista e: {frutas[-1]}")

#agora vamos remover uma fruta da lista
frutas.remove('Abacaxi')
print(f"Abacaxi saiu da lista, agora confere a lista de frutas apos a remocao: {frutas}")

#agora vamos adicionar duas frutas a lista
frutas.append('Manga')
frutas.append('Kiwi')
print(f"Duas frutas foram adicionadas a lista: {frutas}")

#modificando um item da lista
frutas[0] = 'Banana'
print(f"lista de frutas apos a modificacao: {frutas}")

#vamos ordenar a lista de frutas
frutas.sort()
print(f"lista de frutas ordenada: {frutas}")

#vamos verificar o tamanho da lista de frutas
print(f"A lista de frutas tem {len(frutas)} frutas")