
import requests
from bs4 import BeautifulSoup

url = "https://www.bna.com.ar/Personas"
response = requests.get(url)

cotizaciones={}

def obtener_cotizacion():
    
    tabla_cotizacion = soup.find('table', class_="table cotizacion")
    filas = tabla_cotizacion.find_all('tr')

    for fila in filas[1:]:
        celdas = fila.find_all('td')
        moneda = celdas[0].text.strip()
        if moneda in ['Dolar U.S.A','Euro']:
            compra = float(celdas[1].text.strip().replace(',', '.'))
            venta = float(celdas[2].text.strip().replace(',', '.'))
            cotizaciones[moneda]=[compra, venta]
    return cotizaciones

if response.status_code==200:
    soup = BeautifulSoup(response.content, 'html.parser')
    cotizaciones_obtenidas = obtener_cotizacion()
    compra_dolar = cotizaciones_obtenidas['Dolar U.S.A'][0]
    venta_dolar = cotizaciones_obtenidas['Dolar U.S.A'][1]
    compra_euro = cotizaciones_obtenidas['Euro'][0]
    venta_euro = cotizaciones_obtenidas['Euro'][1]
else:
    print("Error:", response.status_code)

class Usuario:
    def __init__(self, dni, nombre, apellido, clave, plan):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave
        self.plan = plan
        self.saldo_pesos = 10000
        self.saldo_dolares = 1000
        self.saldo_euros = 1000
        
    def depositar_pesos(self, monto):
        self.saldo_pesos+=monto
        print('\nSe depositaron $',monto,'ARS')
    def depositar_dolares(self, monto):
        self.saldo_dolares+=monto
        print('\nSe depositaron $',monto,'USD')
    def depositar_euros(self, monto):
        self.saldo_euros+=monto
        print('\nSe depositaron $',monto,'EUR')
            
    def retirar_dinero(self, monto, moneda):
        if monto <= getattr(self, f'saldo_{moneda}'):
            setattr(self, f'saldo_{moneda}', getattr(self, f'saldo_{moneda}') - monto)
            print(f"Se han retirado ${monto} {moneda}.")
        else:
            print('\nFondos insuficientes en esa moneda.')
            
    def monedas_disponibles(self):
        if self.plan == '1':
            return ['pesos']
        elif self.plan == '2':
            return ['pesos', 'dolares']
        else:
            return ['pesos', 'dolares', 'euros']
        
    def consultar_saldo(self):
        print('\nSu cuenta tiene los siguientes saldos:')
        if self.plan == '1':
            print('$',self.saldo_pesos,'ARS')
        elif self.plan == '2':
            print('$',self.saldo_pesos,'ARS')
            print('$',self.saldo_dolares,'USD')
        else:
            print('$',self.saldo_pesos,'ARS')
            print('$',self.saldo_dolares,'USD')
            print('€',self.saldo_euros,'EUR')    
                
    def ver_plan(self):
        if self.plan == '1':
            print (f'\nSu plan es básico.')     
        elif self.plan == '2':
            print(f'\nSu plan es premium.')
        else:
            print(f'\nSu plan es premium black.')
        
    def titular_cuenta(self):
        print(f'\nEl títular de la cuenta es: {self.nombre} {self.apellido}')
        
    def comprar_dolares(self,monto,venta_dolar):
        restar_pesos = (monto * venta_dolar)
        if restar_pesos > self.saldo_pesos:
            print('\nFondos insuficientes')
        else:
            self.saldo_pesos-=restar_pesos
            self.saldo_dolares+=monto
            print('\nSe descontaron $',round(restar_pesos,2),'ARS de tu cuenta.\nSe depositaron $',round(monto,2),'USD en tu cuenta.')
    
    def vender_dolares(self,monto,compra_dolar):
        pass
        
usuarios = {}  # Diccionario para almacenar a los usuarios        
usuario_plan_basico = Usuario('12345678','Juan','Gomez','1111','1') 
usuario_plan_premium = Usuario('87654321','Seba','Leal','2222','2') 
usuario_plan_premium_black = Usuario('43621230','Uriel','Pereyra','3333','3')

