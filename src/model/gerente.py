from .empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, horas_trabajadas, bono):
        super().__init__(nombre, salario_base, horas_trabajadas)
        self.bono = bono

    def calcular_salario_final(self):
        return super().calcular_salario_final() + self.bono
