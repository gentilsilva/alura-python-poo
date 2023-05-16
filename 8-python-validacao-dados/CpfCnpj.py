from validate_docbr import CPF, CNPJ


"""Classe factory"""
"""A partir dela, chamamos outras classes"""
class Documento:
    @staticmethod
    def cria_documento(documento: str):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!!")


class DocCpf:
    def __init__(self, documento: str):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!!!")

    def __str__(self):
        return self.format()

    def valida(self, documento: str):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara: CPF = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento: str):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!!!")

    def __str__(self):
        return self.format()

    def valida(self, documento: str):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara: CNPJ = CNPJ()
        return mascara.mask(self.cnpj)
