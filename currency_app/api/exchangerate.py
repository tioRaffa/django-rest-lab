import requests
from decouple import config
from pprint import pprint


def convert_currency(coin1, coin2, quantity):
    api_key = config('CURRENCY_KEY')
    if not api_key:
        print('Chave API não encontrada no arquivo .env!')
        return None
    
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{coin1}/{coin2}/{quantity}"

    try:
        response = requests.get(url=url)
        data = response.json() if response.status_code == 200 else None

        if data and data.get('result') == 'success':
            conversion = {}
            conversion['moeda_base'] = data.get('base_code')
            conversion['moeda_cotada'] = data.get('target_code')
            conversion['taxa_de_cambio'] = data.get('conversion_rate')
            conversion['valor convertido'] = data.get('conversion_result')
            conversion['ultima_atualização_da_taxa'] = data.get('time_last_update_utc')
            return conversion
        
        elif data and data.get('result') == 'error':
            print(f"Falha ao obter conversão: {data.get('error-type')}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')
        return None


if __name__ == "__main__":
    moeda = convert_currency('USD', 'BRL', 100)
    pprint(moeda)