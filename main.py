import trabalhos as tb
from time import sleep

trabalho = tb.Trabalhos()

pages = int(input('Quantas páginas: '))
word_key = input('Palavra Chave: ')

while pages > 0:
    trabalho.url = f'https://www.vintepila.com.br/trabalhos-freelance/?page={pages}/'
    print(f'Raspando página {pages} de {trabalho.url}\n')
    sleep(1)
    procurar = trabalho.procurar_trabalho(word_key)
    print()
    sleep(2)
    pages -= 1