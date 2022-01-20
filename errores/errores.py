from re import L


# try:
#     while True:
#         print('Hola')
# except NameError:
#     print('l no está definida.')
# except KeyboardInterrupt:
#    print('Salida forzosa.')
# finally:
#     print('Terminó la ejecución.')

try:
    raise IOError
except IOError:
    print('Ocurrió un error')
