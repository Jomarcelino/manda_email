def validar_cpf(cpf):
    # Remove pontos e traços
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais
    if cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    # Verifica se os dígitos calculados conferem
    return cpf[-2:] == f"{digito1}{digito2}"


# Exemplo de uso
cpf = input("Digite um CPF: ")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
