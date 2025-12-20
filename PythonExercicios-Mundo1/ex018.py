from math import radians, sin, cos, tan
a = radians(float(input('\033[1;34mDigite o valor de um ângulo: \033[m')))
print(f'\033[1;40mSeno: \033[33m{sin(a):.4f}\033[m\n'
      f'\033[1;40mCosseno: \033[33m{cos(a):.4f}\033[m\n'
      f'\033[1;40mTangente: \033[33m{tan(a):.4f}\033[m')