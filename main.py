from extrator_url import ExtratorURL


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
valor_quantidade = int(extrator_url.get_valor_parametro("quantidade"))
print("Valor a ser convertido: ", valor_quantidade)
print("Moeda origem: ", moeda_origem)
print("Moeda destino: ", moeda_destino)
valor_convertido = extrator_url.conversao(valor_quantidade, moeda_origem)
print(valor_convertido)

