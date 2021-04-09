# Exibição do dicionário Media
Media = {}
# Leitura dos dados

# Aqui vai pedir pro usuário estimular um periodo de repetições no loop for
n = int(input('Digite quantos alunos irá calcular a média: '))
cont = 0
# Entrada da repetição para a leitura dos daods fornecidos pelo teclado
for i in range(0, n):
  # nome vai entrar como chave dentro do dicionário
  nome = input('Nome do aluno {}: '.format(i + 1))
  # Preenchimento das notas do aluno citado a cima
  nota = float(input('Digite a {}ª nota do aluno: '.format(cont + 1)))
  n1 = float(input('Digite a {}ª nota do aluno: '.format(cont + 2)))
  n2 = float(input('Digite a {}ª nota do aluno: '.format(cont + 3)))
  n3 = float(input('Digite a {}ª nota do aluno: '.format(cont + 4)))
  cont = 0
  # Atribuindo o nome como chave e as notas como valores dentro do dicionário
  Media[nome] = (nota, n1, n2, n3)


print('Nota dos alunos!')
print('-' * 10)
# Incluimos uma copia do dicionario porque não deve ser capaz de expandir/encolher o dicionario enquanto está looping
# Então se cria uma copia para nao ocorrer o erro
mediacopia = {**Media}
# Entramos na varredura e a exibição dos dados varridos e o calculo da media dos alunos exibidos
for nome, notas in mediacopia.items():
  media = (notas[0] + notas[1] + notas[2] + notas[3]) // 4
  # Entra na condição if e se for verdadeira aplica a condição se não aplica outra condição
  if media >= 7:
    print('{} \t{}\t{}\t{}\t{} - Aprovado'.format(nome, notas[0], notas[1], notas[2], notas[3]))
  else:
    print('{} \t{}\t{}\t{}\t{} - Reprovado'.format(nome, notas[0], notas[1], notas[2], notas[3]))
# Fim do codigo !