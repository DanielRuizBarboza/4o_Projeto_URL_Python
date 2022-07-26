import re

endereco = "Rua Cond Luiz Eduardo Matarazzo - 250, Apartamento CA12, Vila São Silvestre, São Paulo, SP, 53560-000"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)   # Match
if busca:
    cep = busca.group()
    print(cep)
