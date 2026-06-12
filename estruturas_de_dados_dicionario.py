#criando um dicionario com informação de um aluno

aluno = {
    'nome': 'Bruno Rodrigues',
    'idade': 24,
    'curso': 'Analise e Desenvolvimento de Sistemas',
    'aluno_ativo': True
}

print(f"dicionario do aluno: {aluno}")

#acessando um valor pela sua chave
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get('curso')}")

#adicionando um novo par chave-valor ao dicionario
aluno['cidade'] = "Sao PAULOOOOOO"
print(f"Dicionario do aluno atualizado: \n {aluno}")

#modificando um valor existente
aluno["idade"] = 25
print(f"Idade atualizada: {aluno['idade']}")

#removendo um par chave-valor do dicionario
del aluno['aluno_ativo']
print(f"Dicionario apos remover a chave 'ativo':\n {aluno}")