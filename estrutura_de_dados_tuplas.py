#criando uma tupla
coordenadas = (10.5, 20.3)
print(f"tupla de coordenadas: {coordenadas}")

#acessando um item pelo indice
print(f"coordenada x: {coordenadas[0]}")
print(f"coordenada y: {coordenadas[1]}")

#tentativa de modificar um item da tupla (isso vai gerar um erro, pois tuplas são imutáveis)
#coordenadas[0] = 15.0  # Isso vai gerar um TypeError

#tuplas são uteis para armazenar dados que não devem ser alterados, como coordenadas, datas, etc. 
#Elas também podem ser usadas como chaves em dicionários ou elementos de conjuntos, ao contrário das 
#listas.

dias_de_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
print(f"O primeiro dia da semana e: {dias_de_semana[0]}")
print(f"o ultimo dia da semana e: {dias_de_semana[-1]}")

