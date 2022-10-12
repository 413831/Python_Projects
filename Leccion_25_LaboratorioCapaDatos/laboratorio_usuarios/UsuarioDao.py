from CursorDelPool import CursorDelPool
from laboratorio_usuarios.Usuario import Usuario
from logger_base import log

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = list()
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'usuario a insertar: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'usuario actualizada: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {usuario}')
            return cursor.rowcount
        
if __name__ == '__main__':

    # Insertar un registro
    # usuario1 = Usuario(username='Manuela', password='secreta')
    # usuarios_insertados = UsuarioDao.insertar(usuario1)
    # log.debug(f'usuarios insertados: {usuarios_insertados}')

    # Actualizar un registro
    # usuario1 = Usuario(2, 'Manuel', 'sarasa')
    # usuarios_actualizados = UsuarioDao.actualizar(usuario1)
    # log.debug(f'usuarios actualizados: {usuarios_actualizados}')

    # Eliminar un registro
    # usuario1 = Usuario(id_usuario=2)
    # usuarios_eliminados = UsuarioDao.eliminar(usuario1)
    # log.debug(f'usuarios eliminadas: {usuarios_eliminados}')

    # Seleccionar objetos
    usuarios = UsuarioDao.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)