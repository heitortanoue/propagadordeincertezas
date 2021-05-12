import math
# ========================================
# OPERAÇÕES

def soma (n1, n2):
  return [n1[0] + n2[0], n1[1] + n2[1]]

def sub (n1, n2):
  return [n1[0] - n2[0], n1[1] + n2[1]]

def prod (n1, n2):
  return [(n1[0] * n2[0]), (n1[1] * n2[0]) + (n1[0] * n2[1])]

def div (n1, n2):
  return [(n1[0] / n2[0]), (((n1[1] * n2[0]) + (n1[0] * n2[1])) / (n2[0]**2))]

def cos (n1):
  return [math.cos(n1[0]), (math.sin(n1[0]) * n1[1])]

def sen (n1):
  return [math.sin(n1[0]), (math.cos(n1[0]) * n1[1])]

def prodconst (const, n1):
  return [(const * n1[0]), (const * n1[1])]

def pot (const, n1):
  return [n1[0]**const, (const * (n1[0]**(const-1)) * n1[1])]

def log (base, n1):
  return [math.log(n1[0], base), ((math.log(math.e, base) / n1[0]) * n1[1])]

def exp (base, n1):
  return [base**n1[0], ((base**n1[0]) * math.log(base) * n1[1])]

# ========================================
# Funções auxiliadoras

def numerize (arr):
  for i in range(len(arr)):
    arr[i] = float(arr[i])
  return arr

def arredondar(x):
  casas = -int(math.floor(math.log10(abs(x[1]))))
  return [round(x[0], casas), round(x[1], casas)]

# ========================================
# Variáveis
mem = None; memformatado = None; useMem = None
cont = 'S'

# Tipo 0: 2 num com incerteza
# Tipo 1: 1 num com incerteza
# Tipo 2: 1 num com incerteza e uma constante
operacoes = [
  {'nome': 'Soma', 'func': soma, 'exp': '(a + b)', 'tipo': 0},
  {'nome': 'Subtração', 'func': sub, 'exp': '(a - b)', 'tipo': 0},
  {'nome': 'Multiplicação', 'func': prod, 'exp': '(a * b)', 'tipo': 0},
  {'nome': 'Produto por constante', 'func': prodconst, 'exp': '(c * a)', 'tipo': 2},
  {'nome': 'Potência', 'func': pot, 'exp': '(a^c)', 'tipo': 2},
  {'nome': 'Divisão', 'func': div, 'exp': '(a / b)', 'tipo': 0},
  {'nome': 'Cosseno', 'func': cos, 'exp': '(cos(a) em radianos)', 'tipo': 1},
  {'nome': 'Seno', 'func': sen, 'exp': '(sen(a) em radianos)', 'tipo': 1},
  {'nome': 'Logaritmo de base c', 'func': log, 'exp': '(log c (a))', 'tipo': 2},
  {'nome': 'Exponencial de base c', 'func': exp, 'exp': '(c^a)', 'tipo': 2},
]
# ========================================

print("╔══════════════════════════════════╗")
print(("PROPAGADOR DE INCERTEZAS").center(36))
print("para lab. de física".center(36))
print("by Toi".center(36))
print("╚══════════════════════════════════╝")

print(
    "\nEscolha a operação a ser realizada e digite o seu número correspondente"
)

for i in range(len(operacoes)):
  print('[' + str(i) + '] - ' + operacoes[i]['nome'] + ' ' + operacoes[i]['exp'])

# ========================================
while cont == 'S':

  if mem:
    useMem = str(input('Deseja usar o último resultado (' + memformatado + ')? (S/N): ')).upper()

  option = int(input('\nOperação escolhida: '))
  res = [0, 0]
  selected = operacoes[option]

  print('-=- ' + selected['nome']  + ' -=-')
  # TIPO 2 ou TIPO 1
  if selected['tipo'] == 1 or selected['tipo'] == 2:
    if selected['tipo'] == 2:
      const = float(input('Insira a constante/base c (use o ponto como separador decimal)\n'))
    if useMem == 'S':
      num = mem
    else:
      inp = str(input("Insira o número e sua incerteza, separados por um espaço (use o ponto como separador decimal)\n"))
      num = numerize(inp.split(' '))
    if selected['tipo'] == 1:
      res = selected['func'](num)
    else:
      res = selected['func'](const, num)

  # TIPO 0
  else:
    if useMem == 'S':
      num1 = mem
    else:
      inp1 = str(input("Insira o primeiro número e sua incerteza, separados por um espaço (use o ponto como separador decimal)\n"))
      num1 = numerize(inp1.split(' '))

    inp2 = str(input("Insira o segundo número e sua incerteza, separados por um espaço (use o ponto como separador decimal)\n"))
    num2 = numerize(inp2.split(' '))
    res = selected['func'](num1, num2)

  mem = res
  numarrendonado = arredondar(res)
  respformatada = str(numarrendonado[0]) + ' ± ' + str(numarrendonado[1])
  respnaoformatada = str(res[0]) + ' ± ' + str(res[1])
  memformatado = str(respformatada)
  # print('\nResultado: ' + str(respformatada))
  cont = str(input('\nDeseja continuar as contas? (S/N): ')).upper()

# ========================================

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(('RESULTADO FINAL = ' + respformatada).center(41))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
input('Pressione alguma tecla para sair').center(41)

