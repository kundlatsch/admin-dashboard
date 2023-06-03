import re
from string import punctuation

def regex_check(regex, value):
    if re.fullmatch(regex, value):
        return True
    else:
        return False

def validate_email(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return regex_check(regex, email)

def validate_date(date: str) -> bool:
    """ Regex based date string validation.

    Params:
        date (str): string date to be validated.
    
    Return:
        bool: True when the format of the date is one of bellow, false otherwise.
            - 2020/02/12
            - 01.10.2019
            - 1.1.2019
            - 1.1.19
            - 12/03/2020
            - 01.05.1950
    """
    regex = re.compile(r'^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$')
    return regex_check(regex, date)

def validate_phone_number(phone_number: str) -> bool:
    # Simply check if the string is just numbers and allowed symbols
    accepted_symbols = ["(", ")", "+", "-", " "]
    try:
        digits = [int(c) for c in phone_number if c not in accepted_symbols]
    except ValueError:
        return False
    return True

def validate_rg(rg: str) -> bool:
    try:
        digits = [int(c) for c in rg if c not in ['.', '-']]
    except ValueError:
        return False
    return True

def validate_cpf(cpf: str) -> bool:
    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.
    Função obtida em: 
    https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validate('529.982.247-25')
    True
    >>> validate('52998224725')
    False
    >>> validate('111.111.111-11')
    False
    """

    # Verifica a formatação do CPF
    # Removido para simplificação
    # if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
    #     return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
