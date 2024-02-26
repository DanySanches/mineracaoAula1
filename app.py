# Variaveis
nome = "Danielle Sanches"
idade = 36

print(f"Nome: {nome}")
print(f"Idade: {idade}")

#Operações Matemáticas
# +, -, *, /
soma = idade + 5
subtracao = idade - 2
multiplicacao = idade * 3
divisao = idade / 5

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

frase = "Nome: " + nome + ", idade: " + str(idade) + "."

print(f"Frase: {frase}")

#Operações de Comparação
teste_idade = idade >= 18
teste_nome = nome == "Danielle Sanches"

print(f"Idade: {teste_idade}")
print(f"Nome: {teste_nome}")

#Funções
tamanho_nome = len(nome)

print(f"Quantidade de caracteres: {tamanho_nome}")

#Laços
for i in range(5):
    print(i)

numero = 1
while numero <= 5:
    print(numero)
    numero += 1