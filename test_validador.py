import pytest
from validador import Validador

@pytest.fixture
def validador():
    return Validador()

# ---------------------------
# Testes para validar_cpf
# ---------------------------

@pytest.mark.parametrize("cpf_valido", [
    "529.982.247-25",
    "52998224725",
    "111.444.777-35"
])
def test_validar_cpf_valido(validador, cpf_valido):
    assert validador.validar_cpf(cpf_valido) is True

@pytest.mark.parametrize("cpf_invalido", [
    "123.456.789-00",
    "00000000000",
    "11111111111",
    "1234567890",     # Menos dígitos
    "123456789012",   # Mais dígitos
])
def test_validar_cpf_invalido(validador, cpf_invalido):
    assert validador.validar_cpf(cpf_invalido) is False

@pytest.mark.parametrize("entrada", [None, 12345678901, 5.5, [], {}])
def test_validar_cpf_tipo_invalido(validador, entrada):
    with pytest.raises(ValueError):
        validador.validar_cpf(entrada)

# ---------------------------
# Testes para validar_cnpj
# ---------------------------

@pytest.mark.parametrize("cnpj_valido", [
    "04.252.011/0001-10",
    "04252011000110",
    "11.444.777/0001-61"
])
def test_validar_cnpj_valido(validador, cnpj_valido):
    assert validador.validar_cnpj(cnpj_valido) is True

@pytest.mark.parametrize("cnpj_invalido", [
    "00.000.000/0000-00",
    "12345678000100",
    "11111111111111",
    "1234567890",     # Menos dígitos
    "123456789012345" # Mais dígitos
])
def test_validar_cnpj_invalido(validador, cnpj_invalido):
    assert validador.validar_cnpj(cnpj_invalido) is False

@pytest.mark.parametrize("entrada", [None, 12345678000100, 3.14, True, []])
def test_validar_cnpj_tipo_invalido(validador, entrada):
    with pytest.raises(ValueError):
        validador.validar_cnpj(entrada)

# ---------------------------
# Testes para validar_cep
# ---------------------------

@pytest.mark.parametrize("cep_valido", [
    "01001-000",
    "30110-028",
    "01001000",
    "99999999"
])
def test_validar_cep_valido(validador, cep_valido):
    assert validador.validar_cep(cep_valido) is True

@pytest.mark.parametrize("cep_invalido", [
    "1234-567",       # Menos dígitos
    "abcdefgh",       # Letras
    "010010000",      # 9 dígitos
    "0000000"         # 7 dígitos
])
def test_validar_cep_invalido(validador, cep_invalido):
    assert validador.validar_cep(cep_invalido) is False

@pytest.mark.parametrize("entrada", [None, 12345678, 3.14, {}, []])
def test_validar_cep_tipo_invalido(validador, entrada):
    with pytest.raises(ValueError):
        validador.validar_cep(entrada)
