import asyncio 
import time
import aiohttp
from bs4 import BeautifulSoup as bs

def digito(rut):
    value = 11 - sum([ int(a)*int(b) for a,b in zip(str(rut).zfill(8), '32765432')])%11
    return {10: 'K', 11: '0'}.get(value, str(value))


rut_inicial = 14000000

print(type(digito(rut_inicial)))

async def fetch_rut(rut:int, session):


async def main(rut_inicial):
    rut_actual = rut_inicial
    while True:
        async with aiohttp.ClientSession() as session:
            for i in range(80000):

                async with session.get('https://sinabweb.junaeb.cl/sinabweb/registro', ssl=False) as response:
                    html = await response.text()

                soup = bs(html, 'html.parser')
                token = soup.find('input', {'name': '_csrf'})['value']

                headers = {
                'x-csrf-token': token,
                }

                url_personal_info = 'https://sinabweb.junaeb.cl/sinabweb/registro/getPersonaInfo' 
                rut_str = f'{str(rut_actual)}-{digito(rut_actual)}'
                payload = {
                        'rut': '21885663-2',
                        }
                async with session.post(url_personal_info, data=payload, headers=headers, ssl=False) as response:
                    personal_info_json = await response.text()

                print(personal_info_json)
                rut_actual +=1


#asyncio.run(main(rut_inicial))

