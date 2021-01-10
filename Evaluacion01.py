import os
opcion=""
plan1=""
plan2=""
plan3=""
valor_plan=0;total=0; valor_plan1=0; valor_plan2=0; valor_plan3=0;contratados=0;uno=0;dos=0;tres=0


def menuPrincipal():
    os.system('cls')
    
    print("=*=*=*=*=*=*=* Menu inicial =*=*=*=*=*=*=*\n")
    print("Seleccione una opción")
    print("[1] - Ingresar precios de los planes")
    print("[2] - Realizar la contratación del plan")
    print("[3] - Cierre de turno")
    print("[4] - Salir")
    return


def menuPlan(plan1,plan2,plan3):
    os.system('cls')
    
    print("=*=*=*=*=*=*=* Bienvenido a Nesfli =*=*=*=*=*=*=*\n")
    print("Seleccione su plan a contratar")
    print(f"[1] - Plan 2 pantallas ${plan1}")
    print(f"[2] - Plan 5 pantallas Full HD ${plan2}")
    print(f"[3] - Plan Ilimitado ${plan3}")
    print("[4] - Salir")
    return    
    
    
def menuCierre(valor_plan1,valor_plan2,valor_plan3):
    os.system('cls')
    
    print("=*=*=*=*=*=*=* Menu de Cierre =*=*=*=*=*=*=*\n")
    print("Total de recaudación por los pagos de los planes que han sido contratos\n")
    print(f"Plan 2 pantallas ${valor_plan1}, cantidad vendida {uno} planes")
    print(f"Plan 5 pantallas Full HD ${valor_plan2}, cantidad vendida {dos} planes")
    print(f"Plan Ilimitado ${valor_plan3}, cantidad vendida {tres} planes")
    print(f"---------------------------------------------------------\nSe han vendido en total {contratados} planes\n")
    print("Las ventas Totales son: ",int(valor_plan1)+int(valor_plan2)+int(valor_plan3))
    print("")
    input("Presione una tecla para continuar....")
    return

while True:
    menuPrincipal()    
    opcion = input("Ingrese el numero correspondiente a la opcion que desea >>>> ")

    if opcion == "1":
        os.system('cls')
        
        print("=*=*=*=*=*=*=* Configuración de valores =*=*=*=*=*=*=*\nAsigne los valores correspondientes a los planes\n")
        print("Plan 2 pantallas HD")
        plan1 = input(": ")
        if int(plan1)<1:
            print("Valor ingresado es incorrecto")
        else:
            print("\nPlan 5 pantallas Full HD")
            plan2 = input(": ")
            if int(plan2)<1:
                print("Valor ingresado es incorrecto")
            else:
                print("\nPlan Ilimitado")
                plan3 = input(": ")
                if int(plan3)<1:
                    print("Valor ingresado es incorrecto")
                else:
                    print("===============================")
                    print(f"Planes Registrados correctamente\nPlan 2 pantallas HD ${plan1}\nPlan 5 pantallas Full HD ${plan2}\nPlan Ilimitado ${plan3}\n===============================")
                    print("")
                    input("Presione una tecla para continuar....")
        
    elif opcion=="2":        
        menuPlan(plan1,plan2,plan3)
        plan=input("Ingrese el numero correspondiente al plan >>>> ")
        if plan=="1":
            cantidad_planes=int(input("¿Cuantos planes contratará?: "))
            if cantidad_planes<=0:
                input("Cantidad ingresada es invalida")
            else:
                print(f"Usted a contratado {cantidad_planes} del plan n°2 con valor {plan1} mensual\nTotal a Pagar mensualmente: $",int(plan1)*cantidad_planes)
                valor_plan1+=int(plan1)*cantidad_planes
                contratados+=cantidad_planes
                uno+=cantidad_planes
                input("\nPresione una tecla para continuar....")
            
        elif plan=="2":
            cantidad_planes=int(input("¿Cuantos planes contratará?: "))
            if cantidad_planes<=0:
                input("Cantidad ingresada es invalida")
            else:
                print(f"Usted a contratado {cantidad_planes} del plan n°3 con valor {plan2} mensual\nTotal a Pagar mensualmente: $",int(plan2)*cantidad_planes)
                valor_plan2+=int(plan2)*cantidad_planes
                contratados+=cantidad_planes
                dos+=cantidad_planes
                input("\nPresione una tecla para continuar....")        
            
        elif plan=="3":
            cantidad_planes=int(input("¿Cuantos planes contratará?: "))
            if cantidad_planes<=0:
                input("Cantidad ingresada es invalida")
            else:
                print(f"Usted a contratado {cantidad_planes} del plan n°1 con valor {plan3} mensual\nTotal a Pagar mensualmente: $",int(plan3)*cantidad_planes)
                valor_plan3+=int(plan3)*cantidad_planes
                contratados+=cantidad_planes
                tres+=cantidad_planes
                input("\nPresione una tecla para continuar....")  
                      
        elif int(plan) > 4 or int(plan) < 0:
            print("Ha ingresado una opcion incorrecta")
            input("Presione una tecla para continuar....")
        
    elif opcion=="3":
        menuCierre(valor_plan1,valor_plan2,valor_plan3)
    elif int(opcion) > 4 or int(opcion) < 0:
        print("Ha ingresado una opcion incorrecta")
        input("Presione una tecla para continuar....")
    else:
        print("Hasta Pronto, gracias por preferir nesfli")
        break
        
    
