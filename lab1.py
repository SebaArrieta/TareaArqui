CONVERSOR = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
    'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
    'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
    'U': 30, 'V': 31,
}

def leer_archivo(file):
    with open(file, 'r') as f:
        txt = f.read()
    txt = txt.strip()
    lista_info = (txt.replace("\n", "-")).split("-")
    lista_numeros = []
    for info in lista_info:
        base, numero = info.split(';')
        base = num_decimal(10, base)  # Se hace esto para evitar usar el metodo int()
        lista_numeros.append((base, numero))
    return lista_numeros


def calcular_valores(lista_numeros: list, rango: int):
    size_n = len(lista_numeros)
    error_numerico = 0
    num_representables = []

    for base, numero in lista_numeros:
        representable = True
        for digito in numero:
            if CONVERSOR[digito] >= base:
                error_numerico += 1
                representable = False
                break
        if representable:
            num_representables.append((base, numero))

    num_representables = base_to_binario(num_representables)
    error_size = 0
    for num in num_representables:
        if len(num) > rango:
            error_size += 1

    return f"{size_n}, {error_numerico}, {error_size}"


def base_to_binario(num_representables):
    lista_num_binario = []
    for base, numero in num_representables:
        num = num_decimal(base, numero)

        num_binario = ""
        while(num != 0):
            num_binario = str(num % 2) + num_binario
            num = num // 2
        lista_num_binario.append(num_binario)

    return lista_num_binario


def num_decimal(base, numero):
    num = 0
    digitos = list(numero)
    digitos.reverse()
    for i, digito in enumerate(digitos):
        num += (base ** i) * CONVERSOR[digito]
    return num


rango = num_decimal(10,input("Ingresa el tamaño del registro: "))
print(calcular_valores(leer_archivo("numeros.txt"), rango))
