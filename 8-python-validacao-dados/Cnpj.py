from validate_docbr import CNPJ

class Cnpj:
    def __int__(self, documento: str):
        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.format_cnpf()

    def cnpj_eh_valido(self, cnpj: str):
        if len(cnpj) == 14:
             validador = CNPJ()
             return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos invalido!")
