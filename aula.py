import random
from collections import Counter
from matplotlib import pyplot as plt
import math

def quantidade_de_usuarios_na_rede():
  return 100

def gera_amizades (numero_conexoes_desejado, qtde_usuarios_na_rede):
  conexoes = []
  for _ in range (numero_conexoes_desejado):
    while True:
      u1 = random.randint (0, qtde_usuarios_na_rede - 1)
      u2 = random.randint(0, qtde_usuarios_na_rede - 1)
      if u1 != u2 and not((u1, u2) in conexoes):
        conexoes.append((u1, u2))
        break
  return conexoes

def quantidade_de_amigos (amizades):
  #[(1, 2), (3, 5), (1, 7), (8, 5)] => [1, 3, 1, 8] => {1:2, 3:1, 8:1}
  a = Counter (i for i, _ in amizades)
  #[(1, 2), (3, 5), (1, 7), (8, 5)] => [2, 5, 7, 5] => {2:1, 5:2, 7:1}
  b = Counter (i for _, i in amizades)
  #{1:2, 3:1, 8:1, 2:1, 5:2, 7:1}
  tudo = a + b
  #{1:2, 3:1, 8:1, 2:1, 5:2, 7:1} => [2, 1, 1, 1, 2, 1] => {2:2, 1:4}
  return Counter (x for x in tudo.values())

def gera_histograma_contagem_amigos(quantidade_de_amigos, qtde_usuarios_na_rede):
  xs = range(qtde_usuarios_na_rede)
  ys = [quantidade_de_amigos[x] for x in xs]
  plt.bar(xs, ys)
  plt.axis ([0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede /4])
  plt.title("Histograma da Contagem de Amigos")
  plt.xlabel ("# de amigos")
  plt.ylabel ("# de usuários")
  plt.show()


def gera_histograma_contagem_amigos_test ():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  amizades = gera_amizades(1000, qtde_usuarios_na_rede)
  qtde_amigos = quantidade_de_amigos(amizades)
  gera_histograma_contagem_amigos(qtde_amigos, qtde_usuarios_na_rede)


def mostra_primeiro_e_segundo_maiores (qtde_amigos):
  print (qtde_amigos)
  lista = sorted(qtde_amigos.values())
  print ("Maior: " + str(lista[len(lista) - 1]))
  print("Segundo maior: " + str(lista[-2]))


def mostra_primeiro_e_segundo_maiores_test ():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  amizades = gera_amizades (1000, qtde_usuarios_na_rede)
  qtde_amigos = quantidade_de_amigos(amizades)
  mostra_primeiro_e_segundo_maiores (qtde_amigos)

def media_qtde_amigos (qtde_amigos):
  #{5: 2, 8: 2, 3: 5} => [10, 16, 15]
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  return sum (so_qtdes) / sum (x for x in qtde_amigos.values())

def media_qtde_amigos_test ():
  qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
  amizades = gera_amizades(500, qtde_usuarios_na_rede)
  qtde_amigos = quantidade_de_amigos(amizades)
  print (media_qtde_amigos (qtde_amigos))


def mediana_qtde_amigos (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  ordenada = sorted (so_qtdes)
  meio = len (ordenada) // 2
  return ordenada[meio] if meio % 2 == 1 else (ordenada[meio - 1] + ordenada[meio]) / 2

def quantil (qtde_amigos, percentual = 0.5):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  indice = int(percentual * len (so_qtdes))
  return sorted(so_qtdes)[indice]

def moda_qtde_amigos (qtde_amigos):
  moda = max (qtde_amigos.values())
  return [x for x, count in qtde_amigos.items() if count == moda]

def amplitude_dos_dados (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  return max(so_qtdes) - min (so_qtdes)

def diferencas_em_relacao_a_media (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  media = media_qtde_amigos (qtde_amigos)
  return [x - media for x in so_qtdes]

def soma_dos_quadrados (diferencas):
  return sum (x**2 for x in diferencas)

def variancia (qtde_amigos):
  so_qtdes = [x * y for x, y in qtde_amigos.items()]
  return soma_dos_quadrados(diferencas_em_relacao_a_media(qtde_amigos)) / (len (so_qtdes) - 1)

def desvio_padrao (qtde_amigos):
  return math.sqrt(variancia(qtde_amigos))

def main ():
  #mostra_primeiro_e_segundo_maiores_test()
  media_qtde_amigos_test()

main()

