# PEP8 OK
# -*- coding: utf-8 -*-

# ATENÇÃO! NÃO NOMEIE O ARQUIVO COM O NOME DA BIBLIOTECA (speedtest.py) POIS DA ERRO DE CIRCULAR IMPORT!!!!!
import speedtest

test = speedtest.Speedtest()

# download
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

# upload
upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

print(f'Download: {fDown} mb/s')
print(f'Upload: {fUp} mb/s')
