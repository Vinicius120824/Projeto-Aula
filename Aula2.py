#Aula 2
#Introdução

#1 + 2 + 3 + 4 + 5
#(23+19+31)/3
#403//73 # -> // somenete o resolutado inteiro
#403%73 # -> % (mod) somenete a sobra do resultado
#2**10
#print(abs(54-57))
#print(min(34, 29, 31))

###############################################################

#s1 = 'ant'
#s2 = 'bat'
#s3 = 'cod'

#Exercicio a)

#print(s1 + ' ' + s2 + ' ' + s3)

#Exercicio b)
#print(10 * (s1 + ' '))

#Exercicio c)
#print(s1 + ' ' + 2 * (s2 + ' ') + 3 * (s3 + ' '))

#Exercicio d)
#print(7 * (s1 + ' ' + s2 + ' '))

#Exercicio e)
#print(5 * (2 * (s2) + s3 + ' '))

#####################################################################################

# 1º Exercicio
#preco = float(input('Informe o valor do preço do produto:'))
#p = float(input('Informe o percentual de desconto (0-100)%:'))

#desconto = preco  * (p / 100)
#final = preco - desconto

#print('O valor do seu produto {} com o percentual de desconto é:{}'.format(preco, p))
#print('O valor do seu produto com desconto é:{}'.format(final))

#####################################################################################

# 2º Exercicio
#km = float(input('Quantidade de Km percorrido pelo carro alugado:'))
#dias = float(input('Quantidade de dias pelos aquais o carro foi alugado:'))

#precoapagar = 60 * dias + 0.15 * km

#print('O valor por dia alugado é R${}, e o valor por Km precorrido é R${}:'.format(dias, km))
#print('O valor a se pagar é R${}:'.format(precoapagar))

#####################################################################################

# 3º Exercicio

frase = input('Digite uma frase qualquer:')
tam = len(frase)
frase2 = frase[:int(tam/2)]
print(frase[-2:])

#Aula 2 Finalizada!!!