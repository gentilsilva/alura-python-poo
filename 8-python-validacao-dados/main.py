from CpfCnpj import Documento

exemplo_cnpj = "35379838000112"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)

exemplo_cpf = "74778773268"
documento_cpf = Documento.cria_documento(exemplo_cpf)

print(documento_cnpj)
print(documento_cpf)
