m = float(input('\033[1;34mMetros: \033[m'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'Quilômetros: \033[33m{km}\033[m\n'
      f'Hectômetros: \033[33m{hm}\033[m\n'
      f'Decametros: \033[33m{dam}\033[m\n'
      f'Decimetros: \033[33m{dm}\033[m\n'
      f'Centrímetros: \033[33m{cm}\033[m\n'
      f'Milímetros: \033[33m{mm}\033[m')