import pytest
from src.cnpj import CNPJ

@pytest.mark.parametrize("cnpj_input, esperado", [
    ("ABC123450001-91", False),
    ("AB.C12.345/0001-10", True),
    ("ABC12345000110", True),
    ("12.ABC.345/01DE-35", True),
    ("12.345.678/0001-95", True),
    ("12345678000195", True),
    ("12.345.678/0001", False),
    ("INV@LID-FORMAT", False),
    ("12.345.678/0001-00", False),
    ("111.111.111-11", False),
    ("", False),
    ("teste", False),
    ("00.000.000/0000-00", False),
    ("11.111.111/1111-11", False),
    ("22.222.222/2222-22", False),
    ("33.333.333/3333-33", False),
    ("44.444.444/4444-44", False),
    ("55.555.555/5555-55", False),
    ("66.666.666/6666-66", False),
    ("77.777.777/7777-77", False),
    ("88.888.888/8888-88", False),
    ("99.999.999/9999-99", False),
    ("00.000.000", False),
])
def test_validacao_cnpj_variados(cnpj_input, esperado):
    try:
        cnpj = CNPJ(cnpj_input)
        resultado = cnpj.valida()
    except ValueError:
        resultado = False

    print(f"Entrada: {cnpj_input} | Esperado: {esperado} | Obtido: {resultado}")
    assert resultado == esperado
