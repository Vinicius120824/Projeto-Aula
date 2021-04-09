#Introdução ao Programa
print('\tPara começar preencha o cadastro com nome e peso de seu lutador, '
      'para saber em qual categoria ele se encaixa!! ')
# o \t = espaço / seria para deixar mais apresentavel para o leitor que irá ver o resultado na tela !

#Declaração das variáveis aonde o usurario terá digitar as informações
nome = input('\tDigite o nome do lutador: ')
peso = float(input('\tDigite o peso do lutador (em kg): '))

#Processamento
#Aqui seria a entrada onde será a verificação do valor so peso e aonde ele se encaixa na tabela de categoria
#e irá imprimir na tela o peso o nome e a categoria se a função for verdadeira
if peso < 65:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Pena'.format(nome, peso, nome, peso))
elif peso >= 65 and peso < 72:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Leve'.format(nome, peso, nome, peso))
elif peso >= 72 and peso < 79:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Ligeiro'.format(nome, peso, nome, peso))
elif peso >= 79 and peso < 86:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Meio-Médio'.format(nome, peso, nome, peso))
elif peso >= 86 and peso < 93:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Médio'.format(nome, peso, nome, peso))
elif peso >= 93 and peso < 100:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Meio-Pesado'.format(nome, peso, nome, peso))
#Se caso nem uma das funções acima for verdadeira ela entra no else que seria de 100kg pra cima
#e imprima a ultima categoria
else:
    print('\n Nome fornecido: {}\n Peso fornecido: {}\n '
          'O lutador {} pesa {}Kg e se enquadra na categoria Pesado' .format(nome, peso, nome, peso))
# o \n = pular linha / seria para deixar mais apresentavel para o leitor que irá ver o resultado na tela !