import requests
from bs4 import BeautifulSoup
from fenixlib import data_doctor

DataDoctor = data_doctor

def PriceDigger(Urls, Classes, Tags, Swaps):
    for url in Urls:
        # Envia uma solicitação GET para a URL
        response = requests.get(url)
        
        # Verifica se a solicitação foi bem sucedida (código de status 200)
        if response.status_code == 200:
            # Parseia o conteúdo HTML da página usando BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontra o elemento que contém o preço (isso pode variar dependendo do site)
            price_element = soup.find(Tags, class_=Classes)
            
            # Extrai as urls e processa o nomes para receber um output User-Friendly          
            # Extrai o preço do elemento encontrado
            if price_element:
                price = price_element.text.strip()
                print(f'O preço do produto em {DataDoctor.QuickSwap(url, Swaps)} é: {price}')
            else:
                print(f'Não foi possível encontrar o preço do produto em {url}')
        else:
            print(f'Falha ao acessar {DataDoctor.QuickSwap(url, Swaps)}. Código de status: {response.status_code}')
