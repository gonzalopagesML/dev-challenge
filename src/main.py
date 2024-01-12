from controller.controladores import ControladorEmpleado


def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    salario = float(input("Ingrese el salario base: "))
    horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    tipo_empleado = input(
        "Ingrese el tipo de empleado (Regular/Gerente/Director): "
        )

    bono = 0
    if tipo_empleado in ["Gerente", "Director"]:
        bono = float(input("Ingrese la bonificación: "))

    empleado = ControladorEmpleado.crear_empleado(
        nombre, salario, horas_trabajadas, tipo_empleado, bono
    )

    if empleado:
        print("Empleado agregado exitosamente.")
    else:
        print("Error al agregar empleado.")


def mostrar_salario():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    salario = ControladorEmpleado.obtener_salario(nombre_empleado)
    if salario is not None:
        print(f"El salario de {nombre_empleado} es: {salario}")
    else:
        print("Empleado no encontrado.")


def main():
    while True:
        print("1. Agregar Empleado")
        print("2. Mostrar Salario")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            mostrar_salario()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
