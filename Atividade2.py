# Aqui ele valida a entrada do usuário com uma função def
def validarEntrada(string, min, max):
    res = int(input(string))
    while (res < min) or (res > max):
        print('Ops, digite um código de produto de 10000 até 30000 !! ')
        res = int(input(string))
    return res

# Aqui soma todos os números da lista
def soma():
    soma_num = 0
    for soma in novoPeso:
        soma_num += soma
# E por fim entra na divisão do resto da soma para achar o digito verificador
    soma_num = soma_num % 7
    digito = soma_num
    # Retornando o digito calculado para a variável dig
    return digito
# programa principal: Declarando as variáveis

novoPeso = [0, 0, 0, 0, 0]
peso = [2, 3, 4, 5, 6]
num = []

# Ponto de entraada do usuário
y = validarEntrada('Digite o código de produto: ', 10000, 30000)

# Aqui ele pega os numeros digitados pelo usuario e transfora em  uma string 
vec = str(y)

# Depois convertemos de novo para int, só que, colocando índice por índice
ind = 0
for i in range(0, 5, 1):
    num.append(int(vec[ind]))
    ind += 1

# Ele entra nesse outro for para realizar o calculo da multiplicação do peso do produto
ind = 0
for i in range(0, 5, 1):
    novoPeso[ind] = peso[ind] * num[ind]
    ind += 1

dig = soma()

# Chega no fim do código mostrando para o usuario o resultado do código do produto
print('O seu código verificador de produto é: {}-{}'.format(y, dig))