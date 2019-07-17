def generuj_kody(kod_poczatkowy, kod_koncowy):

  lista_kodow = []

  if int(kod_poczatkowy[0:2]) == int(kod_koncowy[0:2]):
    for x in range(int(kod_poczatkowy[3:6]) + 1, int(kod_koncowy[3:6])):
      nowy_kod = kod_poczatkowy[0:2] + '-' + str(x).zfill(3)
      lista_kodow.append(nowy_kod)

  else:
    for x in range(int(kod_poczatkowy[3:6]) + 1, 1000):
        nowy_kod = kod_poczatkowy[0:2] + '-' + str(x).zfill(3)
        lista_kodow.append(nowy_kod)

    if (int(kod_koncowy[0:2]) - int(kod_poczatkowy[0:2])) > 1:
      for x in range(int(kod_poczatkowy[0:2]) + 1, int(kod_koncowy[0:2])):
        for y in range(1000):
          nowy_kod = str(x).zfill(2) + '-' + str(y).zfill(3)
          lista_kodow.append(nowy_kod)

    for x in range(0, int(kod_koncowy[3:6])):
        nowy_kod = kod_koncowy[0:2] + '-' + str(x).zfill(3)
        lista_kodow.append(nowy_kod)

  return lista_kodow
