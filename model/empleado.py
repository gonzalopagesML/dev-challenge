class Empleado:
    def __init__(self, nombre, salario_base, horas_trabajadas):
        self.nombre = nombre
        self.salario_base = salario_base
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_final(self):
        return self.salario_base * self.horas_trabajadas
