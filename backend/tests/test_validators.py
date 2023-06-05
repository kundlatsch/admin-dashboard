import pytest
from admin_dashboard.validators import *

def test_valid_cpf_validator():
    # Valid cpfs generated with https://www.4devs.com.br/gerador_de_cpf
    valid_cpfs = ['322.241.460-27', '212.954.120-80', '048.525.190-64']
    is_valid = True
    for cpf in valid_cpfs:
        is_valid = validate_cpf(cpf)
    assert is_valid is True

def test_invalid_cpf_validator():
    invalid_cpfs = ['123456', '122.607.710-251', '35.833.230-71']
    is_valid = False
    for cpf in invalid_cpfs:
        is_valid = validate_cpf(cpf)
    assert is_valid is False

def test_rg_validator():
    rg = '12345678'
    valid = validate_rg(rg)
    rg = 'ab123456'
    invalid = validate_rg(rg)
    assert valid is True
    assert invalid is False

def test_date_validator():
    dates = ["26/09/1999", "26-09-1999", "1999/09/26"]
    valid = True
    for date in dates:
        valid = validate_date(date)
    assert valid is True
