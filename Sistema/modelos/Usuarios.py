from utilitarios.login import login

class Usuarios:
    def __init__(self, id, nome, email, senha_hash, tipo, ativo):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.tipo = tipo
        self.ativo = ativo

    def autenticar(self):
        return login()

    def alterar_senha(self):
        pass

    def validar_permissao(self):
        pass

    def visualizar_detalhes(self):
        pass

    def listar_acoes(self):
        pass

class Administrador(Usuarios):
    def __init__(self, id, nome, email, senha_hash, ativo):
        super().__init__(id, nome, email, senha_hash, "Administrador", ativo)

    def criar_usuario(self):
        pass

    def editar_usuario(self):
        pass

    def desativar_usuario(self):
        pass

    def atribuir_papel(self):
        pass
