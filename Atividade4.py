# cria a função ordem para colocar em ordem alfaetica ['nome'] e retorna para lista.sort().
def ordem(e):
  return e['nome']
# declara as variaveis, como dict anilhada.
lista = []
list(lista)
dados = dict()
listaMaior = []
listaMenor = []
# Leitura de dados do usuário
# Onde o nome do dict dados vai ser o ponto de entrada do teclado, e com isso o usuário so pode terminar se digitar 'sair'.
print('AGENDA TELEFÔNICA!')
print('PARA SAIR E SALVAR A AGENDA DIGITE (sair)!!')
dados['nome'] = str(input('Nome: ')).title()
# Aqui entra no laço(loop) para o preenchimento das chaves dentro do dict dados.
while True:
  if dados['nome'] == 'Sair':
    break
  dados['idade'] = int(input('Idade: '))
  dados['telefone'] = int(input('Telefone: '))
  lista.append(dados.copy())
  dados['nome'] = str(input('Nome: ')).title()
# lista.sort, o .sort seria o metodo para lista organizar a chave 'nome' em ordem alfabetica,
# Onde eu chamo a função para com que a chave 'nome' seja organizada diretamente.
  lista.sort(key=ordem)
# Aqui eu atribuo um novo dict com as informações do dict(dados) para amarzenar em um outra aba
# fazendo a varredura das chave:valores e aplicando a condição de Maior de idade e Menos de idade em outras duas dict

# Depois que atribui as chaves:valores em uma copy do dict(dados), uso dessa função para deleta-la o dict origem.
dados = dict()
del dados

print('AGENDA DE NOMES EM ORDEM ALFÁBETICA!')
print(f'{"Nome":<15}{"Idade":<10}{"Telefone":<10}')
for contatos in lista:
  print(f'{contatos["nome"]:<15}{contatos["idade"]:<10}{contatos["telefone"]:<10}')
  if contatos['idade'] >= 18:
      listaMaior.append(contatos.copy())
  elif contatos['idade'] < 18:
      listaMenor.append(contatos.copy())


# Depois de aplicar as condições faço novamente uma varredura nos dict e gravando em um outro documento, colocando os maiores de idade em listaMaior
# E os menores de idade em listaMenor
print('AGENDA TELEFÔNICA COM MAIOR DE 18 ANOS IDADE! ')
print(f'{"Nome":<15}{"Idade":<10}{"Telefone":<10}')
for contatos1 in listaMaior:
  print(f'{contatos1["nome"]:<15}{contatos1["idade"]:<10}{contatos1["telefone"]:<10}')

# Aqui se aplica a mesma coisa para os menores de idade!
print('AGENDA TELEFÔNICA COM MENOR DE 18 ANOS IDADE! ')
print(f'{"Nome":<15}{"Idade":<10}{"Telefone":<10}')
for contatos1 in listaMenor:
    print(f'{contatos1["nome"]:<15}{contatos1["idade"]:<10}{contatos1["telefone"]:<10}')