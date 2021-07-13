import listas
import main
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

listcotiid = []
listcotinombre = []
listcotiprecio = []
numberid = 67

cabeceros = ["ID", "Nombre", "Precios"]


def pandix(idd, name, precios):
    return tabulate(pd.DataFrame({"ID": idd,
                                  "Nombre": name,
                                  "Precios": precios}), headers=cabeceros, tablefmt='fancy_grid')


def mostrar(lis):
    a = 0
    for i in lis:
        a += 1
        print(str(a) + ". " + i)


def coman(x):
    com = input("\nUsted desea:\n"
                "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                "2. Ver la lista de cotización y regresar a elegir\n"
                "3. Imprimir lista de cotizaciòn con precio final y salir\n"
                )
    if com == "1":
        listas.listcoti.append(x)
        print("\nSu elemento ha sido añadido satisfactoriamente a su lista")
    elif com == "2":
        print("\nLISTA DE COTIZACIÒN:\n")
        for i in listas.listcoti:
            print(i)
    elif com == "3":
        print("")
        for i in listas.listcoti:
            print(i)


# Mostrar inventario


def mostrarinventario():
    print(main.compopd)
    opc02 = input("¿Qué producto desea ver?\n")
    if opc02 == "0":
        print(main.camarapd)
    elif opc02 == "1":
        print(main.casepd)
    elif opc02 == "2":
        opcdisc = input("\n¿Wué tipo de disco busca?\n"
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
        opcdisc = input("\n¿Qué marca de procesador busca?\n"
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


# Mostrar inventario con la cantidad de productos


def mostrar_inventario_cantidad():
    print(main.cantitotpd)
    opc02 = input("¿Qué producto desea ver especificamente?\n")
    if opc02 == "0":
        print(main.camaracantipd)
    elif opc02 == "1":
        print(main.casecantipd)
    elif opc02 == "2":
        opcdisc = input("\n¿Wué tipo de disco?\n"
                        "1. SSD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print(main.ssdcantipd)
        elif opcdisc == "2":
            print(main.hddcantipd)
    elif opc02 == "3":
        print(main.fuentecantipd)
    elif opc02 == "4":
        print(main.ramcantipd)
    elif opc02 == "5":
        print(main.monitorescantipd)
    elif opc02 == "6":
        print(main.mousecantipd)
    elif opc02 == "7":
        print(main.placacantipd)
    elif opc02 == "8":
        opcdisc = input("\n¿Marca del procesador?\n"
                        "1. Intel\n"
                        "2. AMD\n")
        if opcdisc == "1":
            print(main.intelcantipd)
        elif opcdisc == "2":
            print(main.amdcantipd)
    elif opc02 == "9":
        print(main.tarjvideocantipd)
    elif opc02 == "10":
        print(main.tecladocantipd)


def eliminar_producto():
    print(main.cantitotpd)
    opc02 = input("¿Qué producto desea eliminar?\n")
    if opc02 == "0":
        print(main.camaracantipd)
        elim = input("\nEscriba la id del producto que desee eliminar: ")
        numelim = int(input("Escriba cuántos productos desea eliminar: "))
        listas.camwebcanti.remove(elim)
        print("")
        print(numelim)
        print(main.camaracantipd)
    elif opc02 == "1":
        print(main.casecantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.caseid.append(newid)
        listas.case.append(newnombre)
        listas.caseprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.camwebcanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.casepd)
    elif opc02 == "2":
        opcdisc = input("\n¿Wué tipo de disco?\n"
                        "1. SSD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print(main.ssdcantipd)
            newid = "0" + str(numberid)
            newnombre = input("Ingrese el nombre del producto: ")
            newprecio = input("Ingrese el precio en S/: ")
            newcanti = int(input("ingrese la cantidad de productos: "))
            listas.ssdid.append(newid)
            listas.ssd.append(newnombre)
            listas.ssdprecios.append(newprecio)
            for i in range(0, newcanti):
                listas.ssdcanti.append(newid)
            print("\nSu producto fue añadido con éxito.\n")
            print(main.ssdpd)
        elif opcdisc == "2":
            print(main.hddcantipd)
            newid = "0" + str(numberid)
            newnombre = input("Ingrese el nombre del producto: ")
            newprecio = input("Ingrese el precio en S/: ")
            newcanti = int(input("ingrese la cantidad de productos: "))
            listas.hddid.append(newid)
            listas.hdd.append(newnombre)
            listas.hddprecios.append(newprecio)
            for i in range(0, newcanti):
                listas.hddcanti.append(newid)
            print("\nSu producto fue añadido con éxito.\n")
            print(main.hddpd)
    elif opc02 == "3":
        print(main.fuentecantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.fuenteid.append(newid)
        listas.fuente.append(newnombre)
        listas.fuenteprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.fuentecanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.fuentepd)
    elif opc02 == "4":
        print(main.ramcantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.ramid.append(newid)
        listas.ram.append(newnombre)
        listas.ramprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.ramcanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.rampd)
    elif opc02 == "5":
        print(main.monitorescantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.monitoresid.append(newid)
        listas.monitores.append(newnombre)
        listas.monitoresprecio.append(newprecio)
        for i in range(0, newcanti):
            listas.monitorescanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.monitorespd)
    elif opc02 == "6":
        print(main.mousecantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.mouseid.append(newid)
        listas.mouse.append(newnombre)
        listas.mouseprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.mousecanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.mousepd)
    elif opc02 == "7":
        print(main.placacantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.placaid.append(newid)
        listas.placa.append(newnombre)
        listas.placaprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.placacanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.placapd)
    elif opc02 == "8":
        opcdisc = input("\n¿Marca del procesador?\n"
                        "1. Intel\n"
                        "2. AMD\n")
        if opcdisc == "1":
            print(main.intelcantipd)
            newid = "0" + str(numberid)
            newnombre = input("Ingrese el nombre del producto: ")
            newprecio = input("Ingrese el precio en S/: ")
            newcanti = int(input("ingrese la cantidad de productos: "))
            listas.intelid.append(newid)
            listas.intel.append(newnombre)
            listas.intelprecios.append(newprecio)
            for i in range(0, newcanti):
                listas.intelcanti.append(newid)
            print("\nSu producto fue añadido con éxito.\n")
            print(main.intelpd)
        elif opcdisc == "2":
            print(main.amdcantipd)
            newid = "0" + str(numberid)
            newnombre = input("Ingrese el nombre del producto: ")
            newprecio = input("Ingrese el precio en S/: ")
            newcanti = int(input("ingrese la cantidad de productos: "))
            listas.amdid.append(newid)
            listas.amd.append(newnombre)
            listas.amdprecios.append(newprecio)
            for i in range(0, newcanti):
                listas.amdcanti.append(newid)
            print("\nSu producto fue añadido con éxito.\n")
            print(main.amdpd)
    elif opc02 == "9":
        print(main.tarjvideocantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.tarjvideoid.append(newid)
        listas.tarjvideo.append(newnombre)
        listas.tarjvideoprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.tarjvideocanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.tarjvideopd)
    elif opc02 == "10":
        print(main.tecladocantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.tecladoid.append(newid)
        listas.teclado.append(newnombre)
        listas.tecladoprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.tecladocanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.tecladopd)


# Agregar producto


def agregar_producto():
    print("¿Qué tipo de componente desea agregar?")
    print(main.compopd)
    opc02 = input("\n")
    if opc02 == "0":
        print(main.camaracantipd)
        newid = "0" + str(numberid)
        newnombre = input("Ingrese el nombre del producto: ")
        newprecio = input("Ingrese el precio en S/: ")
        newcanti = int(input("ingrese la cantidad de productos: "))
        listas.camwebid.append(newid)
        listas.camweb.append(newnombre)
        listas.camwebprecios.append(newprecio)
        for i in range(0, newcanti):
            listas.camwebcanti.append(newid)
        print("\nSu producto fue añadido con éxito.\n")
        print(main.camarapd)
    elif opc02 == "1":
        print(main.casecantipd)
    elif opc02 == "2":
        opcdisc = input("\n¿Qué tipo de disco?\n"
                        "1. SSD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print(main.ssdcantipd)
        elif opcdisc == "2":
            print(main.hddcantipd)
    elif opc02 == "3":
        print(main.fuentecantipd)
    elif opc02 == "4":
        print(main.ramcantipd)
    elif opc02 == "5":
        print(main.monitorescantipd)
    elif opc02 == "6":
        print(main.mousecantipd)
    elif opc02 == "7":
        print(main.placacantipd)
    elif opc02 == "8":
        opcdisc = input("\n¿Marca del procesador?\n"
                        "1. Intel\n"
                        "2. AMD\n")
        if opcdisc == "1":
            print(main.intelcantipd)
        elif opcdisc == "2":
            print(main.amdcantipd)
    elif opc02 == "9":
        print(main.tarjvideocantipd)
    elif opc02 == "10":
        print(main.tecladocantipd)


# Agregar a lista de cotización


def agregar_cot():
    print("\nElija el componente que quiere que tenga su PC:\n")
    print(main.compopd)
    opc02 = input()
    if opc02 == "0":
        print("\nTenemos estas cámaras web disponibles, por favor, elija una, escribiendo su id:")
        print(main.camarapd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.camweb[listas.camwebid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.camweb[listas.camwebid.index(elegir)])
            listcotiprecio.append(listas.camwebprecios[listas.camwebid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.camweb[listas.camwebid.index(elegir)])
            listcotiprecio.append(listas.camwebprecios[listas.camwebid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))

    elif opc02 == "1":
        print("\nTenemos estos cases disponibles, por favor, elija uno, escribiendo su id:")
        print(main.casepd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.case[listas.caseid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.case[listas.caseid.index(elegir)])
            listcotiprecio.append(listas.caseprecios[listas.caseid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.case[listas.caseid.index(elegir)])
            listcotiprecio.append(listas.caseprecios[listas.caseid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "2":
        opcdisc = input("\nElija un tipo de disco duro:\n"
                        "1. SDD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print("\nEstos son los discos SSD disponibles, por favor elija uno escribiendo el id:")
            print(main.ssdpd)
            elegir = input("\n")
            print("\nEl elemento elegido es: ", listas.ssd[listas.ssdid.index(elegir)])
            opc04 = input("\nUsted desea:\n"
                          "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                          "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
            if opc04 == "1":
                listcotiid.append(elegir)
                listcotinombre.append(listas.ssd[listas.ssdid.index(elegir)])
                listcotiprecio.append(listas.ssdprecios[listas.ssdid.index(elegir)])
                print("El elemento fue añadido a la lista exitosamente.\n")
            elif opc04 == "2":
                listcotiid.append(elegir)
                listcotinombre.append(listas.ssd[listas.ssdid.index(elegir)])
                listcotiprecio.append(listas.ssdprecios[listas.ssdid.index(elegir)])
                listcotiid.append("---")
                listcotinombre.append("PRECIO TOTAL")
                preciofinal = 0
                for i in listcotiprecio:
                    preciofinal += float(i)
                listcotiprecio.append(str(preciofinal))
                print(pandix(listcotiid, listcotinombre, listcotiprecio))
        elif opcdisc == "2":
            print("\nEstos son los discos HDD disponibles, por favor elija uno escribiendo el id:")
            print(main.hddpd)
            elegir = input("\n")
            print("\nEl elemento elegido es: ", listas.hdd[listas.hddid.index(elegir)])
            opc04 = input("\nUsted desea:\n"
                          "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                          "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
            if opc04 == "1":
                listcotiid.append(elegir)
                listcotinombre.append(listas.hdd[listas.hddid.index(elegir)])
                listcotiprecio.append(listas.hddprecios[listas.hddid.index(elegir)])
                print("El elemento fue añadido a la lista exitosamente.\n")
            elif opc04 == "2":
                listcotiid.append(elegir)
                listcotinombre.append(listas.hdd[listas.hddid.index(elegir)])
                listcotiprecio.append(listas.hddprecios[listas.hddid.index(elegir)])
                listcotiid.append("---")
                listcotinombre.append("PRECIO TOTAL")
                preciofinal = 0
                for i in listcotiprecio:
                    preciofinal += float(i)
                listcotiprecio.append(str(preciofinal))
                print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "3":
        print("\nTenemos estas fuentes de poder disponibles, por favor elija una escribiendo el id:")
        print(main.fuentepd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.fuente[listas.fuenteid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.fuente[listas.fuenteid.index(elegir)])
            listcotiprecio.append(listas.fuente[listas.fuenteid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.fuente[listas.fuenteid.index(elegir)])
            listcotiprecio.append(listas.fuente[listas.fuenteid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "4":
        print("\nTenemos estas memorias RAM disponibles, por favor elija una escribiendo el id:")
        print(main.rampd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.ram[listas.ramid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.ram[listas.ramid.index(elegir)])
            listcotiprecio.append(listas.ramprecios[listas.ramid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.ram[listas.ramid.index(elegir)])
            listcotiprecio.append(listas.ramprecios[listas.ramid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "5":
        print("\nTenemos estos monitores disponibles, por favor elija uno escribiendo el id:")
        print(main.monitorespd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.monitores[listas.monitoresid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.monitores[listas.monitoresid.index(elegir)])
            listcotiprecio.append(listas.monitores[listas.monitoresid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.monitores[listas.monitoresid.index(elegir)])
            listcotiprecio.append(listas.monitores[listas.monitoresid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "6":
        print("\nTenemos estos mouses disponibles, por favor elija uno escribiendo el id:")
        print(main.mousepd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.mouse[listas.mouseid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.mouse[listas.mouseid.index(elegir)])
            listcotiprecio.append(listas.mouse[listas.mouseid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.mouse[listas.mouseid.index(elegir)])
            listcotiprecio.append(listas.mouse[listas.mouseid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "7":
        print("\nTenemos estas placas madre disponibles, por favor elija una escribiendo el id:")
        print(main.placapd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.placa[listas.placaid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.placa[listas.placaid.index(elegir)])
            listcotiprecio.append(listas.placaprecios[listas.placaid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.placa[listas.placaid.index(elegir)])
            listcotiprecio.append(listas.placaprecios[listas.placaid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "8":
        opcproce = input("\nPor favor elija una marca de procesador:\n"
                         "1. Intel\n"
                         "2. AMD\n")
        if opcproce == "1":
            print("Estos son los procesadores Intel disponibles, por favor elija uno escribiendo el id:")
            elegir = input("\n")
            print("\nEl elemento elegido es: ", listas.intel[listas.intelid.index(elegir)])
            opc04 = input("\nUsted desea:\n"
                          "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                          "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
            if opc04 == "1":
                listcotiid.append(elegir)
                listcotinombre.append(listas.intel[listas.intelid.index(elegir)])
                listcotiprecio.append(listas.intelprecios[listas.intelid.index(elegir)])
                print("El elemento fue añadido a la lista exitosamente.\n")
            elif opc04 == "2":
                listcotiid.append(elegir)
                listcotinombre.append(listas.intel[listas.intelid.index(elegir)])
                listcotiprecio.append(listas.intelprecios[listas.intelid.index(elegir)])
                listcotiid.append("---")
                listcotinombre.append("PRECIO TOTAL")
                preciofinal = 0
                for i in listcotiprecio:
                    preciofinal += float(i)
                listcotiprecio.append(str(preciofinal))
                print(pandix(listcotiid, listcotinombre, listcotiprecio))
        elif opcproce == "2":
            print("Estos son los procesadores AMD disponibles, por favor elija uno escribiendo el id:")
            print(main.amdpd)
            elegir = input("\n")
            print("\nEl elemento elegido es: ", listas.amd[listas.amdid.index(elegir)])
            opc04 = input("\nUsted desea:\n"
                          "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                          "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
            if opc04 == "1":
                listcotiid.append(elegir)
                listcotinombre.append(listas.amd[listas.amdid.index(elegir)])
                listcotiprecio.append(listas.amdprecios[listas.amdid.index(elegir)])
                print("El elemento fue añadido a la lista exitosamente.\n")
            elif opc04 == "2":
                listcotiid.append(elegir)
                listcotinombre.append(listas.amd[listas.amdid.index(elegir)])
                listcotiprecio.append(listas.amdprecios[listas.amdid.index(elegir)])
                listcotiid.append("---")
                listcotinombre.append("PRECIO TOTAL")
                preciofinal = 0
                for i in listcotiprecio:
                    preciofinal += float(i)
                listcotiprecio.append(str(preciofinal))
                print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "9":
        print("\nTenemos estas tarjetas de video disponibles, por favor elija una escribiendo el id:")
        print(main.tarjvideopd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.tarjvideo[listas.tarjvideoid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.tarjvideo[listas.tarjvideoid.index(elegir)])
            listcotiprecio.append(listas.tarjvideoprecios[listas.tarjvideoid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.tarjvideo[listas.tarjvideoid.index(elegir)])
            listcotiprecio.append(listas.tarjvideoprecios[listas.tarjvideoid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))
    elif opc02 == "10":
        print("\nTenemos estos teclados disponibles, por favor elija uno escribiendo el id:")
        print(main.tecladopd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.teclado[listas.tecladoid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Añadir elemento y ver la lista de cotización final y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.teclado[listas.tecladoid.index(elegir)])
            listcotiprecio.append(listas.teclado[listas.tecladoid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append(elegir)
            listcotinombre.append(listas.teclado[listas.tecladoid.index(elegir)])
            listcotiprecio.append(listas.teclado[listas.tecladoid.index(elegir)])
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))


# Información estadística

tiempo = ["enero", "febrero", "marzo", "abril", "mayo"]
ganancias = [1200, 900, 2000, 400, 600]
gastos = [600, 500, 1500, 700, 500]
usopro = [12, 13, 20, 35, 20, 25, 10, 2, 7, 19, 48]
colors = ["red", "green", "blue", "cyan", "black", "red", "green", "blue", "cyan", "black", "Magenta"]


def chart_bar(tiem, ganan, r, titu):
        fig, ax = plt.subplots()
        rects1 = ax.bar(tiem, ganan, color=r)
        ax.set_title(titu, color="black")
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Ganancias')
        ax.bar_label(rects1, padding=3)
        plt.savefig('chart_bar_green.pdf')
        plt.show()


def infor():
    while True:
        info = input("\n¿Qué desea ver?\n"
                     "1. Gastos\n"
                     "2. Ganancias\n"
                     "3. Productos vendidos en el año\n"
                     "4. Retroceder\n")
        if info == "1":
            chart_bar(tiempo, gastos, "red", 'GASTOS DE ENERO A MAYO DEL 2021')
        elif info == "2":
            chart_bar(tiempo, ganancias, "green", 'GANANCIAS DE ENERO A MAYO DEL 2021')
        elif info == "3":
            chart_bar(listas.componentes, usopro, colors, 'PRODUCTOS MÁS VENDIDOS EN MAYO DEL 2021')
        elif info == "4":
            break
