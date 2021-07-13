import funciones
import main

while True:
    rol = input("\nBienvenido a PC'S GOSU, donde usted tiene el derecho de tener lo mejor. \n"
                "\n"
                "Soy:\n"
                "\n"
                "1. Admin\n"
                "2. Cliente\n"
                "3. Salir\n")

    # Salir

    if rol == "3":
        break

    # Admin

    elif rol == "1":
        while True:
            print("")
            print("*" * 130)
            print("")
            entra = input("Ingrese su opción:\n"
                          "1. Iniciar sesión\n"
                          "2. Salir\n")
            if entra == "2":
                break
            elif entra == "1":
                usu = input("Ingrese su nombre de usuario: ")
                contra = input("Ingrese su contraseña: ")
                if usu == "abrahamguzz" and contra == "1234" or usu == "rumpelstinsky" and contra == "4321":
                    while True:
                        n = (input("\n1. Ver Inventario\n"
                                   "2. Eliminar productos\n"
                                   "3. Agregar productos\n"
                                   "4. Informe de ventas\n"
                                   "5. Cerrar sesión\n"))

                        # Cerrar sesión

                        if n == "5":
                            break

                        # Ver Inventario

                        elif n == "1":
                            funciones.mostrar_inventario_cantidad()

                        # Eliminar productos

                        elif n == "2":
                            funciones.eliminar_producto()

                        # Agregar productos

                        elif n == "3":
                            funciones.agregar_producto()

                        # Informe de ventas

                        elif n == "4":
                            funciones.infor()

                else:
                    print("\nImgrese un usuario y contraseña válidos, por favor.\n")

    # Cliente

    elif rol == "2":
        while True:
            print("")
            print("*" * 130)
            print("")
            opc01 = input("Buenas, ¿En qué podemos ayudarle?:\n\n"
                          "1. Ver productos\n"
                          "2. Ver promociones\n"
                          "3. Hacer cotizaciones\n"
                          "5. Retroceder\n")
            # Retroceder
            if opc01 == "5":
                break
            # Ver Productos
            elif opc01 == "1":
                print(main.compopd)
                opc02 = input("¿Qué producto desea ver?\n")
                if opc02 == "0":
                    print(main.camarapd)
                elif opc02 == "1":
                    print(main.casepd)
                elif opc02 == "2":
                    opcdisc = input("\n¿En qué tipo de disco está interesado?\n"
                                    "1. SSD\n"
                                    "2. HDD\n")
                    if opcdisc == "1":
                        print(main.ssdpd)
                    elif opcdisc == "2":
                        print(main.hddpd)
                elif opc02 == "3":
                    print(main.fuentepd)
                elif opc02 == "4":
                    print(main.rampd)
                elif opc02 == "5":
                    print(main.monitorespd)
                elif opc02 == "6":
                    print(main.mousepd)
                elif opc02 == "7":
                    print(main.placapd)
                elif opc02 == "8":
                    opcdisc = input("\n¿En qué marca de procesador está interesado??\n"
                                    "1. Intel\n"
                                    "2. AMD\n")
                    if opcdisc == "1":
                        print(main.intelpd)
                    elif opcdisc == "2":
                        print(main.amdpd)
                elif opc02 == "9":
                    print(main.tarjvideopd)
                elif opc02 == "10":
                    print(main.tecladopd)

            # Promociones
            elif opc01 == "2":
                print("Tenemos las siguientes promociones:\n\n"
                      "Promoción 01")
                print(main.promocion01pd)
                print("\nPromoción 02")
                print(main.promocion02pd)
                print("\nPromoción 03")
                print(main.promocion03pd)
            # Lista de cotizaciones

            elif opc01 == "3":
                while True:
                    funciones.agregar_cot()
