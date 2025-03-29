

from requests_html import HTMLSession

session = HTMLSession()

try:
    r = session.get('https://resultados.beneficiosestudiantiles.cl/login')
    r.html.render(sleep=2)

    if r.html is None:
        raise ValueError('El contenido es None')

    print(r.html.html)

except Exception as e:
    print('Se ha producido una excepcion', e)

r = session.get('https://resultados.beneficiosestudiantiles.cl/resultados?rut=21967064&recaptcha=03AFcWeA4iSf-lnNbLDUaZktHVyJbJuXvKWA7ij9hm52PW8aDE_gT99FTSkpDI9ptbmddZjKpA9NbKkw1eNh4vHcBMYKr3XZxTH2HDpyPgvD3FjNMcpZcNe68nqa9hMeQzksqJzGXtCfatwGXT_20BZaFwq158pV5ABmb0OwnRlAAC2OnhIkm4rVlYsJPA7iwuLdlDYwzPCL6D54Y_7wfxIlsbwS8qaJReDM64lkHasG6zZSWRsuhi2g1ZZOP28iTUhXEKM48bghqNukUSnvdID5wkcPXbRfeKUDFs--peMPHV0SXtnOnpVd_xphJZXz3kMZ0wcdv7Wy3iPL12Szx5Z7w-O9UpkPlPB9wuunE0RxRUa7ExEZ6q_V_Z9JlzZAScvwFZuFs9DjCWqQlnV6NH9WoFrFhn8llgkYGtjJKXus4sCA%E2%80%A6M3K7ZQ7kmD-tu3H2YWYEv9fJMwPkn5YDxoDW3kGSHZ2vUrZlr1TRXorgg4RBF5RJ5Y0VvD9TF-Fk55p0g4W13oxhQRcIy6G7Ql2dLWxRJBHAdy67usoDWUO2gEHbB6huAfrCQY-X7ZQM3lP4d5TAp54DGNbOvKlGK9cH_hKLuPcIkG3iT8Mld447W6vdtZ6lXgBZWFwV-vf4c4TmomEfXBMEGrt30DVL-CDanQZoqM4D24j2BpNGBbUvGhbGNPXypMpYzvKVPVYCvP9yluouNDnMA90b57F-jMco2ioSegrYMqXg2yI3vRje0_oXAEyrulLr1BKLBTrOAThTjboH8YKJHMZDxnqHRkvQ1O-kcUyxvPnVkfq988IUd4gjYT4IoGjroIK50g0H8P6pHw75hLoPITka6z2nW_qUMwA9e93IBHJFD-rmBfwGoYULjAqPMoLkgJSITHf48aaXGrzZRzkWUkVjfjhvsu2wau_olKqcB6_jWcRMGSiAgHw9mlbA')

texto = r.html.render(timeout=30)
print(texto.html.html)
