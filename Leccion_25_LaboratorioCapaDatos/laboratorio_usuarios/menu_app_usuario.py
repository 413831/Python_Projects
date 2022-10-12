from laboratorio_usuarios.Usuario import Usuario
from laboratorio_usuarios.UsuarioDao import UsuarioDao
from logger_base import log

opcion = None

while opcion != 5:
    print('Opciones')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Ingrese el username: ')
        password_var = input('Ingrese el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id del usuario a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
else:
    log.info('Salimos de la aplicación...')


