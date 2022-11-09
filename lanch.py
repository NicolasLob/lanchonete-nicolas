preco = 0 #variável de preço dos produtos
nico4022326 = 'Nícolas Vinícius Lobo Morais'
print('Bem Vindo a lanchonete do {}'.format(nico4022326))
print('-----------------Cardápio-----------------')
print('| Código | Descrição | Valor |')
print('| 100 | Cachorro Quente | 9,00 |')
print('| 101 | Cachorro Quente Duplo | 11,00 |')
print('| 102 | X-Egg | 12,00 |')
print('| 103 | X-Salada | 12,00 |')
print('| 104 | X-Bacon | 14,00 |')
print('| 105 | X-Tudo | 17,00 |')
print('| 200 | Refrigerante Lata | 5,00 |')
print('| 201 | Chá Gelado | 4,00 |')
while True:
codigo = input('Entre com o código desejado: ') #Código do pedido
if (codigo == '100'):
preco += 9 # Preço inicia com 0 e os valores vão sendo adicionados
conforme o cliente pede algo
print('Você pediu um Cachorro Quente no valor de R$ 9,00')
elif (codigo == '101'):
preco += 11
print('Você pediu um Cachorro Quente Duplo no valor de R$ 11,00')
elif (codigo == '102'):
preco += 12
print('Você pediu um X-Egg no valor de R$ 12,00')
elif (codigo == '103'):
preco += 12
print('Você pediu um X-Salada no valor de R$ 12,00')
elif (codigo == '104'):
preco += 14
print('Você pediu um X-Bacon no valor de R$ 14,00')
elif (codigo == '105'):
preco += 17
print('Você pediu um X-Tudo no valor de R$ 17,00')
elif (codigo == '200'):
else: # Se o código for digitado errado, uma mensagem escrita "Opção
inválida" irá aparecer
print('Opção Inválida')
continue
resp = input('Deseja pedir mais alguma coisa? \n 1 - Sim \n 2 - Não \n>>
')
if (resp == '1'):
continue
else: # Se a resposta for 2 ou qualquer outra coisa que não for "1", o
programa acaba e o valor da conta aparece
print('O total a ser pago é R$ {:.2f}'.format(preco))
break
preco += 5
print('Você pediu um Refrigerante Lata no valor de R$ 5,00')
elif (codigo == '201'):
preco += 4
print('Você pediu um Chá Gelado no valor de R$ 4,00')
