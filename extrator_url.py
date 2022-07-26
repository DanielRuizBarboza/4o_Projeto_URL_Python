import re  # Regular Expression -- RegEx


def sanitiza_url(url):
    if type(url) == str:
        return url.strip()
    else:
        return ""


class ExtratorURL:
    def __init__(self, url):
        self.url = sanitiza_url(url)
        self.valida_url()

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

        print("A URL é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametro = self.url[indice_interrogacao:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __str__(self):
        return f"{self.url} \nURL Base: {self.get_url_base()}\nParametros: {self.get_url_parametros()}"

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def conversao(valor_quantidade, origem):
        dolar = 5.50

        if "real" == origem:
            return f"{valor_quantidade} reais valem {valor_quantidade/dolar:.2f} dólares."
        else:
            return f"{valor_quantidade} dolares valem {valor_quantidade*dolar} reais."

