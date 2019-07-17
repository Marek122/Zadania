def brakujace_elementy(lista_elementow, n):

  lista_brakujacych_elementow = []

  for x in range(1, n + 1):
    if x not in lista_elementow:
      lista_brakujacych_elementow.append(x)

  return lista_brakujacych_elementow
