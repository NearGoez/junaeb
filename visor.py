import time
from edu22 import edu
from tempedu22 import edu as edu22
start = time.perf_counter()
from data import dicc




for key, value in edu.items():

    if 'Derecho' in value and 'Finis' in value: 
        if key in dicc.keys():
            pass
        else:
            print(key, value, f'EL RUT {key} NO ESTA EN LA BASE DE DATOS')



end = time.perf_counter()
print(end - start)