usuarios['12345678'] = usuario_plan_basico
usuarios['43621230'] = usuario_plan_premium_black
usuarios['87654321'] = usuario_plan_premium


def validar_plan(plan):
    planes_validos = ["1", "2", "3"]
    return plan in planes_validos

def validar_dni(dni):
    primer_digito = str(dni)[0]
        
    if primer_digito == '0':
        return False
    if not dni.isdigit():
        return False
    if len(dni) > 6 and len(dni) < 9 and int(dni) >= 1000000:
        return True
    else:
        return False

def validar_clave(clave):
    if not clave.isdigit():
        return False
    if len(clave)!=4:
        return False
    return True

def validar_nombre(nombre):
    if not nombre.isalpha():
        return False
    return True

            
def registrar_usuario():
    while True:
        dni = input('Ingrese su DNI: ')
        if validar_dni(dni):
            if dni in usuarios:
                print('\nYa existe un usuario registrado con ese DNI.')
            else:
                break
        else:
            print('DNI incorrecto. Por favor ingrese nuevamente ')

    while True:
        nombre = input('Ingrese su nombre: ')
        if validar_nombre(nombre):
            break
        else:
            print('Nombre inválido. Solo se permiten letras.')

    apellido = input('Ingrese su apellido: ')
    while not validar_nombre(apellido):
        apellido = input('Apellido inválido. Solo se permiten letras.')

    while True:
        clave = input('Ingrese su clave (4 dígitos): ')
            
        if validar_clave(clave):
            break
        else:
            print('Por favor ingrese una clave válida de 4 dígitos: ')

    while True:
        plan = input(f'\nSeleccione un plan:\n1. Básico(pesos)\n2.Premium(pesos-dolares)\n3.Premium Black(pesos-dolares-euros)\n')
        if validar_plan(plan):
            break
        else:
            print('Por favor ingrese un plan válido')
         
    nuevo_usuario = Usuario(dni, nombre, apellido, clave,plan)
    usuarios[dni] = nuevo_usuario
    print('\n----\nUsuario registrado exitosamente.\n----')
        
    
def iniciar_sesion():
   while True:
        try:
            dni = input('\nIngrese su DNI: ')
            clave = input("Ingrese su clave: ")
            
            if dni in usuarios and usuarios[dni].clave == clave:
                usuario_actual = usuarios[dni]
                print(f'\n¡Bienvenido/a, {usuario_actual.nombre} {usuario_actual.apellido}!')
                menu_usuario(usuario_actual)# Mostrar menú de usuario
                break
            else:
                print('\nDNI o clave incorrectos.')
                validar = input('\n0. Salir\n1. Volver a intentar\n¿Qué desea hacer? ')
                if validar == '0':
                    print('\nVolviendo...')
                    break
                elif validar == '1':
                    pass
                else:
                    validar = input('\n0. Salir\n1. Volver a intentar\n¿Qué desea hacer? ')
            
        except ValueError:
            print('Introduzca válores númericos por favor.')
            

