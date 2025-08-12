propietarios = {}

n = int(input("¿Cuántos propietarios desea registrar?: "))

for i in range(1, n + 1):
    print(f"\nPropietario num-{i}")
    nit = input("Identificación (NIT): ")
    nombre = input("Nombre completo: ")
    telefono = input("Teléfono: ")
    cant_vehiculos = int(input("Cantidad de vehículos: "))

    vehiculos = {}
    for j in range(1, cant_vehiculos + 1):
        print(f"\nVehículo cant-{j}")
        placa = input("Placa: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = int(input("Año: "))
        impuesto = input("¿Pagó el impuesto? (Sí/No): ").capitalize()

        vehiculos[placa] = {
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "impuesto_pagado": impuesto
        }

    propietarios[nit] = {
        "nombre": nombre,
        "telefono": telefono,
        "vehiculos": vehiculos
    }

print("\nResumen de propietarios:")
for nit, datos in propietarios.items():
    print(f"\nIdentificación: {nit}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Teléfono: {datos['telefono']}")
    print("Vehículos:")
    for placa, info in datos["vehiculos"].items():
        print(f"- Placa: {placa} | {info['marca']} {info['modelo']} ({info['año']}) | Impuesto: {info['impuesto_pagado']}")

buscar_nit = input("\nBuscar propietario por identificación (NIT): ")
if buscar_nit in propietarios:
    datos = propietarios[buscar_nit]
    print(f"\nIdentificación: {buscar_nit}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Teléfono: {datos['telefono']}")
    print("Vehículos:")
    for placa, info in datos["vehiculos"].items():
        print(f"- Placa: {placa} | {info['marca']} {info['modelo']} ({info['año']}) | Impuesto: {info['impuesto_pagado']}")
else:
    print("Propietario no encontrado.")

pagados = 0
no_pagados = 0

for datos in propietarios.values():
    for info in datos["vehiculos"].values():
        if info["impuesto_pagado"].lower() == "sí":
            pagados += 1
        else:
            no_pagados += 1

print(f"\nTotal de vehículos con impuesto pagado: {pagados}")
print(f"Total de vehículos sin pagar: {no_pagados}")

