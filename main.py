import asyncio 
import time
import aiohttp
import json
from bs4 import BeautifulSoup as bs

def digito(rut):
    value = 11 - sum([ int(a)*int(b) for a,b in zip(str(rut).zfill(8), '32765432')])%11
    return {10: 'K', 11: '0'}.get(value, str(value))


rut_inicial = 22200000


async def fetch_rut(session,jsessionid, token, rut):
    rut_str = f'{rut}-{digito(rut)}'

    url = 'https://sinabweb.junaeb.cl/sinabweb/registro/getPersonaInfo'
    payload = {
            'rut': rut_str,
    }
    headers = {
            'X-CSRF-TOKEN': token,
            }
    cookies = {
            'JSESSIONID': jsessionid,
            }
    async with session.post(url, cookies=cookies, headers=headers, data=payload, ssl=False) as r:
        return await r.text()

async def main(rut_inicial):
    rut_actual = rut_inicial
    async with aiohttp.ClientSession() as session:
        print('Buscando token...')
        async with session.get('https://sinabweb.junaeb.cl/sinabweb/registro', ssl=False) as response:
            html = await response.text()
            jsessionid = response.cookies['JSESSIONID'].value

        soup = bs(html, 'html.parser')
        token = soup.find('input', {'name': '_csrf'})['value']
        print('Token listo:', token)
        
        print("Iniciando fetching de ruts")
        tasks = [fetch_rut(session, jsessionid, token, rut_inicial + i) for i in range(1)]
        resultados = await asyncio.gather(*tasks) 
        for resultado in resultados:
            print(resultado)


asyncio.run(main(rut_inicial))
