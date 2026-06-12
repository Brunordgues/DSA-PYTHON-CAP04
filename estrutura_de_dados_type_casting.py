#é a conversão de um tipo de dado para outro

"""
=== TYPE CASTING (Conversão de tipos) ===

int(x)     # converte para inteiro (perde decimais)
float(x)   # converte para decimal
str(x)     # converte para texto (sempre funciona)
list(x)    # converte para lista
tuple(x)   # converte para tupla (imutável)
set(x)     # converte para conjunto (remove duplicatas)
dict(x)    # converte para dicionário
bool(x)    # converte para True/False

EXEMPLOS:
int(3.9)      # 3
float(5)      # 5.0
str(123)      # "123"
list("abc")   # ['a', 'b', 'c']
tuple([1,2])  # (1, 2)
set([1,1,2])  # {1, 2}
bool(0)       # False
bool("")      # False

REGRAS:
- String numérica → int("123") funciona
- String com letras → int("abc") dá erro
- True = 1, False = 0 (bool é subclasse de int)
"""

#convertendo de string para numero integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(f"String '{numero_em_texto}' para inteiro: {numero_inteiro}, tipo: {type(numero_inteiro)}")

#convertendo de string para numero float
numero_decimal_em_texto = "45.67"
numero_float = float(numero_decimal_em_texto)
print(f"String '{numero_decimal_em_texto}' para float: {numero_float}, tipo: {type(numero_float)}")


#convertendo de numero para string
idade = 25
idade_texto = str(idade)
print(f"String '{numero_em_texto}' para inteiro: {idade_texto}, tipo: {type(idade_texto)}")

#convertendo entre estrutura de dados
print("\n=== Conversao entre estruturas de dados ===")
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)

print(f"\nLista origianl: {lista_com_duplicatas}")
print(f"\nConjunto (sem duplicatas): {conjunto_unico}")
print(f"\nConvertida de volta para Lista: {lista_sem_duplicatas}\n")