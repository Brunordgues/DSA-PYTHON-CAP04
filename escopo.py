# 1️⃣ Variável no quarto inteiro (escopo global)
brinquedo = "boneca"          # A boneca está no quarto

def brincar():
    # 2️⃣ Recipiente dentro da caixa (escopo local da função)
    brinquedo = "carro"       # Dentro da caixa, agora tem um carro
    print("Dentro da caixa:", brinquedo)  # Mostra CARRO

brincar()                     # Executa a função
print("No quarto:", brinquedo)               # Mostra BONÉCA (a global)

# 3️⃣ Recipiente dentro de uma gaveta (loop for)
for numero in range(3):
    gaveta = numero + 1      # A gaveta recebe 1, depois 2, depois 3
    print("Dentro da gaveta:", gaveta)   # 1, 2, 3

print("Depois do loop, na gaveta:", gaveta)   # 3 (a gaveta ainda existe)

# 4️⃣ Dois brinquedos na mesma caixa, mas um diz “não é meu!”
def caixa_com_brincos():
    brinquedo = "boneca"     # Recipiente local
    def muda_brincos():
        nonlocal brinquedo  # Diz que o brinquedo é o mesmo da caixa
        brinquedo = "carro" # Troca o brinquedo dentro da caixa
        print("Dentro da caixa (muda):", brinquedo)  # CARRO

    muda_brincos()
    print("Dentro da caixa (final):", brinquedo)     # CARRO

caixa_com_brincos()