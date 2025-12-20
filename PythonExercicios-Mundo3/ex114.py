import requests

def verificar_site(url):
    try:
        requests.get(url)
    except Exception as erro:
        print(f'\033[1;31mERRO: {erro.__class__}\nO site {url} não está acessível no momento.\033[m')
    else:
        print(f'\033[1;32mConsegui acessar o site {url} com sucesso.\033[m')

verificar_site('https://www.pudim.com.br/')