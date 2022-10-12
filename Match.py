# Definicion
def http_error(status):
    match status:
        case 400:
            return "Solicitud incorrecta"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Anda funciona mal con internet"
# Ejecucion
status = 418

response = http_error(status)
print(response)