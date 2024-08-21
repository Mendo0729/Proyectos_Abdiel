import re

# Definición de subrutinas para manejar los diferentes mnemónicos
def add(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '0' + ''.join(hex(num)[2:] for num in numeros_enteros) + ' '
    return hexadecimal

def sub(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '1' + ''.join(hex(num)[2:] for num in numeros_enteros) + ' '
    return hexadecimal

def and1(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '2' + ''.join(hex(num)[2:] for num in numeros_enteros) + ' '
    return hexadecimal

def or1(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '3' + ''.join(hex(num)[2:] for num in numeros_enteros) + ' '
    return hexadecimal

def sr(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '4' + ''.join(hex(num)[2:] for num in numeros_enteros) + "0 "
    return hexadecimal

def sl(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = "2a" + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def slt(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = "60" + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def eq(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = "2b" + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def sb(linea):
    pos = linea.split()
    if len(pos) < 3:  # Asegurar que haya al menos tres elementos en la línea
        raise IndexError("La lista 'pos' no tiene suficientes elementos.")
    
    # Obtener el código de máquina en hexadecimal para los registros o valores
    reg1 = pos[1][1:]  # Elimina el primer carácter ('R') para obtener el registro 1
    reg2 = pos[2][1:]  # Elimina el primer carácter ('R') para obtener el registro 2
    
    # Crear el código hexadecimal para la instrucción 'sb'
    hexadecimal = 'a' + ''.join(hex(0)[2:]) + reg1 + reg2 + ' '
    
    return hexadecimal

def lb(linea):
    pos = linea.split()
    if len(pos) < 3:  # Asegurar que haya al menos tres elementos en la línea
        raise IndexError("La lista 'pos' no tiene suficientes elementos.")
    
    # Extraer los registros R1 y R2
    reg1 = pos[1][1:] if pos[1].startswith('R') else pos[1]  # Elimina 'R' si está presente
    reg2 = pos[2][1:] if pos[2].startswith('R') else pos[2]  # Elimina 'R' si está presente
    
    # Crear el código hexadecimal para la instrucción 'lb'
    hexadecimal = 'b' + ''.join(hex(0)[2:]) + reg1 + reg2 + ' '
    
    return hexadecimal

def li(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = 'a' + ''.join(hex(numeros_enteros[0])[2:]) + pos[2] + pos[3] + ' '
    return hexadecimal

def lui(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '9' + hex(numeros_enteros[0])[2:].zfill(3) + ' '
    return hexadecimal

def jmp(linea):
    etiqueta = pos[1]
    for etiq, valor in etiquetas:
        if etiq == etiqueta:
            hexadecimal = 'c' + hex(valor)[2:].zfill(3) + ' '
            return hexadecimal

def bra(linea):
    etiqueta = pos[1]
    for etiq, valor in etiquetas:
        if etiq == etiqueta:
            hexadecimal = 'd' + hex(valor)[2:].zfill(3) + ' '
            return hexadecimal

def jr(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = '8' + hex(numeros_enteros[0])[2:].zfill(3) + ' '
    return hexadecimal

def spc(linea):
    numeros = re.findall(r'\d+', linea.strip())
    if len(numeros) == 1:
        hexadecimal = 'a' + hex(int(numeros[0]))[2:].zfill(3) + ' '
    else:
        hexadecimal = 'a000 '
    return hexadecimal

def mul(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = hex(subr % 16)[2:] + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def div(linea):
    pos = linea.split()
    if len(pos) < 4:
        raise IndexError("La lista 'pos' no tiene suficientes elementos para DIV.")
    
    # Extraer los registros
    reg1 = pos[1]
    reg2 = pos[2]
    reg3 = pos[3]
    
    # Convertir los registros a hexadecimal en el orden correcto
    hex_reg1 = format(int(reg1[1:]), 'x')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    hex_reg2 = format(int(reg2[1:]), 'x')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    hex_reg3 = format(int(reg3[1:]), 'x')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    
    # Construir el código hexadecimal para DIV
    hexadecimal = 'b' + hex_reg1 + hex_reg2 + hex_reg3 + ' '
    
    return hexadecimal

def rem(linea):
    pos = linea.split()
    if len(pos) < 4:
        raise IndexError("La lista 'pos' no tiene suficientes elementos para REM.")
    reg1 = pos[1]
    reg2 = pos[2]
    reg3 = pos[3]

    hex_reg1 = format(int(reg1[1:]), 'x')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    hex_reg2 = format(int(reg2[1:]), 'x')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    hex_reg3 = format(int(reg3[1:]), 'x')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    
    hexadecimal = 'b' + hex_reg1 + hex_reg2 + hex_reg3 + ' '

    return hexadecimal

def xor(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = 'c' + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def rr(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = hex(subr % 16)[2:] + ''.join(hex(numero)[2:] for numero in numeros_enteros) + "0 "
    return hexadecimal

def rl(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = hex(subr % 16)[2:] + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def sgt(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = hex(subr % 16)[2:] + "0" + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def neq(linea):
    numeros = re.findall(r'\d+', linea.strip())
    numeros_enteros = [int(numero) for numero in numeros]
    hexadecimal = "2e" + ''.join(hex(numero)[2:] for numero in numeros_enteros) + ' '
    return hexadecimal

def mov(linea):
    pos = linea.split()
    if len(pos) < 3:  # Ajusta según el número mínimo de elementos que esperas en 'pos'
        raise IndexError("La lista 'pos' no tiene suficientes elementos.")

    # Extraer los registros
    reg_destino = pos[1]
    reg_origen = pos[2]

    # Convertir los registros a hexadecimal en el orden correcto
    hex_reg_destino = format(int(reg_destino[1:]), 'X')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales
    hex_reg_origen = format(int(reg_origen[1:]), 'X')  # Quita la 'R' y convierte a hexadecimal sin ceros adicionales

    # Construir el código hexadecimal para MOV
    hexadecimal = 'c'+ ''.join(hex(0)[2:]) + hex_reg_origen + hex_reg_destino + ' '

    return hexadecimal


def swp(linea):
    pos = linea.split()
    if len(pos) < 2:
        raise IndexError("La lista 'pos' no tiene suficientes elementos para SWP.")
    
    hexadecimal = 'b' + ''.join(hex(0)[2:]) + pos[1] + ' '
    return hexadecimal

def rst(linea):
    pos = linea.split()
    if len(pos) < 1:
        raise IndexError("La lista 'pos' no tiene suficientes elementos para RST.")
    
    hexadecimal = 'c' + ''.join(hex(0)[2:]) + ' '
    return hexadecimal

def bbr(linea):
    pos = linea.split()
    if len(pos) < 2:
        raise IndexError("La lista 'pos' no tiene suficientes elementos para BBR.")
    
    hexadecimal = 'e' + ''.join(hex(0)[2:]) + pos[1] + ' '
    return hexadecimal

def cls(linea):
    pos = linea.split()
    if len(pos) < 1:
        raise IndexError("La lista 'pos' no tiene suficientes elementos para CLS.")
    
    hexadecimal = 'f' + ''.join(hex(0)[2:]) + ' '
    return hexadecimal



# Lista de mnemónicos y sus subrutinas correspondientes
nemonicos = [
    "ADD", "SUB", "AND", "OR", "SR", "SL", "SLT", "EQ", "SB", "LB", "LI", "LUI",
    "JMP", "BRA", "JR", "SPC", "MUL", "DIV", "REM", "XOR", "RR", "RL", "SGT", 
    "NEQ", "MOV", "SWP", "RST", "BBR", "CLS"
]
subrutinas = [
    add, sub, and1, or1, sr, sl, slt, eq, sb, lb, li, lui, jmp, bra, jr, spc,
    mul, div, rem, xor, rr, rl, sgt, neq, mov, swp, rst, bbr, cls
]

etiquetas = []   # lista vacía de duplas [(etiqueta, adress), (etiqueta, adress), ....]
adress = 0       # dirección inicial de la primera instrucción de ensamblador
new_archivo = open('C:\\Users\\abdie\\OneDrive\\Escritorio\\practica\\examen Final OAC\\P41.ASM', "w")  # crear un archivo vacío
with open('C:\\Users\\abdie\\OneDrive\\Escritorio\\practica\\examen Final OAC\\P31.ASM') as archivo:    # abrir el archivo a depurar
    for linea in archivo:                             # recorrer el archivo línea por línea
        w = ''                                        # iniciar una cadena vacía w=''
        lis = linea.split()                           # cada línea del archivo convertirla en lista
        if len(lis) == 0:                             # lista está vacía?
            continue                                  # sí, descartar esta lista
        for l in lis:                                 # recorrer la lista
            if l.startswith('/'):                     # el primer carácter de la lista es '/'?
                break                                 # sí, descartar la lista
            elif l.startswith(':'):                   # el primer carácter es ':'?
                etiquetas.append((l, adress))         # sí, ingresar datos a etiquetas [(etiqueta, adress)]
            else:                                     # si no
                w += l.upper() + ' '                  # concatenar en w el elemento en mayúscula
        if len(w) > 0:                                # si w tiene contenido
            adress += 1                               # incrementar el adress
            new_archivo.write(w.strip() + '\n')       # escribir w en el archivo con '\n'
print(etiquetas)                                      # imprimir las etiquetas
new_archivo.close()                                   # cerrar el archivo

# Apertura del archivo ASM y procesamiento línea por línea
with open('C:\\Users\\abdie\\OneDrive\\Escritorio\\practica\\examen Final OAC\\P41.ASM') as archivo:
    for l in archivo:
        pos = l.split()
        if len(pos) == 0:
            continue
        nemonico = pos[0]
        OK = 0
        for subr in range(len(nemonicos)):  # Asegúrate de no exceder el tamaño de la lista nemonicos
            if nemonico == nemonicos[subr]:
                try:
                    subrutinas[subr](l)
                except IndexError as e:
                    print(f"Error en la línea '{l.strip()}': {e}")
                OK = 1
                break
        if OK == 0:
            print("Este nemónico no existe: ", l.strip())
  

# Procesamiento del archivo depurado
# Abrir el archivo para escribir el código compilado
archivo_code = open('C:\\Users\\abdie\\OneDrive\\Escritorio\\practica\\examen Final OAC\\code.rom', "w")
archivo_code.write("v2.0 raw\n")

with open('C:\\Users\\abdie\\OneDrive\\Escritorio\\practica\\examen Final OAC\\P41.ASM') as archivo:
    for linea in archivo:
        pos = linea.split()
        if len(pos) == 0:
            continue
        
        nemonico = pos[0]  # Suponiendo que el primer elemento es el nemónico
        OK = False
        
        for subr in range(len(nemonicos)):
            if nemonico == nemonicos[subr]:
                try:
                    hexadecimal = subrutinas[subr](linea)
                    if hexadecimal is not None:
                        archivo_code.write(hexadecimal + '\n')  # Escribir código de máquina
                    OK = True
                    break
                except Exception as e:
                    print(f"Error en la línea: {e}")
        
        if not OK:
            print(f"Error: Nemónico no reconocido o formato incorrecto en la línea: {linea.strip()}")

archivo_code.close()