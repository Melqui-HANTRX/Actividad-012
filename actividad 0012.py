estudiantes = {}

try:
    cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))

    for i in range(1, cantidad + 1):
        print(f"\nEstudiante #{i}")
        nombre = input("Nombre: ")

        try:
            cant_notas = int(input("Cantidad de notas: "))
            if cant_notas <= 0:
                raise ZeroDivisionError("No se pueden ingresar 0 notas.")

            notas = []
            for j in range(1, cant_notas + 1):
                try:
                    nota = float(input(f"Nota #{j}: "))
                    notas.append(nota)
                except ValueError:
                    print("Error: La nota debe ser un número.")
                    nota = float(input(f"Vuelva a ingresar la nota #{j}: "))
                    notas.append(nota)
            promedio = sum(notas) / cant_notas
            estudiantes[nombre] = promedio

        except ValueError:
            print("Error: La cantidad de notas debe ser un número entero.")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except TypeError:
            print("Error: Se intentó realizar una operación inválida (número + texto).")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

except ValueError:
    print("Error: Debe ingresar un número entero para la cantidad de estudiantes.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
else:
    print("\nResultados:")
    for nombre, promedio in estudiantes.items():
        print(f"{nombre}: Promedio = {promedio:.2f}")
finally:
    print("\nPrograma finalizado.")


