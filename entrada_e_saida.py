nome = 'Bruno'
idade = 25
cidade = 'Cuiaba-MT'

# Usando f-string (a forma mais moderna e recomendada)
print(f"Ola, meu nome e {nome}, tenho {idade} anos e atualmente moro em {cidade}.")

#formatando os números agora
preco = 49.9999
print(f"o preco desse produto e R${preco:.2f}")  # limita a 2 casas decimais

#entrada com de dados com input()

#pedindo para o usuario digitar seu nome
nome_usuario = input("Digite seu nome: ")

#pedindo a idade do usuario (note que input() retorna string, entao precisamos converter para int)
idade_usuario_str = input("Qual é a sua idade? ")
idade_do_usuario_int = int(idade_usuario_str)

from datetime import datetime

#pega o ano corrente na data definida no sistema operacional da maquina
ano_atual = datetime.now().year

#Processando a idade para calcular o ano de nascimento
ano_nascimento = ano_atual - idade_do_usuario_int

# Exibindo o resultado
print(f"\nOlá, {nome_usuario}! Bem-vindo(a).")
print(f"Você tem {idade_do_usuario_int} anos e nasceu aproximadamente em {ano_nascimento}.")



