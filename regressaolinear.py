import math

arrx = []
arry = []
size = int(input("insira quantos pares de valores serao colocados: "))
a = float(input("insira o coef angular (a): "))
b = float(input("insira o coef linear (b): "))
for i in range(size):
    x = float(input())
    y = float(input())
    arrx.append(x)
    arry.append(y)

somanum = 0
for i in range(size):
    somanum += ((a * arrx[i]) + b - arry[i])**2
deltay = math.sqrt((somanum/(size-2)))

somax = 0
for i in range(size):
    somax += arrx[i]
mediax = somax/size

somadesviox = 0
for i in range(size):
    somadesviox += (arrx[i] - mediax)**2

deltaa = (deltay/(somadesviox)**2)

somaxquadrado = 0
for i in range(size):
    somaxquadrado += (arrx[i])**2
deltab = math.sqrt(somaxquadrado/ size * somadesviox) * deltay

print("o delta a e", deltaa)
print("o delta b e", deltab)
input('Pressione alguma tecla para sair')