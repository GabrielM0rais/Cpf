import re
from random import randint


class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self.OnlyNumbers(cpf)

    @staticmethod
    def OnlyNumbers(cpf):
        return re.sub('[^0-9]', '', cpf)

    @staticmethod
    def calculo(cpfPart):
        if not cpfPart:
            return False

        aux = cpfPart[0] * len(cpfPart)

        if aux == cpfPart:
            return False

        sum = 0

        for key, idx in enumerate(range(len(cpfPart) + 1, 1, -1)):
            sum += int(cpfPart[key]) * idx

        rest = 11 - (sum % 11)
        rest = rest if rest <= 9 else 0

        return cpfPart + str(rest)

    @staticmethod
    def Generator():
        cpf = [randint(0, 9) for x in range(9)]

        for _ in range(2):
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

            cpf.append(11 - val if val > 1 else 0)

        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

    def Validate(self):
        if not self.cpf:
            return False

        newCpf = self.calculo(self.cpf[:9])
        newCpf = self.calculo(newCpf)

        if newCpf == self.cpf:
            return True
        return False
