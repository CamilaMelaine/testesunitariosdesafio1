import re

class Validador:
    def validar_cpf(self, texto: str) -> bool:
        if not isinstance(texto, str):
            raise ValueError("Entrada deve ser uma string")

        cpf = re.sub(r'\D', '', texto)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        def calcular_digito(cpf, peso):
            soma = sum(int(digito) * p for digito, p in zip(cpf, peso))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        d1 = calcular_digito(cpf[:9], range(10, 1, -1))
        d2 = calcular_digito(cpf[:9] + d1, range(11, 1, -1))
        return cpf.endswith(d1 + d2)

    def validar_cnpj(self, texto: str) -> bool:
        if not isinstance(texto, str):
            raise ValueError("Entrada deve ser uma string")

        cnpj = re.sub(r'\D', '', texto)
        if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
            return False

        def calcular_digito(cnpj, pesos):
            soma = sum(int(digito) * peso for digito, peso in zip(cnpj, pesos))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1

        d1 = calcular_digito(cnpj[:12], pesos1)
        d2 = calcular_digito(cnpj[:12] + d1, pesos2)
        return cnpj.endswith(d1 + d2)

    def validar_cep(self, texto: str) -> bool:
        if not isinstance(texto, str):
            raise ValueError("Entrada deve ser uma string")

        cep = re.sub(r'\D', '', texto)
        return bool(re.fullmatch(r'\d{8}', cep))
