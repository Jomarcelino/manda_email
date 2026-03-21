import re
from src.dv import DigitoVerificador

class CNPJ:
    def __init__(self, _input_cnpj: str):
        self.cnpj = self.__remove_pontuacao(_input_cnpj)

        if not self.__valida_formato(self.cnpj):
            raise ValueError("Formato inválido de CNPJ")

    def __remove_digitos_cnpj(self):
        if len(self.cnpj) == 14:
            self.cnpj_sem_dv = self.cnpj[:-2]
        elif len(self.cnpj) == 12:
            self.cnpj_sem_dv = self.cnpj
        else:
            raise ValueError("CNPJ com tamanho inválido")

    def __remove_pontuacao(self, _input: str) -> str:
        return re.sub(r"[^A-Z0-9]", "", _input.upper())

    def valida(self) -> bool:
        if self.cnpj == self.cnpj[0] * len(self.cnpj):
            return False

        self.__remove_digitos_cnpj()
        dv = self.gera_dv()
        return f"{self.cnpj_sem_dv}{dv}" == self.cnpj

    def gera_dv(self) -> str:
        self.__remove_digitos_cnpj()
        dv1 = DigitoVerificador(self.cnpj_sem_dv).calcula()
        dv2 = DigitoVerificador(self.cnpj_sem_dv + str(dv1)).calcula()
        return f"{dv1}{dv2}"

    def __valida_formato(self, _cnpj: str) -> bool:
        return re.match(r'^([A-Z0-9]{12}|[A-Z0-9]{14})$', _cnpj) is not None
