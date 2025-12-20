from time import sleep
print(f'\033[1;33m{" CONTAGEM REGRESSIVA ":=^31}\033[0m')
for c in range(10, -1, -1):
    print(f'\033[1m{c:^30}\033[m')
    sleep(1)
print(f'\033[1;35m{" FOGOS ":=^31}\033[m')
print('\033[1;33m=\033[m'*31)