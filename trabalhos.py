from bs4 import BeautifulSoup
import requests

# Objetivo: De tempo em tempo fazer varredura no site e verificar novos trabalhos

class Trabalhos:
    def __init__(self, url='https://www.vintepila.com.br/trabalhos-freelance/?page=2/'):
        self.url = url
        self.trabalhos = []
        self.soup = None
    
    def carregar_trabalhos(self):
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, 'html.parser')
                self.trabalhos = self.soup.findAll('a', class_='header')
            else:
                print(f'Erro ao carregar a página: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Erro ao carregar a página: {e}')

    def substituir(self, texto: str) -> str:
        texto = (texto.strip().replace('ç', 'c').replace('ã', 'a')
                 .replace('é', 'e').replace('õ', 'o').replace('–', '')
                 .replace('á', 'a').replace('ú', 'u').replace('í', 'i')
                 .replace('â', 'a').replace('ô', 'o'))
        return texto
    
    def organizar_frase(self, frase: str):
        listagem = frase.lower().split()
        frase = '-'.join([self.substituir(palavra) for palavra in listagem])
        return frase.rstrip('-')
    
    def procurar_trabalho(self, palavra: str):
        self.carregar_trabalhos()
        
        if not self.trabalhos:
            print('Nenhum trabalho encontrado')
            return
        
        encontrou = False  # Variável para monitorar se a palavra foi encontrada

        for trabalho in self.trabalhos:
            if trabalho.text and palavra.lower() in trabalho.text.lower():
                encontrou = True
                print(trabalho.text, end='\n')
                t = self.organizar_frase(trabalho.text)
                link = f'Link: https://www.vintepila.com.br/trabalhos-freelance/{t}'
                
                print(link, end='\n')
                

        # Imprime a mensagem de "não encontrado" se nenhum trabalho contiver a palavra-chave
        if not encontrou:
            print(f'Não encontrado palavra-chave: {palavra}')

if __name__ == '__main__':
    trabalho = Trabalhos()
    trabalho.procurar_trabalho('dev')
