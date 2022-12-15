import requests

request = requests.get("https://mindicador.cl/api/uf")
request2 = requests.get("https://catfact.ninja/fact")

datos = request.json()

valoresuf = datos["serie"]
valorufayer = valoresuf[1]
valorufhoy = valoresuf[0]

datosRequest2 = request2.json()
datoGato = datosRequest2['fact']


print(f"Valor de la  Hoy: {valorufhoy['valor']}")
print(f"Valor de la  Ayer: {valorufayer['valor']}")

print(f"Dato ramdon de los Gatos: {datoGato}")
input("")