from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    available_permissions = {'criar_reservas': True, 'deletar_reservas': True, 'editar_reservas': True}

class Usuario(AbstractUserRole):
    available_permissions = {'criar_reservas': False, 'deletar_reservas': False, 'editar_reservas': False}