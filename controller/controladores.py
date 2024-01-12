from model.empleado_regular import EmpleadoRegular
from model.gerente import Gerente
from model.director import Director


class ControladorEmpleado:
    empleados = {}

    @staticmethod
    def crear_empleado(
        nombre, salario, horas_trabajadas, tipo_empleado, bono=0
    ):
        if tipo_empleado == "Regular":
            empleado = EmpleadoRegular(nombre, salario, horas_trabajadas)
        elif tipo_empleado == "Gerente":
            empleado = Gerente(nombre, salario, horas_trabajadas, bono)
        elif tipo_empleado == "Director":
            empleado = Director(nombre, salario, horas_trabajadas, bono)
        else:
            return None

        ControladorEmpleado.empleados[nombre] = empleado
        return empleado

    @staticmethod
    def obtener_salario(nombre_empleado):
        empleado = ControladorEmpleado.empleados.get(nombre_empleado)
        if empleado:
            return empleado.calcular_salario_final()
        else:
            return None
