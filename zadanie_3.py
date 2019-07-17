from decimal import *

def generuj_liczby():
  
  lista_liczb = []

  for x in range(4, 12):
    lista_liczb.append(Decimal(x/2))
  return lista_liczb