def menu_usuario(usuario):
    while True:
        opcion = input('\nMenú de opciones:\n0. Salir\n1. Consultar saldo\n2. Depositar dinero\n3. Retirar dinero\n4. Cambiar divisas\n5. Ver plan\n6. Ver títular de la cuenta\nIngrese una opción: ')
        if opcion == '0':
            print('\nCerrando sesón...')
            break  # Salir del menú
        
        elif opcion == '1':
            usuario.consultar_saldo()
            
        elif opcion == '2':
            if usuario.plan == '1':
                while True:
                    try:
                        monto = float(input('\n0. Salir\n(Límite de un millón $ARS)\nIngrese un monto a depositar: '))
                        if monto == 0:
                            break
                        if 0 < monto < 1000000:
                            usuario.depositar_pesos(monto)  
                            break
                        else:
                            print('Ingrese un monto válido.')
                    except ValueError:
                        print('Ingrese un monto válido.')
                        
            if usuario.plan == '2':
                while True:
                    moneda = input('\n0. Salir\n1. ARS\n2. USD')
                    if moneda == '0':
                        break
                    elif moneda == '1':
                        try:
                            monto = float(input('\n0. Salir\n(Límite de un millón $ARS)\nIngrese un monto a depositar: '))
                            if monto == 0:
                                break
                            if 0 < monto < 1000000:
                                usuario.depositar_pesos(monto)  
                                break
                            else:
                                print('Ingrese un monto válido.')
                        except ValueError:
                            print('Ingrese un monto válido.')
                    elif moneda == '2':    
                        try:
                            monto = float(input('\n0. Salir\n(Límite de $10.000 USD)\nIngrese un monto a depositar: '))
                            if monto == 0:
                                break
                            if 0 < monto < 10000:
                                usuario.depositar_dolares(monto)  
                                break
                            else:
                                print('\nIngrese un monto válido.')
                        except ValueError:
                            print('\nIngrese un monto válido.')
                    else:
                        print('\nOpción inválida.')   
                        
                                     
        elif opcion == '3':
            print("\nSeleccione la moneda a retirar:")
            for i, moneda in enumerate(usuario.monedas_disponibles()):
                print(f"{i+1}. {moneda}")
            while True:
                try:
                    opcion_moneda = int(input("Ingrese el número de la moneda: ")) - 1
                    if 0 <= opcion_moneda < len(usuario.monedas_disponibles()):
                        
                        monto = float(input("Ingrese el monto a retirar: "))
                        moneda_seleccionada = usuario.monedas_disponibles()[opcion_moneda]
                        usuario.retirar_dinero(monto, moneda_seleccionada)
                        break
                    else:
                        print("Opción de moneda inválida. Por favor, seleccione una de las opciones mostradas.")
                except ValueError:
                        print("Ingrese un número válido para la opción de moneda.")
                        
        elif opcion == '4':
            if usuario.plan == '1':
                print('\nNo puede realizar estas operaciones. Necesita de un plan Premium o Premium Black.')
            elif usuario.plan == '2':
                while True:
                    accion = input('\n---COMPRA Y VENTA DE DOLARES---\n0. Salir\n1. Comprar\n2. Vender\nSeleccione una opción por favor: ')
                    if accion == '0':
                        break
                    elif accion == '1':
                        if usuario.saldo_pesos < 3000:
                            print('\nDebe tener mínimo $3000 ARS para comprar dolares')
                            pass
                        else:
                            while True:
                                try:
                                    print('\nEl valor para la venta de USD es de: $',venta_dolar)
                                    monto = float(input('\n0. Salir\nIngrese un monto a comprar:'))
                                    if monto == 0:
                                        break
                                    if monto > 0:
                                        print('Se descontarán $',round(monto*venta_dolar,2),'ARS')
                                        avanzar = input('\n0. No\n1.Si\nDesea continuar? ')
                                        if avanzar == '0':
                                            break
                                        if avanzar== '1':
                                            usuario.comprar_dolares(monto,venta_dolar)
                                            break
                                    else:
                                        print('Ingrese un valor correcto')
                                except ValueError:
                                    print('Ingrese un valor correcto')
                    elif accion == '2':
                        while True:
                            try:
                                print('\nEl valor para la venta de USD es de: $',venta_dolar)
                                monto = float(input('\n0. Salir\nIngrese un monto a comprar:'))
                                if monto == 0:
                                    break
                                if monto > 0:
                                    print('Se descontarán ARS $',round(monto*venta_dolar,2))
                                    avanzar = input('\n0. No\n1.Si\nDesea continuar? ')
                                    if avanzar == '0':
                                        break
                                    if avanzar== '1':
                                        usuario.comprar_dolares(monto,venta_dolar)
                                        break
                                else:
                                    print('Ingrese un valor correcto')
                            except ValueError:
                                print('Ingrese un valor correcto')
                        
        elif opcion == '5':
            usuario.ver_plan()
        elif opcion == '6':
            usuario.titular_cuenta()
        
        else:
            print("\nOpción inválida.")            

while True:
    
    opcion = input('\n---- Menú principal----\n1. Registrarse\n2. Iniciar sesión\n3. Salir\nIngrese una opción ----> ')

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        print('Saliendo...')
        break
    else:
        print('Opción inválida.')
