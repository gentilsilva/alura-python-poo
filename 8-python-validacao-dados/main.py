import requests
from acesso_cep import BuscaEndereco

cep = "31620040"
objeto_cep = BuscaEndereco(cep)

#resposta: requests = requests.get("https://viacep.com.br/ws/01001000/json/"

json: dict[str, str, str]

json = objeto_cep.acessa_via_cep()
print(json)
