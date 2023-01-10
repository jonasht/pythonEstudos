from typing import ItemsView, final
import requests as r


url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)

print(resp.status_code)

raw_data = resp.json()

# print(raw_data[0])

final_data = []

for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

# mostrando o resultado
# print(final_data)
final_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

for dados in final_data:
    # print(dados)
    for dado in dados:
        print(f'{dado} ', end='')
    print()
# 